from es import *


class IndexStatistics(object):
    doc_count = 0
    avg_doc_length = 0
    vocab_size = 0

    def get_doc_count(self):
        return get_doc_count()

    def get_avg_doc_length(self):
        field_statistics = get_field_statistics()
        return field_statistics['sum_ttf'] / field_statistics['doc_count']

    def get_vocab_size(self):
        return get_vocab_size()

    def __init__(self):
        self.doc_count = self.get_doc_count()
        self.avg_doc_length = self.get_avg_doc_length()
        self.vocab_size = self.get_vocab_size()

class DocumentStatistics(object):
    doc_no = ''
    length = 0

    def __init__(self, doc_no):
        self.doc_no = doc_no
        body = get_es_script('get_length')
        body['query']['terms']['_id'] = [doc_no]
        self.length = search(body = body)['hits']['hits'][0]['fields']['doc_length']
