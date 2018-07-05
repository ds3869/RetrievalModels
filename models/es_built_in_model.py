import sys
sys.path.insert(0, '/home/prdx/Documents/CS6200-Summer/A1/')

from utils.es import *
from utils.constants import Constants
from utils.text import build_query_list, get_stopwords, write_output

class BuiltInModel(object):
    def score(self):
        query_list = build_query_list()
        for key in query_list:
            results = self.query(query_list[key])
            rank = 1
            for result in results:
                write_output(
                        model = 'es',
                        query_no = str(key),
                        doc_no = result['_id'],
                        rank = str(rank),
                        score = str(result['_score']))
                rank += 1

    def query(self, keywords = "United States Nuclear"):
        body = get_es_script('search')
        body['query']['match']['text'] = keywords 
        res = es.search(index = Constants.INDEX_NAME,
                body = body
                )
        return res['hits']['hits']



builtin = BuiltInModel()
builtin.score()
