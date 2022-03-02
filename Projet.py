class Node:

    def __init__(self, leaf=True):
        # self.parent = parent
        self.leaf = leaf
        self.keyArray = []  # Current number of keys
        self.tabNodeChildrens = []

    def insert(self, key):
        if self.keyArray:
            if key < self.keyArray[0]:
                self.keyArray.insert(0, key)
            index = 0
            for val in self.keyArray:
                print("val:", val)
                if val < key:
                    index += 1
                if index == len(self.keyArray):
                    print("avant ajout de ", key, ":", self.keyArray)
                    self.keyArray.insert(index, key)
                    print("apres ajout de ", key, ":", self.keyArray)
                    break
        else:
            self.keyArray.append(key)

        # si on a un seul element pour (L,U) = (2,3)
        # alors la valeur retournée sera un tableau vide et que donc la valeur sera ajoutée directement au noeud.
        # au cas contraire, la fonction insert de l'arbre fera le traitement necessaire sur les autres noeuds pour ajouter la valeur.
        length = len(self.keyArray)
        middle_index = length // 2
        second_half = self.keyArray[middle_index:]
        return second_half


class Tree:
    def __init__(self, L, U):
        self.nbChildMin = L - 1
        self.nbChildMax = U - 1
        self.root = Node(True)
        self.nodes = []

    def print_tree(self, node, l=0):
        print("Level ", l, " ", len(node.keyArray), end=":")
        for i in node.keyArray:
            print(i, end=" ")
        print()
        l += 1
        if len(node.tabNodeChildrens) > 0:
            for i in node.tabNodeChildrens:
                self.print_tree(i, l)

    def insert(self, key):
        print("-----------------------------")
        print("pour l'ajout de :", key)
        result = self.root.insert(key)
        print("result", result)
        if len(result) > 1:
            print("RESULT EST PLUS GRAND QUE 1 : TRAITEMENT DU TABLEAU ET CREATION DE NOUVEAUX NOEUDS.")
            # on cree le nouveau noeud parent et on lui attribue la valeur
            newNode = Node(False)
            newNode.keyArray.append(result[0])
            length = len(result) // 2
            # on cree les 2 noeuds enfants
            child = Node()
            child2 = Node()
            child.keyArray = self.root.keyArray[:length]
            child2.keyArray = self.root.keyArray[length + 1:]
            newNode.tabNodeChildrens.append(child)
            newNode.tabNodeChildrens.append(child2)
            self.root = newNode

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

    # TODO optimiser avec tabNodeChildren et non nodes


def main():
    B = Tree(2, 3)

    N = Node()
    N.keyArray = [2, 6]

    N1 = Node()
    N1.keyArray = [1, 3]

    N2 = Node()
    N2.keyArray = [5, 7, 10]

    N.tabNodeChildrens = [N1, N2]
    B.nodes.append(N)
    B.nodes.append(N1)
    B.nodes.append(N2)

    B.root = N

    # B.print_tree(B.root)
    # PARCOURS D'ARBRE : OK

    # print(B.recherche(10))
    # RECHERCHE : OK

    tree = Tree(2, 3)
    tree.insert(1)
    print("noeud racine apres ajout de 1 :", tree.root.keyArray)
    tree.insert(2)
    print("noeud racine apres ajout de 2 :", tree.root.keyArray)
    tree.insert(3)
    print("noeud racine apres ajout de 3 :", tree.root.keyArray)
    tree.insert(4)
    tree.print_tree(tree.root)

if __name__ == '__main__':
    main()
