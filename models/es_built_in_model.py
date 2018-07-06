import sys
sys.path.insert(0, '/home/prdx/Documents/CS6200-Summer/A1/')

from utils.es import *
from utils.constants import Constants
from utils.text import build_query_list, get_stopwords, write_output

class BuiltInModel(object):
    def score(self):
        print "Processing: built in model"
        query_list = build_query_list()
        for key in query_list:
            results = self.query(query_list[key])['hits']['hits']
            rank = 1
            for result in results:
                write_output(
                        model = 'es',
                        query_no = str(key),
                        doc_no = result['_id'],
                        rank = str(rank),
                        score = str(result['_score']))
                rank += 1

    def query(self, keywords = ""):
        return search(keywords)
