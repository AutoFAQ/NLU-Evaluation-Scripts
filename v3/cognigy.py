from nlu_converters.cognigy_converter import CognigyConverter
from nlu_analysers.cognigy_analyser import CognigyAnalyser

API_KEY = "<api key>"
PROJECT_ID = "<project id>"
FLOW_PARENT_ID = "<flow parent id>"
FLOW_ID = "<flow parent id>"
ENDPOINT_URL = "<endpoint url>"

cognigy_converter = CognigyConverter(API_KEY,
                                     "https://api-demo.cognigy.ai/projects/" + PROJECT_ID,
                                     FLOW_PARENT_ID,
                                     FLOW_ID
                                    )
cognigy_converter.import_corpus("WebApplicationsCorpus.json")
cognigy_converter.export("WebApplicationsTraining_Cognigy.json")

cognigy_analyser = CognigyAnalyser(ENDPOINT_URL)
cognigy_analyser.get_annotations("TransportCorpusSplit.json", "TransportAnnotations_Cognigy.json")
cognigy_analyser.analyse_annotations("TransportAnnotations_Cognigy.json", "TransportCorpusSplit.json", "TransportAnalysis_Cognigy.json")
