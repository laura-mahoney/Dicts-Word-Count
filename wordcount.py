# put your code here.
# file_name = open("twain.txt")

import sys
file_name = open(sys.argv[1])

word_count = {}
import string

for line in file_name:  # loops through file based on line
    line = line.rstrip()  # removes whitespace at end of line
    words = line.split(" ")  # splits each line based on word
    for word in words:
        word = word.lower()
        word = word.strip(string.punctuation)
        word_count[word] = word_count.get(word, 0) + 1  # assigning word as key, incrementing value if word already in dictionary


for word, value in word_count.iteritems():
    print word, value
