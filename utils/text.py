import os
import re
from constants import Constants

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

def get_file_list():
    file_list = []
    try:
        with open(Constants.DOCLIST_PATH) as f:
            file_list = f.readlines()
    except:
        print "Processed file does not exist. Processing..."
        os.system('./utils/clean_file_list.sh')
        with open(Constants.DOCLIST_PATH) as f:
            file_list = f.readlines()
    
    file_list = [x.strip() for x in file_list] 
    return file_list

def get_stopwords():
    stopwords = []
    extra_stopwords = [
            'cite',
            'describe',
            'discuss',
            'document',
            'identify',
            'include',
            'predict',
            'report'
            ]
    try:
        stopwords = open(Constants.STOPWORDS_PATH, 'r').read().split('\n')
    except:
        print "Cannot open file"

    # Append few extra stopwords
    stopwords += extra_stopwords
    return stopwords

def remove_stopwords(text):
    stopwords = get_stopwords()
    text = text.lower()
    words = text.split(" ")
    for s in stopwords:
        while s in words:
            words.remove(s)
    text = ' '.join(words)
    
    return text

def remove_punctuation(text):
    punctuations = ['.', ',', '"', '-', '(', ')']
    for p in punctuations:
        text = text.replace(p, '')
    return text

def build_query_list():
    key_val = []
    query_list = {}
    try:
        f = open(Constants.QUERY_LIST_PATH, 'r').read()
        f = remove_punctuation(f)
        f = f.split('\n')

        for q in f:
            key_val = re.split('\s{3}', q.strip())
            if len(key_val) == 2:
                key_val[1] = remove_stopwords(key_val[1])
                query_list[key_val[0]] = key_val[1]

        return query_list

    except Exception as exception:
        print exception


def write_output(model, query_no, doc_no, rank, score):
    try:
        out = open(Constants.RESULTS_PATH + model + '.txt', 'a')
        out.write(query_no + ' Q0 ' + doc_no + ' ' +
                rank + ' ' + score + ' Exp\n')
        out.close()
    except Exception as exception:
        print exception


