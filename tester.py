from avl_template_new import AVLTreeList
import random
import math

    def tester():

        for i in range(1):
            avl1 = AVLTreeList()
            p = random.randint(0,10)
            for i in range(0,p):
                avl1.insert(i, i)

            for i in range(0,math.floor(p/2)):
                d = random.randint(0, avl1.getRoot().length() -1)

                pp= avl1.delete(d)
                if(pp==-1):
                    print("l")
            if (p - math.floor(p/2)) != len(avl1.listToArray()):
                print("no")

            avl2 = AVLTreeList()
            p = random.randint(0,10)
            for i in range(0,p):
                avl2.insert(i, i+10)

            for i in range(0,math.floor(p/2)):
                d = random.randint(0, avl2.getRoot().length() -1)
                if(avl2.delete(d)==-1):
                    print("l")

            for row in trepr(avl1.getRoot()):
                print(row)
            for row in trepr(avl2.getRoot()):
                print(row)
            l1 = avl1.listToArray()
            l2 = avl2.listToArray()
            if (avl1.isAvlTree() == False):
                print("l")
            avl1.concat(avl2)
            for row in trepr(avl1.getRoot()):
                print(row)

            if (avl1.isAvlTree() == False):
                print("l")
            if avl1.listToArray()[0] != avl1.first():
                print(list)
            if avl1.listToArray().pop() != avl1.last():
                print("l")
            if avl1.listToArray() != (l1+ l2):
                print(l1)
                print(l2)
                print(avl1.listToArray())


