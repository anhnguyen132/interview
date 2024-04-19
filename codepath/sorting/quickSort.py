def partition(array, start, end):
  pivot = array[end]
  partition_index = start
  def swap(a, b):
    array[a], array[b] = array[b], array[a]
    
  for i in range(start, end): #swap partition index with array value compared to pivot
    if array[i] <= pivot:
      swap(i, partition_index)
      partition_index += 1

  swap(partition_index, end) #swap pivot with parition index after going through array
  return partition_index
  
def quicksortHelper(array, start, end):
  if(start >= end):
    return
  partition_index = partition(array, start, end)
  quicksortHelper(array, start, partition_index-1)
  quicksortHelper(array, partition_index + 1, end)

def quicksort(array):
  quicksortHelper(array, 0, len(array) - 1)
