Time Complexity: O(nlogn)

import random

def partition(arr,left,right):
	p = random.randint(left,right)

	arr[left],arr[p] = arr[p],arr[left]

	pivot = arr[left]

	i = j = left+1

	for j in range(left+1,right+1):
		if arr[j] <= pivot:
			arr[j],arr[i] = arr[i],arr[j]
			i = i+1

	arr[left],arr[i-1] = arr[i-1],arr[left]

	return i-1

def quicksort(arr,left,right):
	"""
    Sorts the list 'arr' using Quick sort algorithm
    >>> from dsapy.algo import quicksort
    >>> arr = [30, 40, 12, 11, 15, 0]
    >>> right = len(arr) - 1
    >>> quicksort(arr,0,right)
    >>> arr
    [0, 11, 12, 15, 30, 40]
    
    """
	if left < right:
		p = partition(arr,left,right)
		quicksort(arr,left,p-1)
		quicksort(arr,p+1,right)
