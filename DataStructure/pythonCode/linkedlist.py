#!/usr/bin/env python3
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def append(self, data):
		node = Node(data)
		if self.head is None:
			self.head = node
			self.tail = node
		else:
			prev = self.head
			while prev.next:
				prev = prev.next
			prev.next = node
			self.tail = node

#head = Node(1)
#head.next = Node(2)
#head.next.next = Node(3)

mylist = LinkedList()
mylist.append(1)
mylist.append(2)
mylist.append(3)

node = mylist.head
while(node != mylist.tail):
	print(node.data, end =" ")
	node = node.next
print(node.data, "\n")
