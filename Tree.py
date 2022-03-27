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
        bool = self.root.insert(key, self)
        if bool:
            self.split(self.root)

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
            newNode.keys = node.keys[length // 2:] #partie droite
            node.keys = node.keys[:length // 2] #partie gauche

            newNode.childrens = node.childrens[len(node.childrens) // 2:]
            for child in newNode.childrens:
                child.parent = newNode

            node.childrens = node.childrens[:len(node.childrens) // 2]

            i = node.parent.keyIndex(valueToMove)
            node.parent.keys.insert(i, valueToMove)

            i = 0
            for child in node.parent.childrens:
                if child.keys[-1] < newNode.keys[-1]:
                    i += 1
            node.parent.childrens.insert(i, newNode)

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

    def exists_key(self,key):
       return self.root.exists_key(key)

    def initNode(self, G, node):
        keys = str(node.keys)
        for elem in node.childrens:
            keys2 = str(elem.keys)
            G.add_edge(keys, keys2)
            self.initNode(G,elem)


    def toGraph(self):
        G = nx.Graph()
        self.initNode(G, self.root)
        pos = nx.spring_layout(G, k=0.1, iterations=100)
        nx.draw(G, with_labels=True, pos=pos)
        plt.show()
