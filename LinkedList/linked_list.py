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
        while temp is not None:
            print(temp.value)
            temp = temp.next
