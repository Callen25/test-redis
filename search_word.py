import sys
import redis
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


r = redis.Redis(host='localhost', port=6379)
stop_words = set(stopwords.words('english'))

def search(query):
    tokens = word_tokenize(query)
    filtered_words = []

    for word in tokens:
        if word not in stop_words:
            filtered_words.append(word)

    results1 = r.sinter(filtered_words)

    results2 = r.sunion(filtered_words) - results1

    results = list(results1) + list(results2)

    return results


if __name__ == '__main__':
    query = sys.argv[1]
    print(search(query))
