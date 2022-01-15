

class Node :
        
    def __init__(self,taille) :
        self.taille = taille
        self.feuille = False
        #self.parent = parent
        self.tabCles = []
        self.tabFils = []
    
    """
    This is a javadoc style.

    @param param1: this is a first param
    @param param2: this is a second param
    @return: this is a description of what is returned
    @raise keyError: raises an exception
    """
    def ajoutCle(self, cle) :
        self.tabCles.append(cle)
        
    def ajoutCles(self) :
        listevaleurs = [i for i in range (self.taille)]
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
    
    
class Arbre :
    
    def __init__(self, Order) :
       self.Order = Order
       #self.listeArbres = listeArbres
       
       self.val = None
       self.left = None
       self.right = None
           
    
       
        
    