#BFS
n = int(input("Enter the number of nodes : "))
graph = {};
for i in range(n):
    temp = list(map(str, input().split()))
    if len(temp) > 1:
        graph[temp[0]] = temp[1:]
    else:
        graph[temp[0]] = []
        
visited = set();
queue = [];

def bfs(visited, graph, node):
    visited.add(node)
    queue.append(node)
    
    while queue:
        s = queue.pop(0)
        print(s, end = ' ')
        
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
            
source = str(input("Enter the source node : "))
print("Following BFS is : ")
bfs(visited, graph, source)