

class Node :
        
    
    def __init__(self, feuille = False) :
        """
        creator of a node.
        self : the object
        feuille : verification if the object is feuille or not
        """
        self.feuille = feuille
        self.tabCles = []
        self.tabNodeChildrens = []

    def ajoutCle(self, cle) :
        """
        
        self : the object
        
        """
        self.tabCles.append(cle)
        
    def ajoutCles(self, nbCles) :
        """
        
        self : the object
        
        """
        listevaleurs = [i for i in range (nbCles)]
        for i in  listevaleurs:
            self.tabCles.append(i)
     
    # juste pour verification
    def ajoutFils(self, arbre1, arbre2, arbre3) :
        """
        
        self : the object
        
        """
        self.tabFils.append(arbre1)
        self.tabFils.append(arbre2)
        self.tabFils.append(arbre3)
        #self.tabFils.append(arbre)

    def verificationSiFeuille(self) :
        """
        
        self : the object
        
        """
        if len(self.tabFils) == 0 :
            self.feuille = True
        return self.feuille

    
    def ajoutFils(self, Arbre) :
        """
        
        self : the object
        
        """
        self.tabFils.append(Arbre)
        
    def gettabCles(self) :
        """
        get the list of keys
        self : the object
        
        """
        return self.tabCles
    
    def parcourir(self) :
        """
        brows in the node
        self : the object
        """
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
       
    
    def print_tree(self, node, l=0):
        """
        
        self : the object
        
        """
        print("Level ", l, " ", len(node.tabCles), end=":")
        for i in node.tabCles:
            print(i, end=" ")
        print()
        l += 1
        if len(node.tabNodeChildrens) > 0:
            for i in node.tabNodeChildrens:
                self.print_tree(i, l)
                
                
    def addNode(self, node) :
        """
        
        self : the object
        
        """
        n = len(self.nodes)
        if n >= self.nbFilsMax :
            raise Exception('le nombre maximal des noeuds et dépassé')
        else :
            self.nodes.append(node)
    
    
    def parcourir(self) :
        """
        
        self : the object
        
        """
        i = 0
        if self.root != None :
            self.root.parcourir()
            i += 1
            print(i)
 
    def search_key(self, k, node=None):
        """
        
        self : the object
        
        """
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
        """
        
        self : the object
        
        """
        root = self.root
        if len(root.tabCles) == (self.nbFilsMax) - 1:
          temp = Node()
          self.root = temp
          temp.tabNodeChildrens.insert(0, root)
          self.split_child(temp, 0)
          self.insert_non_full(temp, k)
        else:
          self.insert_non_full(root, k)
    
    def insert_non_full(self, x, k):
        """
        
        self : the object
        
        """
        i = len(x.tabCles) - 1
        if x.feuille:
          x.tabCles.append((None, None))
          while i >= 0 and k[0] < x.keys[i][0]:
            x.tabCles[i + 1] = x.tabCles[i]
            i -= 1
          x.tabCles[i + 1] = k
        else:
          while i >= 0 and k[0] < x.tabCles[i][0]:
            i -= 1
          i += 1
          if len(x.tabNodeChildrens[i].keys) == (2 * self.t) - 1:
            self.split_child(x, i)
            if k[0] > x.tabCles[i][0]:
              i += 1
          self.insert_non_full(x.tabNodeChildrens[i], k)

    # Split the child
    def split_child(self, x, i):
        t = (self.nbFilsMax)/2
        y = x.tabNodeChildrens[i]
        z = Node(y.feuille)
        x.tabNodeChildrens.insert(i + 1, z)
        x.tabCles.insert(i, y.tabCles[t - 1])
        z.tabCles = y.tabCles[t: (2 * t) - 1]
        y.tabCles = y.tabCles[0: t - 1]
        if not y.leaf:
          z.tabNodeChildrens = y.tabNodeChildrens[t: 2 * t]
          y.tabNodeChildrens = y.tabNodeChildrens[0: t - 1]
 

def main():
    B = Arbre(2, 3)
    
#    N = Node()
#    N.tabCles = [2,6]
#    
#    N1 = Node()
#    N1.tabCles = [1,3]
#    
#    N2 = Node()
#    N2.tabCles = [5,7,10] 
#    
#    N.tabNodeChildrens = [N1,N2]
#    B.nodes.append(N)
#    B.nodes.append(N1)
#    B.nodes.append(N2)
    B.insert(2)
    B.insert(3)
    B.insert(4)
    
#    B.root = N
    B.print_tree(B.root)
    
    for i in B.nodes:
        B.root = i
        if B.search_key(7) is not None:
            print( True)
        else:
            print( False)
        
         
if __name__ == '__main__':
    main()
    