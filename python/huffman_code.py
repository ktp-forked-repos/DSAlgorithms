'''
Created on May 17, 2015

@author: tekrei
Generate HUFFMAN code
Source: http://rosettacode.org/wiki/Huffman_coding#Python
http://paddy3118.blogspot.com.tr/2009/03/huffman-encoding-in-python.html
'''
from heapq import heappush, heappop, heapify
from collections import defaultdict

def encode(CHAR_FREQ):
    heap = [[wt, [sym, ""]] for sym, wt in CHAR_FREQ.items()]
    heapify(heap)
    while len(heap) > 1:
        low = heappop(heap)
        high = heappop(heap)
        #put smaller to the left
        for pair in low[1:]:
            pair[1] = '0' + pair[1]
        #put higher to the right
        for pair in high[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [low[0] + high[0]] + low[1:] + high[1:])
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

if __name__ == '__main__':
    TXT = "A very beautiful huffman code generation \
            example in Python programming language"
    CHAR_FREQ = defaultdict(int)
    for char in TXT:
        CHAR_FREQ[char] += 1
    HUFFMAN = encode(CHAR_FREQ)
    print "Symbol\tWeight\tHuffman Code"
    for p in HUFFMAN:
        print "%s\t%s\t%s" % (p[0], CHAR_FREQ[p[0]], p[1])
