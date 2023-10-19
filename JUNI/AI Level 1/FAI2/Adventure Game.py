class Node:
    def __init__(self, key, q):
        self.key = key
        self.neighbors = []
        self.q = q

    def __str__(self):
        return "ID: " + str(self.key) + "\nNeighbors: " + str(self.neighbors) + "\n\n"

    def add_neighbor(self, node):
        self.neighbors.append(node)


node1 = Node("start", "Yourself in an abandoned theme park. Do you want to *leave* or *explore*\n")
node2 = Node("explore", "You around until you hear a scary noise. Do you *run away* or *check it out*\n")
node3 = Node("leave", "You decide leave and go home.\n")
node4 = Node("check it out", "You decide to go see what the noise is. You die just because. Shoulda left.\n")
node5 = Node("run away", "You decide to run away but get hit by a truck.\n")


class Graph:
    def __init__(self):
        self.graph = {}

    def __str__(self):
        nodes = ""
        for i in self.graph:
            nodes += str(self.graph[i])

        return "Graph 1:\n\n" + nodes

    def add_node(self, node):
        self.graph[node.key] = node

    def add_edge(self, node1, node2):
        node1.add_neighbor(node2.key)

    # def start_adventure(self, node):
        # while True:
        #   print(node1.q)
        #   choice = input()
        #   while True:
        #     if choice != "leave" or choice != "explore":
        #       print("Pick an option\n")
        #       choice = input()
        #     else:
        #       break
        #   print(self.graph[choice])
        #   if len(self.graph[choice].neighbors) == 0:
        #     break
        #   choice = input()
        #   while True:
        #     if choice != "run away" or choice != "check it out":
        #       print("Pick an option\n")
        #     else:
        #       break
        #   print(self.graph[choice])

# this needs to be fixed - broke during transfer to pycharm
        # while node.nei
        #     choice = ""
        #     choice = "hello"
        #     while choice not in self.graph:
        #         choice = input()
        #     node = self.graph[choice]
        #     print(node.q)


graph1 = Graph()

graph1.add_node(node1)
graph1.add_node(node2)
graph1.add_node(node3)
graph1.add_node(node4)
graph1.add_node(node5)

graph1.add_edge(node1, node2)
graph1.add_edge(node1, node3)
graph1.add_edge(node2, node4)
graph1.add_edge(node2, node5)

graph1.start_adventure(node1)


