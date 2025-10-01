from sumy.utils import get_stop_words
from sumy.nlp.stemmers import Stemmer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.plaintext import PlaintextParser
from flask import Flask, redirect, url_for, render_template, request
from newsdataapi import NewsDataApiClient
import nltk
nltk.download('punkt')



app = Flask(__name__)

LANGUAGE = "english"
SENTENCES_COUNT = 2

def summarize_text(text):
    parser = PlaintextParser.from_string(text, Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)
    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)
    return ' '.join([str(sentence) for sentence in summarizer(parser.document, SENTENCES_COUNT)])


@app.route('/')
def welcome():
    api = NewsDataApiClient(apikey="pub_33882765e67619d7f5b7f6b138c13d32cf8a5")
    response = api.news_api( country='us')
    arr = [["" for x in range(3)] for y in range(10)]
    for x in range(10):
        if response['results'][x]['language'] == 'english':
            content = response['results'][x]['content']
            a = summarize_text(content)
            arr[x][0] = response['results'][x]['title']
            arr[x][1] = a
            
            arr[x][2] = response['results'][x]['link']
        else:
            x = x-1
    return render_template('demo.html', result=arr)


@app.route('/home', methods=['POST'])
def home():
    api = NewsDataApiClient(apikey="pub_33882765e67619d7f5b7f6b138c13d32cf8a5")
    response = api.news_api( country='us')

    arr = [["" for x in range(3)] for y in range(10)]
    for x in range(10):
        content = response['results'][x]['content']
        a = summarize_text(content)
        arr[x][0] = response['results'][x]['title']
        arr[x][1] = a
        arr[x][2] = response['results'][x]['link']
        
    return render_template('demo.html', result=arr)


@app.route('/search', methods=['POST', 'GET'])
def search():
    search = request.form['search']
    api = NewsDataApiClient(apikey="pub_33882765e67619d7f5b7f6b138c13d32cf8a5")
    response = api.news_api( q=search, language="en")

    arr = [["" for x in range(3)] for y in range(10)]
    for x in range(10):
        content = response['results'][x]['content']
        a = summarize_text(content)
        arr[x][0] = response['results'][x]['title']
        arr[x][1] = a
        if len(a) == 0:
            arr[x][1] = response['results'][x]['description']
        arr[x][2] = response['results'][x]['link']
    return render_template('demo.html', result=arr)


@app.route('/business', methods=['POST'])
def business():
    api = NewsDataApiClient(apikey="pub_33882765e67619d7f5b7f6b138c13d32cf8a5")
    response = api.news_api(category="business", language="en")
    arr = [["" for x in range(3)] for y in range(10)]
    for x in range(10): 
        content = response['results'][x]['content']
        a = summarize_text(content)
        arr[x][0] = response['results'][x]['title']
        arr[x][1] = a
        arr[x][2] = response['results'][x]['link']    
    return render_template('demo.html', result=arr)


@app.route('/politics', methods=['POST'])
def politics():
    api = NewsDataApiClient(apikey="pub_33882765e67619d7f5b7f6b138c13d32cf8a5")
    response = api.news_api(category="politics", language="en", country='us')
    arr = [["" for x in range(3)] for y in range(10)]
    for x in range(10):
        content = response['results'][x]['content']
        a = summarize_text(content)
        arr[x][0] = response['results'][x]['title']
        arr[x][1] = a
        arr[x][2] = response['results'][x]['link']
    return render_template('demo.html', result=arr)


@app.route('/technology',  methods=['POST'])
def technology():
    api = NewsDataApiClient(apikey="pub_33882765e67619d7f5b7f6b138c13d32cf8a5")
    response = api.news_api(category="technology", language="en", country='us')
    arr = [["" for x in range(3)] for y in range(10)]
    for x in range(10):
        content = response['results'][x]['content']
        a = summarize_text(content)
        arr[x][0] = response['results'][x]['title']
        arr[x][1] = a
        arr[x][2] = response['results'][x]['link']    
    return render_template('demo.html', result=arr)


@app.route('/sports', methods=['POST'])
def sports():
    api = NewsDataApiClient(apikey="pub_33882765e67619d7f5b7f6b138c13d32cf8a5")
    response = api.news_api(category="sports", language="en")
    arr = [["" for x in range(3)] for y in range(10)]
    for x in range(10):
        content = response['results'][x]['content']
        a = summarize_text(content)
        arr[x][0] = response['results'][x]['title']
        arr[x][1] = a
        arr[x][2] = response['results'][x]['link']
    return render_template('demo.html', result=arr)

@app.route('/entertainment', methods=['POST'])
def entertainment():
    api = NewsDataApiClient(apikey="pub_33882765e67619d7f5b7f6b138c13d32cf8a5")
    response = api.news_api(category="entertainment",   language="en", country='us')
    arr = [["" for x in range(3)] for y in range(10)]
    for x in range(10):
        content = response['results'][x]['content']
        a = summarize_text(content)
        arr[x][0] = response['results'][x]['title']
        arr[x][1] = a
        arr[x][2] = response['results'][x]['link']
    return render_template('demo.html', result=arr)

@app.route('/world', methods=['POST'])
def world():
    api = NewsDataApiClient(apikey="pub_33882765e67619d7f5b7f6b138c13d32cf8a5")
    response = api.news_api(category="world",   language="en", country='us')
    arr = [["" for x in range(3)] for y in range(10)]
    for x in range(10):
        content = response['results'][x]['content']
        a = summarize_text(content)
        arr[x][0] = response['results'][x]['title']
        arr[x][1] = a
        arr[x][2] = response['results'][x]['link']
    return render_template('demo.html', result=arr)


if __name__ == '__main__':
    app.run(debug=True)
