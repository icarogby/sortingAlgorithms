from tests import *

from matplotlib import pyplot as plt

def test(funcao, o):
    results4 = [0, 0, 0, 0]

    for i in range(3):
        temp = funcao(o)

        for j in range(4):
            results4[j] = results4[j] + temp[j]

    for j in range(4):
        results4[j] = results4[j]/3

    return results4

def main():
    opc = int(input("Select: "))

    x = [1, 2, 3, 4, ]

    listatest = test(selectionTest, opc)

    # Results1 = selectionTest(o)
    # Results2 = insertionTest(o)
    # Results3 = bubbleTest(o)


    # Results5 = heapTest(o)
    # Results6 = quickTest(o)

    # plt.plot(x, Results1)
    # plt.plot(x, Results2)
    # plt.plot(x, Results3)
    plt.plot(x, listatest)
    # plt.plot(x, Results5)
    # plt.plot(x, Results6)

    plt.show()

if __name__ == "__main__":
    main()
