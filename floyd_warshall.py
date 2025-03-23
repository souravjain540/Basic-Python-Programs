class Solution:
    def __init__(self,graph,n):
        self.graph=graph
        self.n=n
    def floydWarshall(self,graph):
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    if self.graph[i][j]>self.graph[i][k]+self.graph[j][k]:
                        self.graph[i][j]=self.graph[i][k]+self.graph[j][k]
        return self.graph


n=int(input())
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))
obj=Solution(graph,n)
print(obj.floydWarshall(graph))