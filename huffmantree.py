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

if __name__ == "__main__":
    text = "your text here"
    root = getHuffmanTree(text)
    # Now you can use the 'root' variable which is the root of the Huffman tree.