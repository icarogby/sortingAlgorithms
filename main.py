from tests import *
from algorithms import *
from save import *

def main():
    opc = int(input("1) Aleatory\n2) Ascending\n3) Descending\n\nSelect: "))

    selectionY = mediaTimeTest(selectionSort, opc)
    insertionY = mediaTimeTest(insertionSort, opc)
    bubbleY    = mediaTimeTest(bubbleSort, opc)
    mergeY     = mediaTimeTest(mergeSort, opc)
    heapY      = mediaTimeTest(heapSort, opc)
    quickY     = mediaTimeTest(quickSort, opc)

    saveCSV(selectionY, insertionY, bubbleY, mergeY, heapY, quickY, opc)
    savePNG(selectionY, insertionY, bubbleY, mergeY, heapY, quickY, opc)
    
if __name__ == "__main__":
    main()
