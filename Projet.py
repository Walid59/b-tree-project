

class Node :
        
    
    def __init__(self, leaf = False) :
        """
        creator of a node.
        self : the object
        leaf : verification if the object is feuille or not
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
       """
       self : the object
       L : nbFilsMin
       U : nbFilsMax
       """
       self.nbFilsMin = L-1
       self.nbFilsMax = U-1
       self.root = Node(True)
       self.nodes = []
       
       
    
    def print_tree(self, node, l=0):
        """
        self : the object
        node : the root
        l : the level in the tree
        
        return the tree
        """
        print("Level ", l, " ", len(node.keyArray), end=":")
        for i in node.keyArray:
            print(i, end=" ")
        print()
        l += 1
        if len(node.tabNodeChildrens) > 0:
            for i in node.tabNodeChildrens:
                self.print_tree(i, l)
                
                
    
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
        k : the element that we are searching
        node : verification if we are in node or leaf
        """
        if node is not None:
            i = 0
            while i < len(node.tabCles) and k > node.tabCles[i]:
                i += 1
            if i < len(node.tabCles) and k == node.tabCles[i]:
                return (node, i)
            if node.feuille:
                return None
        else:
            return self.search_key(k, self.root)
        
        for i in node.tabNodeChildrens :
            self.root  =i
            return self.search_key(k, i)   

    
      
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
    
    N = Node()
    N.keyArray = [12,16]
    
    N1 = Node()
    N1.keyArray = [10]
    
    N2 = Node()
    N2.keyArray = [14]
    
    N3 = Node()
    N3.keyArray = [18]
    
    N.tabNodeChildrens = [N1,N2,N3]
    B.nodes.append(N)
    B.nodes.append(N1)
    B.nodes.append(N2)
    B.nodes.append(N3)
    B.insertAA(15)
 
    B.root = N
    B.print_tree(B.root)
  
if __name__ == '__main__':
    main()
    