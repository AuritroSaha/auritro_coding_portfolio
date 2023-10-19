class Node:
    def __init__(self, key):
        self.key = key
        self.neighbors = []

    def __str__(self):
        return "ID: " + str(self.key) + "\nNeighbors: " + str(self.neighbors) + "\n\n"

    def add_neighbor(self, node):
        self.neighbors.append(node)


node1 = Node("a")

# node1.add_neighbor("b")
# node1.add_neighbor("c")
# node1.add_neighbor("d")

node2 = Node("b")
node3 = Node("c")
node4 = Node("d")


class Graph:
    def __init__(self):
        self.graph = {}

    def __str__(self):
        nodes = ""
        for i in self.graph:
            nodes += str(self.graph[i])

        return "Graph 1:\n\n" + nodes

    def add_node(self, node, key):
        self.graph[key] = node

    def add_edge(self, node1, node2):
        node1.add_neighbor(node2.key)
        node2.add_neighbor(node1.key)


graph1 = Graph()

graph1.add_node(node1, node1.key)
graph1.add_node(node2, node2.key)
graph1.add_node(node3, node3.key)
graph1.add_node(node4, node4.key)

graph1.add_edge(node1, node2)
graph1.add_edge(node2, node3)
graph1.add_edge(node3, node4)
graph1.add_edge(node4, node1)

print(graph1)









