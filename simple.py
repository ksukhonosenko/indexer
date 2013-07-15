# -*- coding: utf-8 -*-

__author__ = 'apple'

import glob
import string


class NumFilter:
    def filter(self, word):
        if word is None:
            return None

        try:
            float(word)
            return None
        except ValueError:
            return word


class StopWords:
    def __init__(self):
        self.stops = set()

        with open("./cfg/stops.txt") as f:
            for line in f:
                self.stops.add(line.strip())

            f.close()

    def filter(self, word):
        if word in self.stops:
            return None
        else:
            return word


class SynMap:
    def __init__(self):
        self.map = {}
        # line = root_word <blank> list_of_blank_separated_synonyms
        with open("./cfg/themes.txt") as f:
            for line in f:
                line = line.strip()
                if len(line) == 0:
                    continue

                words = line.split()
                root = words[0]
                words = words[1:]
                for w in words:
                    self.map[w] = root

                self.map[root] = root  # add self-case

            f.close()

    def findRoot(self, word):
        if word is None:
            return None

        # try find matching syn and its corresponding root
        for syn in self.map.keys():
            if word.find(syn) == 0:  # partial matching from beginning
                return self.map[syn]  # return root

        return None


freq_map = {}
index = {}
inverted_freq = {}
sm = SynMap()
stop = StopWords()
num = NumFilter()
issue_count = 0 # detect by IM-CL-

# read file content in  each file in specified directory
file_list = glob.glob("./data/*.txt")
for file_name in file_list:
    print "Processing file %s ..." % file_name

    with open(file_name) as f:
        for line in f:

            # tokenize
            word_list = string.split(line)
            for w in word_list:
                token = w.strip('.<>,:%$!@#$%^&*()_+=-')

                token = string.lower(token)

                if token.find("im-cl-") == 0:
                    issue_count += 1

                # check token against synonym map (filter out stop words)
                token = stop.filter(token)
                token = num.filter(token)
                token = sm.findRoot(token)
                if token is None:
                    continue  # skip this word

                # build freq map
                if token not in freq_map:
                    freq_map[token] = 1
                else:
                    freq_map[token] += 1

                # build index word - > unique file names
                if not index.has_key(token):
                    index[token] = set()

                index[token].add(file_name)

        f.close()

for tk in freq_map.keys():
    count = freq_map[tk]
    if not inverted_freq.has_key(count):
        inverted_freq[count] = set()
    inverted_freq[count].add(tk)

sorted_counts = inverted_freq.keys()
sorted_counts.sort(reverse=True)

# get total word count and set buzz-word limit (words counted more than that will be ignored)
total = sum(sorted_counts)
buzz_limit = total / 100

# print top themes with corresponding source urls
for cnt in sorted_counts:
    #if cnt > 100000:
    #    continue   # ignore hi freq words

    #if cnt < 1:
    #    continue   # ignore low freq words

    for w in inverted_freq[cnt]:
        print "%s : %d" % (w, cnt)
        #print w

        # print source urls
        #for url in index[w]:
        #    print "-> %s" % (url)

print "Total issue count: %d" % (issue_count)