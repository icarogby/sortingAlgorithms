from algorithms import *
from time import time

def main():
    arr = [5,7,9,3,24,-70,-5,95,67,0,-2,123,14,95,75]

    opc = int(input("Select a algorithm: "))

    time1 = time()
    match opc:
        case 0:
            selectionSort(arr)
        case 1:
            insertionSort(arr)
        case 2:
            bubbleSort(arr)
        case 3:
            mergeSort(arr)
        case 4:
            heapSort(arr)
        case 5:
            quickSort(arr)

    time2 = time()

    print(arr)
    print(time2-time1)

if __name__ == "__main__":
    main()
