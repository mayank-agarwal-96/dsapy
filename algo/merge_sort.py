def merge(arr,left,middle,right):

	n1 = middle-left+1
	n2 = right-middle
	left_array = arr[left:middle+1]
	right_array = arr[middle+1:right+1]

	k = left
	i,j = 0,0
	while i < n1 and j < n2:
		if left_array[i] <= right_array[j]:
			arr[k] = left_array[i]
			i += 1
		else:
			arr[k] = right_array[j]
			j += 1
		k += 1


	while i < n1:
		arr[k] = left_array[i]
		k+=1
		i+=1

	while j < n2:
		arr[k] = right_array[j]
		k+=1
		j+=1


def merge_sort(arr,left,right):

	if left < right:
		middle = (left+right)/2
		merge_sort(arr,left,middle)
		merge_sort(arr,middle+1,right)

		merge(arr,left,middle,right)
