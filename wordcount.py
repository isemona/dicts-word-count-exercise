# put your code here.
import sys

filename = sys.argv[1]
word_count = {}
for line in open(filename):
    for word in line.split():
        if word[-1] in ['.', '?', ',']:
            word = word[:-1]
        word_count[word.title()] = word_count.get(word.title(),0) + 1

for key,value in word_count.items():
    print(key,value)


