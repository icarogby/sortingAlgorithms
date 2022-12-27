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
            file = "descending"
    
    try:
        file1 = open(f"test cases\\512{file}.txt")
        file2 = open(f"test cases\\1024{file}.txt")
        file3 = open(f"test cases\\2048{file}.txt")
        file4 = open(f"test cases\\4096{file}.txt")
        file5 = open(f"test cases\\8192{file}.txt")
        file6 = open(f"test cases\\16384{file}.txt")

        arr1 = []
        arr2 = []
        arr3 = []
        arr4 = []
        arr5 = []
        arr6 = []

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

        for line in file6:
            arr6.append(int(line))

        sets.append(arr1)
        sets.append(arr2)
        sets.append(arr3)
        sets.append(arr4)
        sets.append(arr5)
        sets.append(arr6)
    
    except:
        print("Fail.")
    else:
        file1.close()
        file2.close()
        file3.close()
        file4.close()
        file5.close()
        file6.close()

    return sets

def timeTest(algorith: Callable[[list], list], opc: int) -> list:
    sys.setrecursionlimit(50000)

    results = []
    sets = loadSets(opc)

    for i in range(6):
        time1 = time()
        algorith(sets[i])
        time2 = time()
        results.append(time2 - time1)

    return results

def mediaTimeTest(algorith: Callable[[list], list], opc: int) -> list:
    results = [0, 0, 0, 0, 0, 0]

    for i in range(3):
        temp = timeTest(algorith, opc)

        for j in range(6):
            results[j] = results[j] + temp[j]

    for j in range(6):
        results[j] = results[j]/3

    return results
