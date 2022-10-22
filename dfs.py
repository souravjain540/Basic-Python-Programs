#DFS
n = int(input("Enter the number of nodes : "))
graph = {};
for i in range(n):
    temp = list(map(str, input().split()))
    if len(temp) > 1:
        graph[temp[0]] = temp[1:]
    else:
        graph[temp[0]] = []
        
visited = set();

def dfs(visited, graph, node):
    if node not in visited:
        print(node, end = ' ')
            
        visited.add(node)
        for  neighbour in graph[node]:
            dfs(visited, graph, neighbour);

source = str(input("Enter the source node : "))
print("Following DFS is : ")
dfs(visited, graph, source)