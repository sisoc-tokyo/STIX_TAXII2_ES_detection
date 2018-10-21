from stix2 import CustomObject, properties, TAXIICollectionSource
from taxii2client import Collection
from stix2 import Filter
import sys
import os


def polling(poll_url):
    # poll
    collection = Collection(poll_url, 'user1', 'Password1')
    tc_source = TAXIICollectionSource(collection)

    f1 = Filter("type", "=", "indicator")
    indicators = tc_source.query([f1])
    n = 0
    for indicator in indicators:
        print(indicator)
        filewrite(indicator, n)
        n += 1


def filewrite(indicator, n):
    f = open('taxiidata.json', 'a')
    if n != 0:
        f.write(',')
    f.write(str(indicator))


def add_brackets_top():
    f = open('taxiidata.json', 'a')
    f.write('{"objects": [')


def add_brackets_bottom():
    f = open('taxiidata.json', 'a')
    f.write(']}')
    f.close()


if __name__ == '__main__':
    currentpath = os.path.dirname(os.path.abspath(__file__))
    filepath = currentpath + '/taxiidata.json'
    if os.path.exists(filepath):
        os.remove(filepath)

    add_brackets_top()
    polling(sys.argv[1])
    add_brackets_bottom()