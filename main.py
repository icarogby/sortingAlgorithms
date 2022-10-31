from tests import *

from matplotlib import pyplot as plt


def main():
    x = [1, 2, 3, 4, ]

    Results1 = selectionTest(1)
    Results2 = insertionTest(1)
    Results3 = bubbleTest(1)
    Results4 = mergeTest(1)
    Results5 = heapTest(1)
    Results6 = quickTest(1)

    plt.plot(x, Results1)
    plt.plot(x, Results2)
    plt.plot(x, Results3)
    plt.plot(x, Results4)
    plt.plot(x, Results5)
    plt.plot(x, Results6)

    plt.show()

if __name__ == "__main__":
    main()
