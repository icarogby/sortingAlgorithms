from algorithms import *

from time import time
import sys

def loadAleatory():
    try:
        file1 = open("test cases\\800aleatory.txt")
        file2 = open("test cases\\4000aleatory.txt")
        file3 = open("test cases\\20000aleatory.txt")
        file4 = open("test cases\\100000aleatory.txt")
        file5 = open("test cases\\500000aleatory.txt")

        arr1 = []
        arr2 = []
        arr3 = []
        arr4 = []
        arr5 = []

        for line in file1:
            arr1.append(int(line))

        for line in file2:
            arr2.append(int(line))

        for line in file3:
            arr3.append(int(line))

        for line in file4:
            arr4.append(int(line))

        for line in file5:
            arr5.append(int(line))
    
    except:
        print("Fail.")
    else:
        file1.close()
        file2.close()
        file3.close()
        file4.close()
        file5.close()

    return arr1, arr2, arr3, arr4, arr5

def loadAscending():
    try:
        file1 = open("test cases\\800ascending.txt")
        file2 = open("test cases\\4000ascending.txt")
        file3 = open("test cases\\20000ascending.txt")
        file4 = open("test cases\\100000ascending.txt")
        file5 = open("test cases\\500000ascending.txt")

        arr1 = []
        arr2 = []
        arr3 = []
        arr4 = []
        arr5 = []

        for line in file1:
            arr1.append(int(line))

        for line in file2:
            arr2.append(int(line))

        for line in file3:
            arr3.append(int(line))

        for line in file4:
            arr4.append(int(line))

        for line in file5:
            arr5.append(int(line))
    
    except:
        print("Fail.")
    else:
        file1.close()
        file2.close()
        file3.close()
        file4.close()
        file5.close()

    return arr1, arr2, arr3, arr4, arr5

def loadDescending():
    try:
        file1 = open("test cases\\800descending.txt")
        file2 = open("test cases\\4000descending.txt")
        file3 = open("test cases\\20000descending.txt")
        file4 = open("test cases\\100000descending.txt")
        file5 = open("test cases\\500000descending.txt")

        arr1 = []
        arr2 = []
        arr3 = []
        arr4 = []
        arr5 = []

        for line in file1:
            arr1.append(int(line))

        for line in file2:
            arr2.append(int(line))

        for line in file3:
            arr3.append(int(line))

        for line in file4:
            arr4.append(int(line))

        for line in file5:
            arr5.append(int(line))
    
    except:
        print("Fail.")
    else:
        file1.close()
        file2.close()
        file3.close()
        file4.close()
        file5.close()

    return arr1, arr2, arr3, arr4, arr5

def selectionTest(opc: int) -> list:
    results = []

    match opc:
        case 1:
            temp_arr1, temp_arr2, temp_arr3, temp_arr4, temp_arr5 = loadAleatory()
        case 2:
            temp_arr1, temp_arr2, temp_arr3, temp_arr4, temp_arr5 = loadAscending()
        case 3:
            temp_arr1, temp_arr2, temp_arr3, temp_arr4, temp_arr5 = loadDescending()
    
    time1 = time()
    selectionSort(temp_arr1)
    time2 = time()
    results.append(time2 - time1)

    time1 = time()
    selectionSort(temp_arr2)
    time2 = time()
    results.append(time2 - time1)

    time1 = time()
    selectionSort(temp_arr3)
    time2 = time()
    results.append(time2 - time1)

    time1 = time()
    selectionSort(temp_arr4)
    time2 = time()
    results.append(time2 - time1)

    time1 = time()
    selectionSort(temp_arr5)
    time2 = time()
    results.append(time2 - time1)

    return results

