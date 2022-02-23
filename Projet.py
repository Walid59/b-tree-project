class Node :
        
    def __init__(self, feuille = False) :
        #self.taille = taille
        #self.parent = parent
        #self.nbClesMin = L-1
        #self.nbClesMax = U-1
        self.feuille = feuille
        #self.n = n # nobre des element dans ce neoud
        self.tabCles = []
        self.tabNodeChildrens = []
        # Current number of keys
        #self.n = 0
    
    """
    This is a javadoc style.

    @param param1: this is a first param
    @param param2: this is a second param
    @return: this is a description of what is returned
    @raise keyError: raises an exception
    """
    def ajoutCle(self, cle) :
        self.tabCles.append(cle)
        
    def ajoutCles(self, nbCles) :
        listevaleurs = [i for i in range (nbCles)]
        for i in  listevaleurs:
            self.tabCles.append(i)
     
    # juste pour verification
    def ajoutFils(self, arbre1, arbre2, arbre3) :
        self.tabFils.append(arbre1)
        self.tabFils.append(arbre2)
        self.tabFils.append(arbre3)
        
    
    def verificationSiFeuille(self) :
        if len(self.tabFils) == 0 :
            self.feuille = True
        return self.feuille
        
    def presentation(self) :
        None
    
    def ajoutFils(self, Arbre) :
        self.tabFils.append(Arbre)
        
    def ajoutFils(self, arbre) :
        self.tabFils.append(arbre)
        
    def getTabCles(self) :
        return self.tabCles
    
    def getTaille(self) :
        print(self)
        return self.taille
    
    def parcourir(self) :
        i = 0
        for i in self.n :
            if self.feuille == False :
                self.tabFils[i].parcourir()
            print(self.tabCles[i])
        if self.feuille == False :
            self.tabFils[i].parcourir()

    def insert(self, key):
        if self.tabCles:
            if key < self.tabCles[0]:
                self.tabCles.insert(0, key)
            index = 1
            for val in self.tabCles:
                print("val:",val)
                if key > val:
                    print("avant ajout de ", key, ":", self.tabCles)
                    self.tabCles.insert(index,key)
                    print("apres ajout de ", key, ":", self.tabCles)
                    break
                index += 1

        else:
            self.tabCles.append(key)

        #si on a un seul element pour (L,U) = (2,3)
        #alors la valeur retournée sera un tableau vide et que donc la valeur sera ajoutée directement au noeud.
        # au cas contraire, la fonction insert de l'arbre fera le traitement necessaire sur les autres noeuds pour ajouter la valeur.
        length = len(self.tabCles)
        middle_index = length // 2
        second_half = self.tabCles[middle_index:]
        return second_half

    
class Arbre :
    
    def __init__(self, L, U) :
       self.nbFilsMin = L-1
       self.nbFilsMax = U-1
       self.root = Node(True)
       self.nodes = []
       #self.listeArbres = listeArbres
       #self.val = None
       #self.left = None
       #self.right = None
       
    """
    Add nodes to the tree
    @param node : the node added to the tree
    """
    
    def print_tree(self, node, l=0):
        print("Level ", l, " ", len(node.tabCles), end=":")
        for i in node.tabCles:
            print(i, end=" ")
        print()
        l += 1
        if len(node.tabNodeChildrens) > 0:
            for i in node.tabNodeChildrens:
                self.print_tree(i, l)
                
                
    # def insert(self, node) :
    #     n = len(self.nodes)
    #     if n >= self.nbFilsMax :
    #         raise Exception('le nombre maximal des noeuds et dépassé')
    #     else :
    #         self.nodes.append(node)

    def insert(self, key):
        print("-----------------------------")
        print("pour l'ajout de :",key)
        result = self.root.insert(key)
        print("result",result)
        if len(result) > 1:
            newNode = Node()
            newNode.tabCles.append(result[0])
            newNode.tabNodeChildrens.append(self.root.tabCles)
            newNode.tabNodeChildrens.append(result[result[0]:])
            self.root = newNode


    def parcourir(self) :
        i = 0
        if self.root != None :
            self.root.parcourir()
            i += 1
            print(i)

    def search_key(self,v):
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
    #TODO optimiser avec tabNodeChildren et non nodes
    
    def is_tree(self) :
        # a modifier aprés
        return True


def main():
    B = Arbre(2, 3)

    N = Node()
    N.tabCles = [2,6]
    
    N1 = Node()
    N1.tabCles = [1,3]
    
    N2 = Node()
    N2.tabCles = [5,7,10] 
    
    N.tabNodeChildrens = [N1,N2]
    B.nodes.append(N)
    B.nodes.append(N1)
    B.nodes.append(N2)
    
    B.root = N

    #B.print_tree(B.root)
    #PARCOURS D'ARBRE : OK

    #print(B.recherche(10))
    #RECHERCHE : OK

    tree = Arbre(2, 3)
    tree.insert(1)
    print("noeud racine apres ajout de 1 :",tree.root.tabCles)
    tree.insert(2)
    print("noeud racine apres ajout de 2 :",tree.root.tabCles)
    tree.insert(3)
    print("noeud racine apres ajout de 3 :",tree.root.tabCles)
    print("noeud enfants apres ajout de 3 :",tree.root.tabNodeChildrens)



if __name__ == '__main__':
    main()