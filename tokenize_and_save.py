import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

import redis

import glob

r = redis.Redis(
    host='localhost',
    port=6379,
)

stop_words = set(stopwords.words('english'))

txt_files = glob.glob("*.txt")

for file in txt_files:
    with open(file, 'r') as doc:
        data = doc.read()

    tokens = word_tokenize(data)

    words = set()

    for word in tokens:
        if word not in stop_words:
            words.add(word)

    pipeline = r.pipeline(True)

    for word in words:
        pipeline.sadd(word, file)

    print(len(pipeline.execute()))
