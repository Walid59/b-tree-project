import random

from Tree import *


def main():
    tree = Tree(2, 3)

    liste = list(range(1,10 +1))
    random.shuffle(liste)
    print(liste)
    tree.insertKeys(liste)
    #print(tree.toStringAllNodes(tree.root))
    tree.toGraph()
    #tree.remove(2)

if __name__ == '__main__':
    main()