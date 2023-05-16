#!/usr/bin/env python3

class MinHeap(object):
	def __init__(self):
		self.queue = []
	
	def insert(self, data):
		self.queue.append(data)
		data_index = len(self.queue) - 1
		parent_index = self.parent(data_index)
		while self.queue[parent_index] > data:
			if data_index == 0:
				break
			self.swap(data_index, parent_index)
			data_index = parent_index
			parent_index = self.parent(data_index)
	
	def delete(self):
		last_index = len(self.queue) - 1
		if last_index < 0:
			return -1
		self.swap(0, last_index)
		ret = self.queue.pop()
		self.minHeapify(0)
		return ret

	def minHeapify(self, cur_index):
		left_index = self.leftChild(cur_index)
		right_index = self.rightChild(cur_index)
		min_index = cur_index

		if left_index <= len(self.queue) - 1 and self.queue[min_index] > self.queue[left_index]:
			min_index = left_index
		if right_index <= len(self.queue) - 1 and self.queue[min_index] > self.queue[right_index]:
			min_index = right_index

		if min_index != cur_index:
			self.swap(cur_index, min_index)
			self.minHeapify(min_index)

	
	def swap(self, cur_index, swap_index):
		self.queue[cur_index], self.queue[swap_index] = self.queue[swap_index], self.queue[cur_index]
	
	def parent(self, index):
		return (index - 1) // 2
	
	def leftChild(self, index):
		return index * 2 + 1

	def rightChild(self, index):
		return index * 2 + 2


myheap = MinHeap()
myheap.insert(4)
print(myheap.queue)
myheap.insert(3)
print(myheap.queue)
myheap.insert(2)
print(myheap.queue)
myheap.insert(1)
print(myheap.queue)

myheap.delete()
print(myheap.queue)
myheap.delete()
print(myheap.queue)
