from tests import *
from algorithms import *

from matplotlib import pyplot as plt

def main():
    opc = int(input("Select: "))

    x = [1, 2, 3, 4]

    y = mediaTimeTest(selectionSort, opc)

    # listatest = test(selectionTest, opc)

    # Results1 = selectionTest(o)
    # Results2 = insertionTest(o)
    # Results3 = bubbleTest(o)


    # Results5 = heapTest(o)
    # Results6 = quickTest(o)

    # plt.plot(x, Results1)
    # plt.plot(x, Results2)
    # plt.plot(x, Results3)
    # plt.plot(x, listatest)
    # plt.plot(x, Results5)
    plt.plot(x, y)

    plt.show()

if __name__ == "__main__":
    main()
