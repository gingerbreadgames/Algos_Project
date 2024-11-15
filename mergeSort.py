# Type: Merge Sort
def merge(arr, l, m, r):
	n1 = m - l + 1
	n2 = r - m
	L = arr[l:m + 1]
	R = arr[m + 1:r + 1]

	i, j, k = 0, 0, l

	while i < n1 and j < n2:
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1

	while i < n1:
		arr[k] = L[i]
		i += 1
		k += 1

	while j < n2:
		arr[k] = R[j]
		j += 1
		k += 1
 
 
def mergeSort(arr, l, r):
	if l < r:
		m = l+(r-l)//2
		mergeSort(arr, l, m)
		mergeSort(arr, m+1, r)
		merge(arr, l, m, r)