class Node:

    def __init__(self, taille, parent=None, feuille=False):
        self.taille = taille
        self.parent = parent
        # self.nbClesMin = L-1
        # self.nbClesMax = U-1
        self.feuille = feuille
        self.tabCles = []
        self.tabNodeChildrens = []

    def numberOfChildrens(self):
        if self.taille < len(self.tabCles):
            i = 0
            for children in self.tabNodeChildrens:
                i += 1
                i += children.numberOfChildrens()
            return i
        else:

    # self.n = n # nombre des element dans ce neoud
    # Current number of keys
    # self.n = 0

    """
    This is a javadoc style.

    @param param1: this is a first param
    @param param2: this is a second param
    @return: this is a description of what is returned
    @raise keyError: raises an exception
    """

    def insertKey(self, key):
        index = 0
        for elem in self.tabCles:
            if key > elem:
                index += 1
            else:
                break
        self.tabCles.insert(index, key)

    def ajoutCles(self, nbCles):
        listevaleurs = [i for i in range(nbCles)]
        for i in listevaleurs:
            self.tabCles.append(i)
            # TODO

    # juste pour verification
    def ajoutFils(self, arbre1, arbre2, arbre3):
        self.tabFils.append(arbre1)
        self.tabFils.append(arbre2)
        self.tabFils.append(arbre3)

    def verificationSiFeuille(self):
        if len(self.tabFils) == 0:
            self.feuille = True
        return self.feuille

    def presentation(self):
        None

    def ajoutFils(self, Arbre):
        self.tabFils.append(Arbre)

    def ajoutFils(self, arbre):
        self.tabFils.append(arbre)

    def gettabCles(self):
        return self.tabCles

    def getTaille(self):
        print(self)
        return self.taille

    def parcourir(self):
        i = 0
        for i in self.n:
            if self.feuille == False:
                self.tabFils[i].parcourir()
            print(self.tabCles[i])
        if self.feuille == False:
            self.tabFils[i].parcourir()


class Arbre:

    def __init__(self, L, U):
        self.nbFilsMin = L - 1
        self.nbFilsMax = U - 1
        self.root = Node(True)
        self.nodes = []
        # self.listeArbres = listeArbres
        # self.val = None
        # self.left = None
        # self.right = None

    """
    Add nodes to the tree
    @param node : the node added to the tree

    """

    def numberOfChildrens(self):
        return self.root.numberOfChildrens()

    def print_tree(self, node, l=0):
        print("Level ", l, " ", len(node.tabCles), end=":")
        for i in node.tabCles:
            print(i, end=" ")
        print()
        l += 1
        if len(node.tabNodeChildrens) > 0:
            for i in node.tabNodeChildrens:
                self.print_tree(i, l)

    def addNode(self, node):
        n = len(self.nodes)
        if n >= self.nbFilsMax:
            raise Exception('le nombre maximal des noeuds et dépassé')
        else:
            self.nodes.append(node)

    def parcourir(self):
        i = 0
        if self.root != None:
            self.root.parcourir()
            i += 1
            print(i)

    #    def search(self, cle) :
    #        if self.root == None :
    #            return None
    #        else :
    #            return self.root.search(cle)

    def search_key(self, k, node=None):
        if node is not None:
            #            for i in range(len(node.tabCles)) :
            #                if k == node.tabCles[i]:
            #                    return (node, i)
            #                elif node.feuille:
            #                    return None
            #                else :
            #                    return self.search_key(k, node.tabNodeChildrens[i])
            i = 0
            while i < len(node.tabCles) and k > node.tabCles[i]:
                i += 1
            if i < len(node.tabCles) and k == node.tabCles[i]:
                return (node, i)
            if node.feuille:
                return None
        #            else:
        #                return self.search_key(k, node.tabNodeChildrens[i])

        else:
            return self.search_key(k, self.root)

        for i in node.tabNodeChildrens:
            self.root = i
            return self.search_key(k, i)

    #        for elm in node.tabNodeChildrens :
    #
    #        j=0
    #        while j< len(node.tabNodeChildrens) :
    #            self.search_key(k, node.tabNodeChildrens[j])
    #            #return self.search_key(k, i)
    #            j +=1

    def recherche(self, v):
        for noeud in self.nodes:
            cles = noeud.tabCles
            a = 0
            b = len(cles) - 1
            while a <= b:
                m = (a + b) // 2
                if cles[m] == v:
                    return True
                elif cles[m] < v:
                    a = m + 1
                else:
                    b = m - 1
        return False

    # TODO optimiser avec tabNodeChildren et non nodes

    def is_tree(self):
        # a modifier aprés
        return True

    #    def recherche(self,v):
    #        a = 0
    #        for noeud in self.nodes:
    #            cles = noeud.tabCles
    #            b = len(cles) - 1
    #            while a <= b:
    #                m = (a + b) // 2
    #                if cles[m] == v:
    #                        # on a trouvé v
    #                    return True
    #                elif cles[m] < v:
    #                    a = m + 1
    #                else:
    #                    b = m - 1
    #                # on a a > b
    #            return False

    def numberOfElements(self):
        i = 0
        for node in self.nodes:
            i += len(node.tabCles)
        return i

    def insertKey(self, value):
        if not self.root.tabNodeChildrens:
            N = Node(self.root)
            N2 = Node(self.root)
            self.nodes.append(N)
            self.nodes.append(N2)
            self.root.tabNodeChildrens.append(N)
            self.root.tabNodeChildrens.append(N2)

            # si le nombre de fils max est pair, alors on aura un arbre équilibré avec un meme nombre de clé dans
            # chaque noeud enfant. au cas contraire, on aura filsmax//2 a gauche et filsmax//2 + filsmax%2 a droite

        # self.root.tabCles.append(value)
        # if len(self.root.tabCles) == self.nbFilsMax:
        #     if not self.root.tabNodeChildrens:


def main():
    B = Arbre(2, 3)

    N = Node()
    N.tabCles = [2, 6]

    N1 = Node()
    N1.tabCles = [1, 3]

    N2 = Node()
    N2.tabCles = [5, 7, 10]

    # N.tabNodeChildrens = [N1, Node()]
    N.tabNodeChildrens = [N1, N2]
    B.nodes.append(N)
    B.nodes.append(N1)
    B.nodes.append(N2)

    B.root = N
    B.print_tree(B.root)
    print(B.numberOfChildrens())


if __name__ == '__main__':
    main()