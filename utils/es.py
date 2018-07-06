from elasticsearch5 import Elasticsearch
from constants import Constants
import json

es = Elasticsearch()

def create_index():
    """Create new index
    """
    es.indices.create(Constants.INDEX_NAME, 
            body = get_es_script('index_create'))

def delete_index():
    """Delete existing index
    """
    es.indices.delete(index = Constants.INDEX_NAME, ignore = [400, 404])

def get_es_script(script_name):
    """Read es json file
    return dictionary of the body
    """
    with open(Constants.ES_SCRIPTS_PATH + script_name + '.json') as s:
        body = json.load(s)
    return body

def get_doc_count():
    """Retrieve document count from ES
    return int number of documents in the corpus
    """
    result = es.count(index = Constants.INDEX_NAME,
            doc_type = Constants.DOC_TYPE)
    return result['count']

def get_field_statistics(_id = 'AP890201-0001'):
    """Get field statistics
    return dictionary of field statistics
    """
    result = es.termvectors(index = Constants.INDEX_NAME, 
            doc_type = Constants.DOC_TYPE,
            id = _id, 
            body = get_es_script('term_vectors')) 
    return result["term_vectors"]['text']['field_statistics']

def get_terms_statistics(_id = 'AP890201-0001'):
    """Get terms statistics
    return dictionary of term statistics
    """
    result = es.termvectors(index = Constants.INDEX_NAME, 
            doc_type = Constants.DOC_TYPE,
            id = _id, 
            body = get_es_script('term_vectors')) 
    return result["term_vectors"]['text']['terms']


def get_vocab_size():
    """Get vocabulary size of the corpus
    return int vocabulary size
    """
    body = get_es_script('agg_vocab_size')
    print body
    return search("", body)['aggregations']['vocabSize']['value']


def search(keywords = "", body = {}):
    """ES Built-in search command
    parameter string keyword to search
    return list of matched documents
    """
    if len(body) == 0 and keywords != "":
        body = get_es_script('search')
        body['query']['match']['text'] = keywords 
        body['size'] = Constants.MAX_OUTPUT

    res = es.search(index = Constants.INDEX_NAME,
            body = body
        )
    return res

def store_document(doc_id, text, doc_length):
    es.index(index = Constants.INDEX_NAME,
            doc_type = Constants.DOC_TYPE,
            id = doc_id,
            body = {
                "doc_id": doc_id,
                "text": text,
                "doc_length": doc_length
                }
            )
