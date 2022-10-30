def prims_mst(self):
    # Defining a really big number, that'll always be the highest weight in comparisons
    postitive_inf = float('inf')

    # This is a list showing which nodes are already selected
    # so we don't pick the same node twice and we can actually know when stop looking
    selected_nodes = [False for node in range(self.m_num_of_nodes)]

    # Matrix of the resulting MST
    result = [[0 for column in range(self.m_num_of_nodes)]
              for row in range(self.m_num_of_nodes)]

    indx = 0
    for i in range(self.m_num_of_nodes):
        print(self.m_graph[i])

    print(selected_nodes)

    # While there are nodes that are not included in the MST, keep looking:
    while (False in selected_nodes):
        # We use the big number we created before as the possible minimum weight
        minimum = postitive_inf

        # The starting node
        start = 0

        # The ending node
        end = 0

        for i in range(self.m_num_of_nodes):
            # If the node is part of the MST, look its relationships
            if selected_nodes[i]:
                for j in range(self.m_num_of_nodes):
                    # If the analyzed node have a path to the ending node AND its not included in the MST (to avoid cycles)
                    if (not selected_nodes[j] and self.m_graph[i][j] > 0):
                        # If the weight path analized is less than the minimum of the MST
                        if self.m_graph[i][j] < minimum:
                            # Defines the new minimum weight, the starting vertex and the ending vertex
                            minimum = self.m_graph[i][j]
                            start, end = i, j

        # Since we added the ending vertex to the MST, it's already selected:
        selected_nodes[end] = True

        # Filling the MST Adjacency Matrix fields:
        result[start][end] = minimum

        if minimum == postitive_inf:
            result[start][end] = 0

        print("(%d.) %d - %d: %d" % (indx, start, end, result[start][end]))
        indx += 1

        result[end][start] = result[start][end]

    # Print the resulting MST
    # for node1, node2, weight in result:
    for i in range(len(result)):
        for j in range(0 + i, len(result)):
            if result[i][j] != 0:
                print("%d - %d: %d" % (i, j, result[i][j]))