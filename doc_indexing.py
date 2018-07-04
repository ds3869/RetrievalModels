from bs4 import BeautifulSoup
from elasticsearch5 import Elasticsearch
import os
import json

data_path = '/home/prdx/Documents/CS6200-Summer/A1/AP_DATA/ap89_collection/'

'For list of stop words, stem words'
es_script_path = '/home/prdx/Documents/CS6200-Summer/A1/es/'
es = Elasticsearch()

class Data(object):
    doc_id = ""
    text = ""

    def __init__(self, doc_id, text):
        self.doc_id = doc_id
        self.text = text

def find_and_sanitize(soup, params):
    return soup.find(params).string.strip().replace('\n', '')

def get_es_script(script_name):
    with open(es_script_path + script_name + '.json') as s:
        body = json.load(s)
    return body

data_collection = []


if es.ping():
    # Delete already existing index
    es.indices.delete(index = 'ap89_collection', ignore = [400, 404])

    # Create initial index
    es.indices.create('ap89_collection', 
            body = get_es_script('index_create'))
    
    # Go through all of the corpus and store it
    for doc in os.listdir(data_path):
        if doc.startswith('ap'):
            with open(data_path + doc) as d:
                soup = BeautifulSoup(d, "lxml-xml")
                doc_id = find_and_sanitize(soup, 'DOCNO')
                text = find_and_sanitize(soup, 'TEXT')

                # Store it in case we need it
                data_collection.append(Data(doc_id, text))

                es.index(index = 'ap89_collection',
                        doc_type = 'document',
                        id = doc_id,
                        body = {
                            "doc_id": doc_id,
                            "text": text,
                            }
                        )

