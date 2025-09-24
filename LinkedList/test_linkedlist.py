#test LinkedList
from linked_list import LinkedList

myList = LinkedList(20)     # New Linkedlist with one node -> value = 20
myList.insert(0,10)
myList.insert(1, 30)
myList.insert(0,0)
myList.insert(4,40)
myList.print_list()         # print myList -> output -> 0 , 10 , 30 , 20 , 40
myList.append(20)
myList.append(30)
myList.append(40)
myList.append(50)
myList.append(60)

myList.set_value(6,200)
myList.print_list()