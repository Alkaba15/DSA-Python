#test LinkedList
from linked_list import LinkedList

myList =  LinkedList(10);
myList.append(20)
myList.append(30)
myList.append(40)
myList.append(50)
myList.append(60)


myList.prepend(0)

print(myList.tail.value)