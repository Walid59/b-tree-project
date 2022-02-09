

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
        
    def gettabCles(self) :
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
                
                
    def addNode(self, node) :
        n = len(self.nodes)
        if n >= self.nbFilsMax :
            raise Exception('le nombre maximal des noeuds et dépassé')
        else :
            self.nodes.append(node)
    
    
    def parcourir(self) :
        i = 0
        if self.root != None :
            self.root.parcourir()
            i += 1
            print(i)
 
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
        
        for i in node.tabNodeChildrens :
            self.root  =i
            return self.search_key(k, i)   
#        for elm in node.tabNodeChildrens :
#            
#        j=0
#        while j< len(node.tabNodeChildrens) :
#            self.search_key(k, node.tabNodeChildrens[j])
#            #return self.search_key(k, i)
#            j +=1
    
    
    def insert(self, k):
        root = self.root
        if len(root.tabCles) == (2 * self.t) - 1:
          temp = Node()
          self.root = temp
          temp.tabNodeChildrens.insert(0, root)
          # split in tabNodeChildrens ..

    
    def is_tree(self) :
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
        
    def insert(self, element) :
        # a modifier apres
        return None

def main():
    B = Arbre(2, 3)

 
    N = Node()
    N.tabCles = [2,6]
    
    N1 = Node()
    N1.tabCles = [1,3]
    
    N2 = Node()
    N2.tabCles = [5,7,10] 
    
    #N.tabNodeChildrens = [N1, Node()]
    N.tabNodeChildrens = [N1,N2]
    B.nodes.append(N)
    B.nodes.append(N1)
    B.nodes.append(N2)
    
    B.root = N
    B.print_tree(B.root)
    
    for i in B.nodes:
        B.root = i
        if B.search_key(7) is not None:
            print( True)
        else:
            print( False)
        
         
if __name__ == '__main__':
    main()
    