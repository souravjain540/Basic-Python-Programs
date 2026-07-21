from heapq import heapify as hpf
from heapq import heappop as hpp
from heapq import heappush as hppu
class Node:
    def __init__(self,ch,freq,left=None,right=None):
        self.ch,self.freq=ch,freq
        self.left,self.right=left,right
    def __lt__(self,other):
        return self.freq<other.freq

def getHuffmanTree(txt):
    if len(txt)==0:
        return
    freq={ch:txt.count(ch) for ch in set(txt)}
    pq=[Node(k,v) for k,v in freq.items()]
    hpf(pq)
    while len(pq)>1:
        left,right=hpp(pq),hpp(pq);
        newFreq=left.freq+right.freq
        hppu(pq,Node(None,newFreq,left,right))
    root=pq[0]
    return root

def printCodes(node, code=""):
    if node is None:
        return
        
    # If this is a leaf node, it contains a character (internal nodes are created with None)
    if node.ch is not None:
        print(f"'{node.ch}' : {code}")
        
    # Traverse left (add 0 to code)
    printCodes(node.left, code + "0")
    # Traverse right (add 1 to code)
    printCodes(node.right, code + "1")

if __name__ == "__main__":
    text = "hello huffman"
    print(f"Building Huffman Tree for text: '{text}'")
    root_node = getHuffmanTree(text)
    
    if root_node:
        print("Huffman Codes:")
        printCodes(root_node)

