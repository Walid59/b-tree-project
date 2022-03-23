from Node import *
import networkx as nx
import matplotlib.pyplot as plt

class Tree:
    def __init__(self, L, U):
        self.nbChildMin = L - 1
        self.nbChildMax = U - 1
        self.root = Node()
        self.nodes = []

    def toStringAllNodes(self,node):
        node.toString()
        for child in node.childrens:
            print("--------------------------------------------------------")
            self.toStringAllNodes(child)

    def print_tree(self, node, l=0):
        print("Level ", l, " ", len(node.keys), end=":")
        for i in node.keys:
            print(i, end=" ")
        print()
        l += 1
        if len(node.childrens) > 0:
            for i in node.childrens:
                self.print_tree(i, l)

    def insertKeys(self,keys):
        for key in keys:
            self.insert(key)
            self.print_tree(self.root)
            print("-------------------------------------------------")

    def insert(self, key):
        node = self.root.insert(key)
        if len(node.keys) > self.nbChildMax:
            self.split(node)

    def split(self, node):
        print("Traitement du noeud contenant une valeur en trop:", node.keys)
        length = len(node.keys)

        if length % 2 == 0:
            valueToMove = node.keys[length // 2 - 1]
        else:
            valueToMove = node.keys[length // 2]
        node.keys.remove(valueToMove)

        length = len(node.keys)
        if node.parent is not None:
            newNode = Node(node.parent, node.leaf)
            newNode.keys = node.keys[length // 2:]
            node.keys = node.keys[:length // 2]

            print("noeud gauche", node.keys)
            print("nouveau noeud droit", newNode.keys)

            i = node.parent.keyIndex(valueToMove)
            print(node.parent.keys)
            node.parent.keys.insert(i, valueToMove)
            print(node.parent.keys)
            node.parent.childrens.append(newNode)

            if len(node.parent.keys) > self.nbChildMax:
                self.split(node.parent)
        else:
            nLeft = Node(node, node.leaf)
            nRight = Node(node, node.leaf)

            if node.leaf:
                node.leaf = False

            nLeft.keys = node.keys[:length // 2]
            nRight.keys = node.keys[length // 2:]
            nLeft.childrens = node.childrens[:len(node.childrens) // 2]
            nRight.childrens = node.childrens[len(node.childrens) // 2:]
            for child in node.childrens[:len(node.childrens) // 2]:
                child.parent = nLeft

            for child in node.childrens[len(node.childrens) // 2:]:
                child.parent = nRight

            node.childrens = [nLeft, nRight]
            node.keys.clear()
            node.keys.append(valueToMove)

    def search_key(self, v):
        for node in self.nodes:
            keys = node.keyArray
            a = 0
            b = len(keys) - 1
            while a <= b:
                m = (a + b) // 2
                if keys[m] == v:
                    return True
                elif keys[m] < v:
                    a = m + 1
                else:
                    b = m - 1
        return False

    def initNode(self, G, node):
        keys = str(node.keys)
        for elem in node.childrens:
            keys2 = str(elem.keys)
            G.add_edge(keys, keys2)
            self.initNode(G,elem)


    def graph(self):
        G = nx.Graph()
        self.initNode(G, self.root)

        nx.draw(G, with_labels=True)
        plt.show()
    # TODO optimiser avec childrens et non nodes
