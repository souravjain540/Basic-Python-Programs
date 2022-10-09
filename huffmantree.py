Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from heapq import heapify as hpf
from heapq import heappop as hpp
from heapq import heappush as hppu
class Node:
    def __init(self,ch,freq,left=None,right=None):
        self.ch,self.freq=ch,freq
        self.left,self.right=left,right
    def __lt__(self,other):
        return self.freq<other.freq

def getHuffmanTree(txt):
    if len(txt)==0:
        return
    freq={ch:text.count(ch) for k,v in set(txt)}
    pq=[Node(k,v) for k,v in freq.items()]
    hpf(pq)
    while len(pq)>1:
        left,right=hpp(pq),hpp(pq);
        newFreq=left.freq+right.freq
        hppu(pq,Node(None,newFreq,left,right))
    root=pq[0]
    return root

