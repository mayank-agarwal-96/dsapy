class Queue(object):

	def __init__(self):
		self.__items = []
		
	def isEmpty(self):
		return self.__items == []
		
	def enqueue(self,item):
		self.__items.append(item)
	
	def dequeue(self):
		return self.__items.pop(0)
	
	def size(self):
		return len(self.__items)
