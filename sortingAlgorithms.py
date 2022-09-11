from util import *

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

def mergeSort(arr, l, r):
    if l < r:
 
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2
 
        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
