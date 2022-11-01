from time import time
import sys
from typing import Callable

def loadSets(opc: int) -> list[list]:
    sets = []

    match opc:
        case 1:
            file = "aleatory"
        case 2:
            file = "ascending"
        case 3:
            file = "decending"
    
    try:
        file1 = open(f"test cases\\160{file}.txt")
        file2 = open(f"test cases\\800{file}.txt")
        file3 = open(f"test cases\\4000{file}.txt")
        file4 = open(f"test cases\\20000{file}.txt")

        arr1 = []
        arr2 = []
        arr3 = []
        arr4 = []

        for line in file1:
            arr1.append(int(line))

        for line in file2:
            arr2.append(int(line))

        for line in file3:
            arr3.append(int(line))

        for line in file4:
            arr4.append(int(line))

        sets.append(arr1)
        sets.append(arr2)
        sets.append(arr3)
        sets.append(arr4)
    
    except:
        print("Fail.")
    else:
        file1.close()
        file2.close()
        file3.close()
        file4.close()

    return sets

def timeTest(algorith: Callable[[list], list], opc: int) -> list:
    sys.setrecursionlimit(50000)

    results = []
    sets = loadSets(opc)
    
    for i in range(4):
        time1 = time()
        algorith(sets[i])
        time2 = time()
        results.append(time2 - time1)

    return results

def mediaTimeTest(algorith: Callable[[list], list], opc: int) -> list:
    results = [0, 0, 0, 0]

    for i in range(3):
        temp = timeTest(algorith, opc)

        for j in range(4):
            results[j] = results[j] + temp[j]

    for j in range(4):
        results[j] = results[j]/3

    return results
