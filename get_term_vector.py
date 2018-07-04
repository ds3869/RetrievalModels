from utils.constants import Constants
from utils.es import *
from utils.text import *

es = Elasticsearch()

if es.ping():
    file_list = get_file_list()
    print file_list

    result = es.termvectors(index = Constants.INDEX_NAME, 
            doc_type = Constants.DOC_TYPE,
            id = 'AP890201-0001',
            body = get_es_script('term_vectors'))["term_vectors"]    
    print result
