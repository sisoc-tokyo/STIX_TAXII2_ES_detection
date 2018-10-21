import sys
from elasticsearch import Elasticsearch
import send_alert

es = Elasticsearch('localhost:9200')

def search_message(message):
    URL = (message.split(' ')[6])
    src = (message.split(' ')[0])

    res = es.search(index='blacklist', body={"from": 0, "size": 10000, 'query': {'match_all': {}}})
    for hit in res['hits']['hits']:
        if 'malicious_URL' in hit['_source']:
            malURL = hit['_source']['malicious_URL']
            if malURL in URL:
                send_alert.Send_alert(malURL, URL, src)
                return 'matched'
    else:
        return '-'

if __name__ == '__main__':
    result = search_message(sys.argv[1])
    print(result)