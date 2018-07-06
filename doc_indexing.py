from bs4 import BeautifulSoup
import os
from utils.constants import Constants
from utils.data import Data
from utils.es import *
from utils.text import *

data_collection = []

if es.ping():
    # Delete already existing index
    delete_index()

    # Create initial index
    create_index()
    
    # Go through all of the corpus and store it
    for f in os.listdir(Constants.DATA_PATH):
        if f.startswith('ap'):
            with open(Constants.DATA_PATH + f, 'r') as d:
                d = d.read()
                docs = find_docs_by_regex(d)

                print "Processing {0}, with {1} docs".format(f, len(docs)) 

                for doc in docs:
                    doc_id = find_doc_no_by_regex(doc)
                    text = find_all_texts_by_regex(doc)
                    doc_length = len(text.split(' '))

                    store_document(doc_id, text, doc_length)


