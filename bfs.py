"""
Breadth First Search (BFS) - Graph traversal algorithm
Uses queue to explore all vertices at current depth before moving to next level
Time Complexity: O(V + E) where V is vertices and E is edges
"""

from collections import deque, defaultdict


class Graph:
    """Graph class for BFS implementation"""
    
    def __init__(self):
        """Initialize graph using adjacency list"""
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        """
        Add an edge to the graph
        
        Args:
            u: Source vertex
            v: Destination vertex
        """
        self.graph[u].append(v)
    
    def bfs(self, start):
        """
        Perform BFS traversal from starting vertex
        
        Args:
            start: Starting vertex
        
        Returns:
            List of vertices in BFS order
        """
        visited = set()
        queue = deque([start])
        visited.add(start)
        result = []
        
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            
            # Visit all adjacent vertices
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return result
    
    def bfs_with_levels(self, start):
        """
        BFS that tracks level of each vertex
        
        Args:
            start: Starting vertex
        
        Returns:
            Dictionary with vertices as keys and levels as values
        """
        visited = {start: 0}
        queue = deque([start])
        
        while queue:
            vertex = queue.popleft()
            current_level = visited[vertex]
            
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited[neighbor] = current_level + 1
                    queue.append(neighbor)
        
        return visited
    
    def shortest_path(self, start, end):
        """
        Find shortest path between two vertices using BFS
        
        Args:
            start: Starting vertex
            end: Ending vertex
        
        Returns:
            List representing shortest path, or None if no path exists
        """
        if start == end:
            return [start]
        
        visited = {start}
        queue = deque([(start, [start])])
        
        while queue:
            vertex, path = queue.popleft()
            
            for neighbor in self.graph[vertex]:
                if neighbor == end:
                    return path + [neighbor]
                
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        
        return None


if __name__ == "__main__":
    print("=" * 50)
    print("BREADTH FIRST SEARCH (BFS)")
    print("=" * 50)
    
    # Create a sample graph
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    
    print("\nGraph edges:")
    for vertex, neighbors in g.graph.items():
        print(f"{vertex} -> {neighbors}")
    
    start_vertex = 2
    print(f"\nBFS starting from vertex {start_vertex}:")
    bfs_result = g.bfs(start_vertex)
    print(f"Traversal order: {bfs_result}")
    
    print(f"\nBFS with levels from vertex {start_vertex}:")
    levels = g.bfs_with_levels(start_vertex)
    for vertex, level in sorted(levels.items()):
        print(f"Vertex {vertex}: Level {level}")
    
    # Shortest path example
    print("\n" + "=" * 50)
    print("SHORTEST PATH EXAMPLE")
    print("=" * 50)
    
    g2 = Graph()
    g2.add_edge('A', 'B')
    g2.add_edge('A', 'C')
    g2.add_edge('B', 'D')
    g2.add_edge('C', 'D')
    g2.add_edge('C', 'E')
    g2.add_edge('D', 'E')
    g2.add_edge('D', 'F')
    g2.add_edge('E', 'F')
    
    start, end = 'A', 'F'
    path = g2.shortest_path(start, end)
    print(f"\nShortest path from {start} to {end}: {' -> '.join(path)}")
