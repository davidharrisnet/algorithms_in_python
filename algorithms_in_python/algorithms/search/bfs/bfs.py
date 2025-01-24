from collections import deque

def bfs(graph, start):
    """
    Perform a breadth-first search on a graph.

    Args:
        graph: A dictionary representing the graph as {node: [neighbors]}.
        start: The starting node for the search.

    Returns:
        A list of nodes in the order they were visited.
    """

    visited = set()  # Set to track visited nodes
    queue = deque([start])  # Queue for BFS traversal
    result = []  # List to store the order of visited nodes

    while queue:
        node = queue.popleft()  # Dequeue the next node

        if node not in visited:
            visited.add(node)
            result.append(node)

            # Enqueue unvisited neighbors
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return result

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print(bfs(graph, 'A'))  # Output: ['A', 'B', 'C', 'D', 'E', 'F']