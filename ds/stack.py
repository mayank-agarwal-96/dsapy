class Stack:

	def __init__(self):
		self.__array = []

	def isEmpty(self):
		return self.__array == []

	def push(self, value):
		self.__array.append(value)

	def pop(self):
		return self.__array.pop()

	def size(self):
		return len(self.__array)

