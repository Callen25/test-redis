import sys
import redis
from nltk.tokenize import word_tokenize


r = redis.Redis(host='localhost', port=6379)

def search(query):
    tokens = word_tokenize(query)
    results = r.sinter(tokens)
    return results


if __name__ == '__main__':
    query = sys.argv[1]
    print(search(query))
