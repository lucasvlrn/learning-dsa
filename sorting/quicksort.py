#1°
def quicksort(arr,left, right):
    print(arr[left:right+1])
    if left < right:
        pi = partition(arr, left, right)
        quicksort(arr, left, pi-1)
        quicksort(arr, pi+1, right)

def partition(arr, left, right):
    pivot = arr[right]
    i = left -1
    for j in range(left, right):
        if arr[j] <= pivot:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1],arr[right] = arr[right], arr[i+1]
    return i+1

arr = [0,3,6,7,8,4,2,1,5]
quicksort(arr, 0, len(arr)-1)

#2°

def quicksort_listcomprehension(arr):
    if len(arr) <=1
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        bigger_than_pivot = [x for x in arr[1:] if x > pivot]
        return quicksort_listcomprehension(less_than_pivot)+[pivot]+quicksort_listcomprehension(bigger_than_pivot)
arr = quicksort_listcomprehension(arr)