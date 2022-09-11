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

# selectionsort
# shell

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

# heap
# quick
