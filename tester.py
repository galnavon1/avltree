from avl_template_new import AVLTreeList
import random
import math

import numpy as np
import time


# node structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#class Linked List
class LinkedList:
    def __init__(self):
        self.head = None

    #Inserts a new element at the given position
    def push_at(self, newElement, position):
        newNode = Node(newElement)
        if(position < 1):
            print("\nposition should be >= 1.")
        elif (position == 1):
            newNode.next = self.head
            self.head = newNode
        else:
            temp = self.head
            for i in range(1, position-1):
                if(temp != None):
                    temp = temp.next
            if(temp != None):
                newNode.next = temp.next
                temp.next = newNode
            else:
                print("\nThe previous node is null.")



def check2():
    for i in range(1, 11):
        avl1 = AVLTreeList()
        lista = LinkedList()
        n = 1500 * i
        arr = []
        start = time.time()
        for j in range(n):
            rand = random.randrange(0, avl1.size+1, 1)
            avl1.insert(rand, rand)
        end = time.time()
        print("avl", i, end - start, (end - start) / n)

        start1 = time.time()
        for j in range(n):
            rand = random.randrange(0, j+1, 1)
            lista.push_at(rand, rand)
        end1 = time.time()
        print("LinkedList", i, end1 - start1, (end1 - start1) / n)

        start2 = time.time()
        for j in range(n):
            rand = random.randrange(0, len(arr)+1)
            arr.insert(rand, rand)
        end2 = time.time()
        print("numpy array : ", i, end2 - start2, (end2 - start2) / n)


check2()


def check():
    for j in range(1, 11):
        t1 = AVLTreeList()
        t3 = AVLTreeList()
        counter1 = 0
        counter2 = 0
        counter3 = 0
        n = 1500 * (2 ** j)
        print(n)

        '''
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
        
        print(counter1)
        print(counter2)
        print(counter3)
        '''


def check1():
    for j in range(5, 11):
        t1 = AVLTreeList()
        t2 = AVLTreeList()
        t3 = AVLTreeList()
        counter1 = 0
        counter2 = 0
        counter3 = 0
        n = 10 * (2 ** j)
        for i in range(n):
            counter1 += t1.insert(random.randint(0, i), i)
            t2.insert(random.randint(0, i), i)
            counter2 += t2.insert(random.randint(0, i), i)
            if i < n // 2:
                counter3 += t3.insert(random.randint(0, i), i)
            else:
                if i % 2 == 0:
                    c = random.randint(0, t3.size - 1)
                    print(t3.retrieve(c))
                    print(t3.select(c + 1).bf)
                    print(t3.select(c + 1).right.bf)
                    print(t3.select(c + 1).left.bf)
                    t3.printt()
                    counter3 += t3.delete(c)
                else:
                    counter3 += t3.insert(random.randint(0, t3.size), i)



