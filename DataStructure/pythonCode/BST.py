#!/usr/bin/env python3

#Binary Search Tree
#Reference: https://gingerkang.tistory.com/86

class Node:
	def __init__(self, data):
		self.data = data
		self.right = None
		self.left = None

class BST:
	def __init__(self):
		self.root = None
	
	def insert(self, data):
		if self.root == None:
			self.root = Node(data)
		else:
			cur_node = self.root
			while True:
				if data < cur_node.data:
					if cur_node.left == None:
						cur_node.left = Node(data)
						break
					else:
						cur_node = cur_node.left
				else:
					if cur_node.right == None:
						cur_node.right = Node(data)
						break
					else:
						cur_node = cur_node.right
	
	def search(self, data):
		cur_node = self.root
		while cur_node:
			if cur_node.data == data:
				return True
			elif cur_node.data < data:
				cur_node = cur_node.right
			else:
				cur_node = cur_node.left
		return False
	
	def delete(self, data):
		is_present = False
		cur_node = self.root
		parent = self.root
		while cur_node:
			if cur_node.data == data:
				is_present = True
				break
			elif cur_node.data < data:
				parent = cur_node
				cur_node = cur_node.right
			else:
				parent = cur_node
				cur_node = cur_node.left

		if is_present == False:
			return False

		#1. Delet할 노드가 leaf node, 바로 삭제
		if cur_node.left == None and cur_node.right == None:
			if data < parent.data:
				# 왼쪽 자식일 때
				parent.left = None
			else:
				# 오른쪽 자식일 때
				parent.right = None

		#2. Delete할 노드가 왼쪽  subtree 1개를 가질 때
		if cur_node.left != None and cur_node.right == None:
			if data < parent.data:
				# 삭제할 노드가 parent node의 왼쪽 자식일 때
				parent.left = cur_node.left
			else:
				# 삭제할 노드가 parent node의 오른쪽 자식일 때
				parent.right = cur_node.left

		#3. Delete할 노드가 오른쪽 subtree 1개를 가질 때
		if cur_node.left == None and cur_node.right != None:
			if data < parent.data:
				parent.left = cur_node.right
			else:
				parent.right = cur_node.right

		#4. Delet할 노드가 양쪽 자식 모두 있을 때
		if cur_node.left != None and cur_node.right != None:
			min_node = cur_node.right
			min_node_prev = min_node
			while min_node.left:
				min_node_prev = min_node
				min_node = min_node.left
			cur_node.data = min_node.data
			min_node_prev.left = min_node.right 
			#min_node를 없앴으니, min_node의 parent node의 left 자식을 min_node의 오른쪽 자식으로 바꿈.min_node의 왼쪽 자식은 없음. 있으면 그 왼쪽 자식이 min_node가 됐었을 것이므로
		
		return True

	
	def preorderBST(self, cur_node):
		#prints in preorder(VLR)
		if cur_node:
			print(cur_node.data)
			self.preorderBST(cur_node.left)
			self.preorderBST(cur_node.right)

	def inorderBST(self, cur_node):
		#prints in inorder(LVR)
		if cur_node:
			self.inorderBST(cur_node.left)
			print(cur_node.data)
			self.inorderBST(cur_node.right)

	def postorderBST(self, cur_node):
		#prints in postorder(LRV)
		if cur_node:
			self.postorderBST(cur_node.left)
			self.postorderBST(cur_node.right)
			print(cur_node.data)

myBST = BST()
myBST.insert(4)
myBST.preorderBST(myBST.root)
print("\n")
myBST.insert(3)
myBST.preorderBST(myBST.root)
print("\n")
myBST.insert(2)
myBST.preorderBST(myBST.root)
print("\n")
myBST.insert(5)
myBST.preorderBST(myBST.root)
print("\n")
myBST.insert(8)
'''
Current Tree Format
     4
	  / \
	 3   5
	/     \
 2       8
'''
print("preorder:")
myBST.preorderBST(myBST.root)
print("inorder:")
myBST.inorderBST(myBST.root)
print("postorder:")
myBST.postorderBST(myBST.root)
print("\n")
print(myBST.search(2))
print(myBST.delete(2))
print(myBST.preorderBST(myBST.root))
