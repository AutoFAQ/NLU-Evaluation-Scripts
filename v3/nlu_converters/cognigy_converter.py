import requests
import time

from .converter import *


class CognigyConverter(Converter):
    def __init__(self, api_key, project_url, flow_parent_id, flow_id):
        super(CognigyConverter, self).__init__()
        self.api_key = api_key
        self.cognigy_intents = {}
        self.keyphrases = ""
        self.project_url = project_url
        self.flow_parent_id = flow_parent_id
        self.flow_id = flow_id

    def __add_intent(self, intent):
        if intent in self.cognigy_intents:
            return 0

        intent_payload = {
            "confirmationSentence": "",
            "currentlyValid": True,
            "defaultReply": None,
            "exampleSentences": [],
            "flowId": self.flow_id,
            "id": None,
            "name": intent,
            "rules": [],
            "type": None
        }
        self.cognigy_intents[intent] = intent_payload

    def __add_entity(self, tag, text):
        self.keyphrases += "\"" + text + "\",\"" + tag + "\",\n"

    def __add_utterance(self, intent, text):
        example_sentence = {"text": text, "type": "user"}
        self.cognigy_intents[intent]["exampleSentences"].append(example_sentence)

    def import_corpus(self, file):
        data = json.load(open(file))

        # meta data
        self.create_lexicon_payload = {"name": data["name"]}

        # training data
        for s in data["sentences"]:
            if s["training"]:  # only import training data
                # intents
                self.__add_intent(s["intent"])
                # entities
                for e in s["entities"]:
                    self.__add_entity(e["entity"], e["text"])
                    # utterances
                self.__add_utterance(s["intent"], s["text"])

    def export(self, file):
        cognigy_json = {}
        cognigy_json["create_lexicon_payload"] = self.create_lexicon_payload
        cognigy_json["import_lexicon_payload"] = {"type": "csv", "data": self.keyphrases}
        cognigy_json["cognigy_intents"] = self.cognigy_intents

        create_lexicon_url = self.project_url + "/lexicons/"
        create_lexicon_response = requests.post(create_lexicon_url,
                                                data=cognigy_json["create_lexicon_payload"],
                                                headers={"x-api-key": self.api_key}).json()

        time.sleep(2)

        import_lexicon_url = self.project_url + "/lexicons/" + create_lexicon_response["_id"] + "/import"
        import_lexicon_response = requests.post(import_lexicon_url,
                                                data=cognigy_json["import_lexicon_payload"],
                                                headers={"x-api-key": self.api_key}).json()

        create_intent_url = self.project_url + "/flows/" + self.flow_parent_id + "/flow/" + self.flow_id + "/intents/"
        for intent_payload in self.cognigy_intents.iteritems():
            requests.post(create_intent_url,
                          json=intent_payload[1],
                          headers={"x-api-key": self.api_key}).json()
