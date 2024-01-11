# -*- coding: utf-8 -*-


import json
# if you are using python 3, you should 
import urllib.request 
import requests
# import urllib2


# change the url according to your own corename and query
# inurl = "http://localhost:8983/solr/bm25/query?q=&q.op=OR&fl=id,score&rows=20&wt=json"
inurl = 'http://localhost:8983/solr/bm25/select?q=text_en:%20"Syrian%20civil%20war"%5E4%20or%20text_de:%20("Bürgerkrieg%20Syrien"~5)%5E3%20or%20text_ru:%20(Сирийская%20гражданская%20война)%20or%20text_en:%20(Syria%20war)%5E2%20%20or%20text_de:%20Syrien&fl=id%2Cscore&wt=json&indent=true&rows=20'
outfn = '2.txt'


# change query id and IRModel name accordingly
qid = '002'
IRModel='bm25' #either bm25 or vsm
outf = open(outfn, 'a+')
# data = urllib2.urlopen(inurl)
# if you're using python 3, you should use
data = requests.get(inurl).json()
# data = urllib.request.urlopen(inurl)

docs = data['response']['docs']
# docs = json.load(data)['response']['docs']
# the ranking should start from 1 and increase
rank = 1
for doc in docs:
    outf.write(qid + ' ' + 'Q0' + ' ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(doc['score']) + ' ' + IRModel + '\n')
    rank += 1
outf.close()
