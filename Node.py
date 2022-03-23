class Node:
    def __init__(self, parent=None, leaf=True):
        self.parent = parent
        self.leaf = leaf
        self.keys = []  # Current number of keys
        self.childrens = []

    def toString(self):
        if self.parent is None:
            print("parent node :", self.parent)
        else:
            print("keys of parent node :", self.parent.keys)
        print("leaf:",self.leaf)
        print("keys:",self.keys)
        childs = []
        for child in self.childrens:
            childs.append(child.keys)
        print("key of childrens :", childs)

    def keyIndex(self, key):
        i = 0
        for elem in self.keys:
            if key > elem:
                i += 1
            else:
                break
        return i
    def insert(self, key):
        i = self.keyIndex(key)
        if not self.leaf:
            print("on va au fils contenant les clés", self.childrens[i].keys)
            node = self.childrens[i].insert(key)
            return node
        else:
            print("ajout de", key, "au noeud contenant déjà les clés", self.keys)
            self.keys.insert(i, key)
            return self