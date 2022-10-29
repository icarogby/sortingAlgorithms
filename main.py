from algorithms import *
from time import time
import sys

def main():
    sys.setrecursionlimit(200000)

    opc = input("File Adress: ")


    file = open(opc)
    arr = []

    for line in file:
        arr.append(int(line))

    file.close()

    print(arr)

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
