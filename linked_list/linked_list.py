from __future__ import annotations
from typing import List, Any

class Node:
    def __init__(self, data= None, next= None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None)
    
    def insert_values(self, data_list: List[Any]) -> LinkedList:
        for element in data_list:
            self.insert_at_end(element)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.head = self.head.next
            return
    
        count = 0
        itr = self.head
        while itr and count < index-1:
            itr = itr.next
            count += 1
        itr.next = itr.next.next

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr and count < index-1:
            itr = itr.next
            count += 1
        node = Node(data, itr.next)
        itr.next = node
        

    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        
        itr = self.head
        llstr = ""

        while itr.next:
            llstr += str(itr.data) + '->'
            itr = itr.next
        print(f"{llstr}{itr.data}")

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    print(ll.get_length())
    ll.remove_at(2)
    print(ll.get_length())
    ll.print()
    ll.insert_at(1,"figs")
    ll.print()
    ll.insert_at(4,"strawberries")
    ll.print()