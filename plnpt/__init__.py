
import urllib
import urllib.request
import json

API = 'http://api.pln.pt/'

def tokenizer(text, sentence=0):
    opts = 'sentence='+str(sentence)
    return _proc('tokenizer', opts, text)

def tagger(text, ner=0):
    opts = 'ner='+str(ner)
    return _proc('tagger', opts, text)

def dep_parser(text):
    opts = ''
    return _proc('dep_parser', opts, text)

def tf(text):
    opts = ''
    return _proc('tf', opts, text)

def stopwords():
    opts = ''
    return _proc('stopwords', opts, None)

def _proc(action, opts, text):
    url = API + action + '?' + opts
    data = None
    if (text):
        data = text.encode('utf8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        p = response.read()
    return json.loads(p)

