from bs4 import BeautifulSoup
import os
from utils.constants import Constants
from utils.data import Data
from utils.es import *
from utils.text import *

data_collection = []

if es.ping():
    # Delete already existing index
    es.indices.delete(index = Constants.INDEX_NAME, ignore = [400, 404])

    # Create initial index
    es.indices.create(Constants.INDEX_NAME, 
            body = get_es_script('index_create'))
    
    # Go through all of the corpus and store it
    for f in os.listdir(Constants.DATA_PATH):
        if f.startswith('ap'):
            with open(Constants.DATA_PATH + f) as d:
                soup = BeautifulSoup(d, "lxml-xml")

                docs = soup.findAll('DOC')

                print "Processing {0}, with {1} docs".format(f, len(docs)) 

                for doc in docs:
                    doc_id = find_doc_no(doc)
                    text = find_all_texts(doc)

                    # Store it in case we need it
                    data_collection.append(Data(doc_id, text))

                    es.index(index = Constants.INDEX_NAME,
                            doc_type = Constants.DOC_TYPE,
                            id = doc_id,
                            body = {
                                "doc_id": doc_id,
                                "text": text,
                                }
                            )

