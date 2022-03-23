from Tree import *
from Node import *


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
    tree.insertKeys([1,2,3,4,5,6,7,8,9,10])


    tree.toStringAllNodes(tree.root)

    tree.graph()

if __name__ == '__main__':
    main()