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
         print('None')


    def print_list(self):
        temp = self.head
        if temp is None :
          print("Empty List")
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

    def pop(self):
       if self.length == 0:
          return None
       temp = self.head
       pre = self.head
       
       if self.length == 1:
          self.head = None
          self.tail = None
          self.length-=1
          return temp.value
       
       while(temp.next is not None):
          pre = temp
          temp = temp.next
       self.tail = pre
       self.tail.next = None
       self.length-=1

       return temp.value
    
    def prepend(self, value):
      newNode = Node(value)
      if self.length == 0:
         self.head = newNode
         self.tail = newNode
         self.length = 1
      else:
         newNode.next = self.head
         self.head = newNode
       
    
