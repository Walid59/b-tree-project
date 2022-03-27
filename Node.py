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
        print("leaf:", self.leaf)
        print("keys:", self.keys)
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

    def insert(self, key, tree):
        i = self.keyIndex(key)
        if not self.leaf:
            print("on va au fils contenant les clés", self.childrens[i].keys)
            bool = self.childrens[i].insert(key, tree)
            if bool:
                tree.split(self.childrens[i])
                return len(self.keys) > tree.nbChildMax

            else:
                return False
        else:
            print("ajout de", key, "au noeud contenant déjà les clés", self.keys)
            self.keys.insert(i, key)
            return len(self.keys) > tree.nbChildMax

    def exists_key(self, searching_key):
        i = 0
        while i < len(self.keys) and searching_key > self.keys[i]:
            i += 1

        if self.leaf:
            return i < len(self.keys) and searching_key == self.keys[i]

        else:
            if i == len(self.keys):
                self.childrens[-1].exists_key(searching_key)

            elif self.keys[i] == searching_key:
                return True

            return self.childrens[i].exists_key(searching_key)