

class Node :
        
    
    def __init__(self, leaf = False) :
        """
        creator of a node.
        self : the object
        feuille : verification if the object is feuille or not
        """
        self.leaf = leaf
        self.keyArray = []
        self.tabNodeChildrens = []

    def split(self, parent, payload):
      """Split a node and reassign keys/children."""
      new_node = self.__class__(self.nbFilsMax)

      mid_point = self.size//2
      split_value = self.keys[mid_point]
      parent.add_key(split_value)

      # Add keys and children to appropriate nodes
      new_node.children = self.children[mid_point + 1:]
      self.children = self.children[:mid_point + 1]
      new_node.keys = self.keys[mid_point+1:]
      self.keys = self.keys[:mid_point]

      # If the new_node has children, set it as internal node
      if len(new_node.children) > 0:
        new_node.leaf = False

      parent.children = parent.add_child(new_node)
      if payload < split_value:
        return self
      else:
        return new_node
    
    def add_key(self, value):
      """Add a key to a node. The node will have room for the key by definition."""
      self.tabCles.append(value)
      self.tabCles.sort()
      
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
        print("Level ", l, " ", len(node.keyArray), end=":")
        for i in node.keyArray:
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
    
    
    
      
    def insertAA(self, key) :
#        res = self.root
#        for elm in range (0, len(self.root.keyArray)) :
#            if key < elm :
        node = self.root   
        while not node.leaf:
          i = len(node.keyArray) - 1
          while i > 0 and key < node.keyArray[i] :
            i -= 1
          # incrementation de la taille de keyArray
          if key > node.keyArray[i]:
            i += 1
          next = node.tabNodeChildrens[i]
          if len(next.keyArray) == self.nbChildMax :
            node = next.split(node, key)
          else:
            node = next
        # Since we split all full nodes on the way down, we can simply insert the payload in the leaf.
        node.keyArray.append(key)
        node.keyArray.sort()
            #node.add_key(key)
        
def main():
    B = Arbre(1, 3)
    B.insertAA(12)
#    B.insertAA(16)
#    
#    B.insertAA(10)
#    B.insertAA(14)
#    
#    B.insertAA(15)
#    
#    B.print_tree(B.root)
    
    N = Node()
    N.keyArray = [12,16]
#    
    N1 = Node()
    N1.keyArray = [10]
#    
    N2 = Node()
    N2.keyArray = [14]
    
    N3 = Node()
    N3.keyArray = [18]
#    
    N.tabNodeChildrens = [N1,N2,N3]
    B.nodes.append(N)
    B.nodes.append(N1)
    B.nodes.append(N2)
    B.nodes.append(N3)
    B.insertAA(15)
#    B.insert(2)
#    B.insert(3)
#    B.insert(4)
    
    B.root = N
    B.print_tree(B.root)
#    
#    for i in B.nodes:
#        B.root = i
#        if B.search_key(7) is not None:
#            print( True)
#        else:
#            print( False)
#        
         
if __name__ == '__main__':
    main()
    