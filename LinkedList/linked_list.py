#Implementation LinkedList
from node import Node

class LinkedList :                  # LinkedList Class
    def __init__(self, value=None):
        newNode = Node(value)
        if value is not None :
          self.head = newNode
          self.tail = newNode
          self.length = 1
        else:
         self.head = None 
         self.tail = None
         self.length = 0


    def print_list(self):
        temp = self.head
        if temp is None :
          print("None")
          return

        while temp is not None:
            print(temp.value)
            temp = temp.next
        

    def append(self, value):
       newNode = Node(value)
       if self.head is None:
          self.head = newNode
          self.tail = newNode
       else:
          self.tail.next = newNode
          self.tail = newNode
          self.length+=1
          