def insertionTest(opc: int) -> list:
    results = []

    match opc:
        case 1:
            temp_arr1, temp_arr2, temp_arr3, temp_arr4, temp_arr5 = loadAleatory()
        case 2:
            temp_arr1, temp_arr2, temp_arr3, temp_arr4, temp_arr5 = loadAscending()
        case 3:
            temp_arr1, temp_arr2, temp_arr3, temp_arr4, temp_arr5 = loadDescending()
    
    time1 = time()
    insertionSort(temp_arr1)
    time2 = time()
    results.append(time2 - time1)

    time1 = time()
    insertionSort(temp_arr2)
    time2 = time()
    results.append(time2 - time1)

    time1 = time()
    insertionSort(temp_arr3)
    time2 = time()
    results.append(time2 - time1)

    time1 = time()
    insertionSort(temp_arr4)
    time2 = time()
    results.append(time2 - time1)

    time1 = time()
    insertionSort(temp_arr5)
    time2 = time()
    results.append(time2 - time1)

    return results

def bubbleTest(opc: int) -> list:
    results = []

    match opc:
        case 1:
            temp_arr1, temp_arr2, temp_arr3, temp_arr4, temp_arr5 = loadAleatory()
        case 2:
            temp_arr1, temp_arr2, temp_arr3, temp_arr4, temp_arr5 = loadAscending()
        case 3:
            temp_arr1, temp_arr2, temp_arr3, temp_arr4, temp_arr5 = loadDescending()
    
    time1 = time()
    bubbleSort(temp_arr1)
    time2 = time()
    results.append(time2 - time1)

    time1 = time()
    bubbleSort(temp_arr2)
    time2 = time()
    results.append(time2 - time1)

    time1 = time()
    bubbleSort(temp_arr3)
    time2 = time()
    results.append(time2 - time1)

    time1 = time()
    bubbleSort(temp_arr4)
    time2 = time()
    results.append(time2 - time1)

    time1 = time()
    bubbleSort(temp_arr5)
    time2 = time()
    results.append(time2 - time1)

    return results

def heapTest(opc: int) -> list:
    results = []

    match opc:
        case 1:
            temp_arr1, temp_arr2, temp_arr3, temp_arr4, temp_arr5 = loadAleatory()
        case 2:
            temp_arr1, temp_arr2, temp_arr3, temp_arr4, temp_arr5 = loadAscending()
        case 3:
            temp_arr1, temp_arr2, temp_arr3, temp_arr4, temp_arr5 = loadDescending()
    
    time1 = time()
    heapSort(temp_arr1)
    time2 = time()
    results.append(time2 - time1)

    time1 = time()
    heapSort(temp_arr2)
    time2 = time()
    results.append(time2 - time1)

    time1 = time()
    heapSort(temp_arr3)
    time2 = time()
    results.append(time2 - time1)

    time1 = time()
    heapSort(temp_arr4)
    time2 = time()
    results.append(time2 - time1)

    time1 = time()
    heapSort(temp_arr5)
    time2 = time()
    results.append(time2 - time1)

    return results

def quickTest(opc: int) -> list:
    sys.setrecursionlimit(500000)
    
    results = []

    match opc:
        case 1:
            temp_arr1, temp_arr2, temp_arr3, temp_arr4, temp_arr5 = loadAleatory()
        case 2:
            temp_arr1, temp_arr2, temp_arr3, temp_arr4, temp_arr5 = loadAscending()
        case 3:
            temp_arr1, temp_arr2, temp_arr3, temp_arr4, temp_arr5 = loadDescending()
    
    time1 = time()
    quickSort(temp_arr1)
    time2 = time()
    results.append(time2 - time1)

    time1 = time()
    quickSort(temp_arr2)
    time2 = time()
    results.append(time2 - time1)

    time1 = time()
    quickSort(temp_arr3)
    time2 = time()
    results.append(time2 - time1)

    time1 = time()
    quickSort(temp_arr4)
    time2 = time()
    results.append(time2 - time1)

    time1 = time()
    quickSort(temp_arr5)
    time2 = time()
    results.append(time2 - time1)

    return results
