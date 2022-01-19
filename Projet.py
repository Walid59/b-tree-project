

class Node :
        
    def __init__(self, n, feuille = False) :
        #self.taille = taille
        #self.parent = parent
        self.feuille = feuille
        #self.nbClesMin = L-1
        #self.nbClesMax = U-1
        self.n = n # nobre des element dans ce neoud
        self.tabCles = []
        self.tabNodeChildrens = []
        # Current number of keys
        self.n = 0 
    
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
       self.rout = None
       self.nodes = []
       #self.listeArbres = listeArbres
       #self.val = None
       #self.left = None
       #self.right = None
       
    """
    Add nodes to the tree
    @param node : the node added to the tree
    
    """
    def addNode(self, node) :
        n = len(self.nodes)
        if n >= self.nbFilsMax :
            raise Exception('le nombre maximal des noeuds et dépassé')
        else :
            self.nodes.append(node)
    
    
    def parcourir(self) :
        i = 0
        if self.rout != None :
            self.rout.parcourir()
            i += 1
            print(i)
        
    
    def search(self, cle) :
        if self.rout == None :
            return None
        else :
            return self.rout.search(cle)
    
    def is_tree(self) :
        # a modifier aprés
        return True
       
    def recherche(self, element) :
        #a modifier apres
        return True
        
    def insert(self, element) :
        # a modifier apres
        return None

    