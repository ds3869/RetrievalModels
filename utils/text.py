import os
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


