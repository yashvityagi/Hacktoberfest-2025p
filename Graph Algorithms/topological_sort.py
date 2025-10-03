from collections import defaultdict, deque

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_sort(self):
        # Step 1: Compute in-degree of all vertices
        in_degree = [0] * self.V
        for u in self.graph:
            for v in self.graph[u]:
                in_degree[v] += 1

        # Step 2: Enqueue all vertices with in-degree 0
        queue = deque([i for i in range(self.V) if in_degree[i] == 0])
        topo_order = []

        # Step 3: Process nodes
        while queue:
            u = queue.popleft()
            topo_order.append(u)

            # Reduce in-degree of neighbors
            for v in self.graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

        # Step 4: Check for cycle
        if len(topo_order) != self.V:
            print("Cycle detected in the graph!")
            return None
        else:
            return topo_order


# ---------------- Mock Example ----------------
if __name__ == "__main__":
    # Example 1: Acyclic Graph (DAG)
    g1 = Graph(6)
    g1.add_edge(5, 2)
    g1.add_edge(5, 0)
    g1.add_edge(4, 0)
    g1.add_edge(4, 1)
    g1.add_edge(2, 3)
    g1.add_edge(3, 1)

    print("Topological Sort of g1:")
    print(g1.topological_sort())  # Valid order

    # Example 2: Graph with Cycle
    g2 = Graph(4)
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)
    g2.add_edge(2, 3)
    g2.add_edge(3, 1)  # introduces cycle

    print("\nTopological Sort of g2:")
    print(g2.topological_sort())  # Will detect cycle
