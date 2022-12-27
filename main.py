from tests import *
from algorithms import *

from matplotlib import pyplot as plt

def main():
    opc = int(input("1) Aleatory\n2) Ascending\n3) Descending\n\nSelect: "))

    x = [1, 2, 3, 4, 5, 6]

    selectionY = mediaTimeTest(selectionSort, opc)
    insertionY = mediaTimeTest(insertionSort, opc)
    bubleY = mediaTimeTest(bubbleSort, opc)
    mergeY = mediaTimeTest(mergeSort, opc)
    heapY = mediaTimeTest(heapSort, opc)
    quickY = mediaTimeTest(quickSort, opc)

    plt.plot(x, selectionY, color = 'r', label = "Selection Sort")
    plt.plot(x, insertionY, color = 'b', label = "Insertion Sort")
    plt.plot(x, bubleY, color = 'y', label = "Bubble Sort")
    plt.plot(x, mergeY, color = 'c', label = "Merge Sort")
    plt.plot(x, heapY, color = 'm', label = "Heap Sort")
    plt.plot(x, quickY, color = 'g', label = "Quick Sort")

    plt.title("Sorting Algorithms")
    plt.xlabel("Number of Elements")
    plt.ylabel("Media of time (seconds)")

    plt.grid(True)
    plt.yscale("log")
    plt.legend()
    plt.savefig("plottest2ale.png")
    
if __name__ == "__main__":
    main()
