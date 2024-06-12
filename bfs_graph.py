#Python program to print BFS traversal
#from a given source vertex. BFS(int s)
#traverses vertices reachable from s.

from collections import defaultdict


#This class represents a directed graph
#using adjacency list representation
class Graph:

    def __init__(self):

        #default dictionary to store graph
        self.graph=defaultdict(list)

   #function to add edge to graph     
    def AddEdge(self,u,v):
        self.graph[u].append(v)
        
    #function to print a BFS of graph
    def BFS(self,s):

        #mark all vertices as not visited
        visited=[False] * (max(self.graph) + 1)

        #create queue for BFS
        queue=[]

        #Mark the source node as
        #visited and enqueue it
        queue.append(s)
        visited[s] =True

        while queue:


            #Dequeue a vertex
            #from queue and print it
            s=queue.pop(0)
            print(s,end=" ")


        #Get all adjacent vertices of the
        #dequeue vertex s.If an adjacent has
        #not been visited, then mark it
        #visited and enqueue it
        for i in self.graph[s]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
                
#Driver code

g = Graph()
g.AddEdge(0,1)
g.AddEdge(0,2)
g.AddEdge(1,2)
g.AddEdge(2,0)
g.AddEdge(2,3)
g.AddEdge(3,3)

print("the following is Breadth First traversal"
      "(starting from vertex 2)")

g.BFS(2)


        
