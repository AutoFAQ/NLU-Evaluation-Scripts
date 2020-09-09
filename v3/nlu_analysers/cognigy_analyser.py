from analyser import *
import random
import string

class CognigyAnalyser(Analyser):
    @staticmethod
    def detokenizer(s):
        return s.replace(" . ", ".").replace(" , ", ",").replace(" ' ", "'").replace(" ? ", "?").replace(" ! ",
                                                                                                         "!").replace(
            " & ", "&").replace(" : ", ":").replace(" - ", "-").replace(" / ", "/").replace(" ( ", "(").replace(" ) ",
                                                                                                                ")")

    def __init__(self, endpoint_url):
        super(CognigyAnalyser, self).__init__()
        self.url = endpoint_url

    def get_annotations(self, corpus, output):
        data = json.load(open(corpus))
        annotations = {'results': []}

        for s in data["sentences"]:
            if not s["training"]:  # only use test data
                random_id = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(12))
                answer = requests.post(self.url, json={"userId": random_id, "sessionId": random_id, "text": s['text']}, headers={}).json()
                annotations['results'].append(answer["data"])

        file = open(output, "w")
        file.write(
            json.dumps(annotations, sort_keys=False, indent=4, separators=(',', ': '), ensure_ascii=False).encode(
                'utf-8'))
        file.close()

    def analyse_annotations(self, annotations_file, corpus_file, output_file):
        analysis = {"intents": {}, "entities": {}}

        corpus = json.load(open(corpus_file))
        gold_standard = []
        for s in corpus["sentences"]:
            if not s["training"]:  # only use test data
                gold_standard.append(s)

        annotations = json.load(open(annotations_file))

        i = 0
        for a in annotations["results"]:
            if not 'query' in a:
                print('error: missing query')
                continue

            if not a["query"] == gold_standard[i]["text"]:
                print a["query"]
                print gold_standard[i]["text"]
                print "WARNING! Texts not equal"

            # intent
            aIntent = a["topScoringIntent"]["intent"]
            oIntent = gold_standard[i]["intent"]

            Analyser.check_key(analysis["intents"], aIntent)
            Analyser.check_key(analysis["intents"], oIntent)

            if aIntent == oIntent:
                # correct
                analysis["intents"][aIntent]["truePos"] += 1
            else:
                # incorrect
                analysis["intents"][aIntent]["falsePos"] += 1
                analysis["intents"][oIntent]["falseNeg"] += 1

            # entities
            aEntities = a["entities"]
            oEntities = gold_standard[i]["entities"]

            for x in aEntities:
                Analyser.check_key(analysis["entities"], x["type"])

                if len(oEntities) < 1:  # false pos
                    analysis["entities"][x["type"]]["falsePos"] += 1
                else:
                    truePos = False

                    for y in oEntities:
                        if CognigyAnalyser.detokenizer(x["entity"]) == y["text"].lower():
                            if x["type"] == y["entity"]:  # truePos
                                truePos = True
                                oEntities.remove(y)
                                break
                            else:  # falsePos + falseNeg
                                analysis["entities"][x["type"]]["falsePos"] += 1
                                analysis["entities"][y["entity"]]["falseNeg"] += 1
                                oEntities.remove(y)
                                break
                    if truePos:
                        analysis["entities"][x["type"]]["truePos"] += 1
                    else:
                        analysis["entities"][x["type"]]["falsePos"] += 1

            for y in oEntities:
                Analyser.check_key(analysis["entities"], y["entity"])
                analysis["entities"][y["entity"]]["falseNeg"] += 1

            i += 1

        self.write_json(output_file, json.dumps(analysis, sort_keys=False, indent=4, separators=(',', ': '),
                                                ensure_ascii=False).encode('utf-8'))
