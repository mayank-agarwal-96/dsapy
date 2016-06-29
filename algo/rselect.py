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

def rselect(arr,left,right,n):
	"""
    Returns the nth smallest number of an array
    >>> from dsapy.algo import rselect
    >>> arr = [30, 40, 12, 11, 15, 0]
    >>> right = len(arr) - 1
    >>> x = rselect(arr,0,right,3)
    >>> x
    12
    """
	if n > 0 and n <= right-left + 1:
		p = partition(arr,left,right)
		j = p
		if j-left == n-1:
			return arr[j]
		elif j-left > n-1:
			return rselect(arr,left,j-1,n)
		else:
			return rselect(arr,j+1,right,n-j+left-1)
	else:
		return None
