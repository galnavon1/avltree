from avl_template_new import AVLTreeList
import random
import math

def check():
    for j in range(1, 11):
        t1 = AVLTreeList()
        t3 = AVLTreeList()
        counter1 = 0
        counter2 = 0
        counter3 = 0
        n=1500*(2**j)
        for i in range(n):
            counter1 += t1.insert(random.randint(0, i), i)
            if i < n//2:
                counter3 += t3.insert(random.randint(0, i), i)
            else:
                if i % 2 == 0:
                    counter3 += t3.delete(random.randint(0, t3.size-1))
                else:
                    counter3 += t3.insert(random.randint(0, t3.size), i)
        for i in range(n):
            counter2 += t1.delete(random.randint(0, t1.size-1))
        print(j)
        print(counter1)
        print(counter2)
        print(counter3)

check()


def check1():
    for j in range(5, 11):
        t1 = AVLTreeList()
        t2 = AVLTreeList()
        t3 = AVLTreeList()
        counter1 = 0
        counter2 = 0
        counter3 = 0
        n = 10*(2**j)
        for i in range(n):
            counter1 += t1.insert(random.randint(0, i), i)
            t2.insert(random.randint(0, i), i)
            counter2 += t2.insert(random.randint(0, i), i)
            if i < n//2:
                counter3 += t3.insert(random.randint(0, i), i)
            else:
                if i % 2 == 0:
                    c = random.randint(0, t3.size-1)
                    print(t3.retrieve(c))
                    print(t3.select(c+1).bf)
                    print(t3.select(c + 1).right.bf)
                    print(t3.select(c + 1).left.bf)
                    t3.printt()
                    counter3 += t3.delete(c)
                else:
                    counter3 += t3.insert(random.randint(0, t3.size), i)



