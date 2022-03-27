import random

from Tree import *
from Node import *
import graphviz


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

    liste = list(range(1,20 +1))
    random.shuffle(liste)
    tree.insertKeys(liste)
    print(liste)

    tree.toGraph()
    #tree.toStringAllNodes(tree.root)
    #print(tree.exists_key(18))


if __name__ == '__main__':
    main()