def selectionSort(arr: list) -> list:
    for i in range(len(arr)):
        min = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j

        arr[i], arr[min] = arr[min], arr[i]

    return arr

def insertionSort(arr: list) -> list:
    for i in range(1, len(arr)):
        key = arr[i]

        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            
            j -= 1

        arr[j + 1] = key

    return arr

def bubbleSort(arr: list) -> list:
    exchanges = True
    i = len(arr) - 1

    while i > 0 and exchanges:
        exchanges = False

        for j in range(i):
            if arr[j] > arr[j + 1]:
                exchanges = True
                
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        i -= 1

    return arr

def mergeSort(arr: list) -> list:
    if len(arr) > 1:
        mid = len(arr)//2
  
        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)
  
        i = j = k = 0
  
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            
            k += 1
  
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
  
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr
 
def heapSort(arr: list) -> list:
    n = len(arr)

    for i in range(n):
        if arr[i] > arr[int((i - 1) / 2)]:
            j = i

            while arr[j] > arr[int((j - 1) / 2)]:
                (arr[j], arr[int((j - 1) / 2)]) = (arr[int((j - 1) / 2)], arr[j])
                
                j = int((j - 1) / 2)
 
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]

        j, index = 0, 0
         
        while True:
            index = 2 * j + 1
             
            if (index < (i - 1) and arr[index] < arr[index + 1]):
                index += 1

            if index < i and arr[j] < arr[index]:
                arr[j], arr[index] = arr[index], arr[j]
         
            j = index
            
            if index >= i:
                break
    
    return arr

def quickSort(arr: list) -> list:
    low = 0
    high = len(arr)-1

    if low < high:
        pivot = arr[high]

        i = low - 1
    
        for j in range(low, high):
            if arr[j] <= pivot:
                i = i + 1
    
                (arr[i], arr[j]) = (arr[j], arr[i])
    
        (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])

        pi = i + 1
 
        arr[:pi] = quickSort(arr[:pi])
        arr[pi:] = quickSort(arr[pi:])

    return arr

    