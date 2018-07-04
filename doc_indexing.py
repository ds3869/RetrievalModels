from bs4 import BeautifulSoup
from elasticsearch5 import Elasticsearch
import os
import json

DATA_PATH = '/home/prdx/Documents/CS6200-Summer/A1/AP_DATA/ap89_collection/'
ES_SCRIPTS_PATH = '/home/prdx/Documents/CS6200-Summer/A1/es/'
INDEX_NAME = 'ap89_collection'

es = Elasticsearch()

class Data(object):
    doc_id = ""
    text = ""

    def __init__(self, doc_id, text):
        self.doc_id = doc_id
        self.text = text

def sanitize(text):
    return text.strip().replace('\n', '')

def find_doc_no(soup):
    return soup.find('DOCNO').string.strip()

def find_all_texts(soup):
    text = ''
    elements = soup.findAll('TEXT')
    for element in elements:
        text = text + ' ' + sanitize(element.string)

    return text

def get_es_script(script_name):
    with open(ES_SCRIPTS_PATH + script_name + '.json') as s:
        body = json.load(s)
    return body

data_collection = []

if es.ping():
    # Delete already existing index
    es.indices.delete(index = INDEX_NAME, ignore = [400, 404])

    # Create initial index
    es.indices.create(INDEX_NAME, 
            body = get_es_script('index_create'))
    
    # Go through all of the corpus and store it
    for f in os.listdir(DATA_PATH):
        if f.startswith('ap'):
            with open(DATA_PATH + f) as d:
                soup = BeautifulSoup(d, "lxml-xml")

                docs = soup.findAll('DOC')

                for doc in docs:
                    doc_id = find_doc_no(doc)
                    text = find_all_texts(doc)

                    # Store it in case we need it
                    data_collection.append(Data(doc_id, text))

                    es.index(index = INDEX_NAME,
                            doc_type = 'document',
                            id = doc_id,
                            body = {
                                "doc_id": doc_id,
                                "text": text,
                                }
                            )

