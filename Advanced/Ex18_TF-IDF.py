import math
import numpy as np

text = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''

def distance(row1, row2):
    diff = 0
    for ro1, ro2 in zip(row1, row2):
        diff += abs(ro1 - ro2)
    return diff

def find_nearest_pair(data):
    N = len(data)
    dist = np.empty((N, N), dtype=np.float64)
    for i, datai in enumerate(data):
        for j, dataj in enumerate(data):
            if (i == j):
                dist[i][j] = np.inf
            else:
                dist[i][j] = distance(datai, dataj)      
    print(np.unravel_index(np.argmin(dist),dist.shape))

    print(dist)

def main(text):
    # tasks your code should perform:

    # 1. split the text into words, and get a list of unique words that appear in it
    # a short one-liner to separate the text into sentences (with words lower-cased to make words equal 
    # despite casing) can be done with 
    docs = [line.lower().split() for line in text.split('\n')]
    N = len(docs)

    vocabulary = list(set(text.lower().split()))
    tf = {}
    df = {}

    # 2. go over each unique word and calculate its term frequency, and its document frequency
    for word in vocabulary:
        tf[word] = [doc.count(word)/len(doc) for doc in docs]
        df[word] = sum([word in doc for doc in docs])/N
    
    # 3. after you have your term frequencies and document frequencies, go over each line in the text and 
    # calculate its TF-IDF representation, which will be a vector
    data = []
    for doc_index, doc in enumerate(docs):
        tfidf = []
        for word in vocabulary:
            tfidf.append(tf[word][doc_index] * math.log(1/df[word],10))
        data.append(tfidf)    

    find_nearest_pair(data) 
    
    # 4. after you have calculated the TF-IDF representations for each line in the text, you need to
    # calculate the distances between each line to find which are the closest.
    

main(text)
