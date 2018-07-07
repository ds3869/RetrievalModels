from models.es_built_in_model import BuiltInModel
from models.okapi_tf_model import OkapiTFModel
from models.tf_idf_model import TFIDFModel
from models.okapi_bm25 import OkapiBM25
from models.laplace_unigram_lm_model import LaplaceUnigramLMModel
from utils.constants import Constants
from utils.es import get_term_statistics
from utils.statistics import DocumentStatistics
from utils.text import build_query_list, get_stopwords, get_file_list, write_output
import sys
import os
import threading

document_statistics = {}
query_list = {}

def run_built_in():
    print "Processing: built in model"
    built_in = BuiltInModel()
    for key in query_list:
        results = built_in.query(query_list[key])['hits']['hits']
        rank = 1
        for result in results:
            write_output(
                    model = 'es',
                    query_no = str(key),
                    doc_no = result['_id'],
                    rank = str(rank),
                    score = str(result['_score']))
            rank += 1

def run_okapi_tf():
    print "Processing: Okapi TF model"
    okapi_tf = OkapiTFModel(document_statistics)
    print query_list
    for q_no in query_list:
        query = query_list[q_no]
        tf_collection  = []
        words = query.split(' ')

        print "Collecting the tf values"
        for word in words:
            w_d, tf = get_term_statistics(word)
            tf_collection.append(tf)

        results = okapi_tf.query(query, tf_collection)
        rank = 1
        for key, value in sorted(results.iteritems(), key=lambda (k,v): (v,k), reverse=True):
            if rank > Constants.MAX_OUTPUT or value <= 0:
                break
            write_output(
                    model = 'okapi_tf',
                    query_no = str(q_no),
                    doc_no = str(key),
                    rank = str(rank),
                    score = str(value))
            rank += 1
    print "Okapi TF Done"

def run_tf_idf():
    print "Processing: TF-IDF model"
    tfidf = TFIDFModel(document_statistics)
    for q_no in query_list:
        query = query_list[q_no]
        tf_collection  = []
        wd_collection = []
        words = query.split(' ')

        print "Collecting the tf values"
        for word in words:
            wd, tf = get_term_statistics(word)
            wd_collection.append(wd)
            tf_collection.append(tf)

        results = tfidf.query(query, wd_collection, tf_collection)
        rank = 1
        for key, value in sorted(results.iteritems(), key=lambda (k,v): (v,k), reverse=True):
            if rank > Constants.MAX_OUTPUT or value <= 0:
                break
            write_output(
                    model = 'tfidf',
                    query_no = str(q_no),
                    doc_no = str(key),
                    rank = str(rank),
                    score = str(value))
            rank += 1
    print "TF-IDF Done"

def run_bm25():
    print "Processing: Okapi BM25 model"
    bm25 = OkapiBM25(document_statistics)
    for q_no in query_list:
        query = query_list[q_no]
        tf_collection  = []
        wd_collection = []
        words = query.split(' ')

        print "Collecting the tf values"
        for word in words:
            wd, tf = get_term_statistics(word)
            wd_collection.append(wd)
            tf_collection.append(tf)

        results = bm25.query(query, wd_collection, tf_collection)
        rank = 1
        for key, value in sorted(results.iteritems(), key=lambda (k,v): (v,k), reverse=True):
            if rank > Constants.MAX_OUTPUT or value <= 0:
                break
            write_output(
                    model = 'bm25',
                    query_no = str(q_no),
                    doc_no = str(key),
                    rank = str(rank),
                    score = str(value))
            rank += 1
    print "BM25 Done"

def run_laplace_unigram():
    print "Processing: Unigram LM with Laplace model"
    laplace_unigram = LaplaceUnigramLMModel(document_statistics)
    print query_list
    for q_no in query_list:
        query = query_list[q_no]
        tf_collection  = []
        words = query.split(' ')

        print "Collecting the tf values"
        for word in words:
            w_d, tf = get_term_statistics(word)
            tf_collection.append(tf)

        results = laplace_unigram.query(query, tf_collection)
        rank = 1
        for key, value in sorted(results.iteritems(), key=lambda (k,v): (v,k), reverse=True):
            if rank > Constants.MAX_OUTPUT or value == 0:
                break
            write_output(
                    model = 'laplace_unigram',
                    query_no = str(q_no),
                    doc_no = str(key),
                    rank = str(rank),
                    score = str(value))
            rank += 1
    print "Unigram LM with Laplace done"

def build_document_statistics():
    print "Building document statistics"
    file_list = get_file_list()
    for doc_no in file_list:
        stats = DocumentStatistics(doc_no)
        document_statistics[doc_no] = stats.length[0]

if __name__ == '__main__':
    """Main function
    """
    threads = []

    query_list = build_query_list()
    build_document_statistics()
    run_laplace_unigram()

    # t1 = threading.Thread(target=run_okapi_tf)
    # threads.append(t1)
    # t2 = threading.Thread(target=run_tf_idf)
    # threads.append(t2)
    # t3 = threading.Thread(target=run_)
    # threads.append(t2)

    # t1.start()
    # t2.start()

