from elasticsearch5 import Elasticsearch
from utils.constants import Constants
import json

es = Elasticsearch()

def get_es_script(script_name):
    with open(Constants.ES_SCRIPTS_PATH + script_name + '.json') as s:
        body = json.load(s)
    return body
