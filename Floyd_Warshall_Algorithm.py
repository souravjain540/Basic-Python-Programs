class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = [[float('inf')] * num_vertices for _ in range(num_vertices)]
        for i in range(num_vertices):
            self.graph[i][i] = 0

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight  # Symmetric for undirected graph

    def floyd_warshall(self):
        dist = self.graph

        for k in range(self.num_vertices):
            for i in range(self.num_vertices):
                for j in range(self.num_vertices):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        return dist

# Example usage:
if __name__ == "__main__":
    graph = Graph(4)
    graph.add_edge(0, 1, 5)
    graph.add_edge(0, 2, 9)
    graph.add_edge(0, 3, 4)
    graph.add_edge(1, 2, 2)
    graph.add_edge(2, 3, 3)

    # Run Floyd-Warshall algorithm
    result = graph.floyd_warshall()

    print("Shortest distances between every pair of vertices:")
    for row in result:
        print(row)
