from matplotlib import pyplot as plt

def saveCSV(list1, list2, list3, list4, list5, list6, opc):
    try:
        if opc == 1:
            file = open(f'results\\aleatory.csv', 'w')
        elif opc == 2:
            file = open(f'results\\ascending.csv', 'w')
        elif opc == 3:
            file = open(f'results\\descending.csv', 'w')

        file.write("Algorithm/Number of Elements, 512, 1024, 2048, 4096, 8192, 16384\n")
        
        file.write(f"Selection Sort, ")
        for i in range(len(list1)):
            if (i == len(list1) - 1):
                file.write(f"{list1[i]}\n")
            else:
                file.write(f"{list1[i]}, ")

        file.write(f"Insertion Sort, ")
        for i in range(len(list2)):
            if (i == len(list2) - 1):
                file.write(f"{list2[i]}\n")
            else:
                file.write(f"{list2[i]}, ")

        file.write(f"Bubble Sort, ")
        for i in range(len(list3)):
            if (i == len(list3) - 1):
                file.write(f"{list3[i]}\n")
            else:
                file.write(f"{list3[i]}, ")

        file.write(f"Merge Sort, ")
        for i in range(len(list4)):
            if (i == len(list4) - 1):
                file.write(f"{list4[i]}\n")
            else:
                file.write(f"{list4[i]}, ")

        file.write(f"Heap Sort, ")
        for i in range(len(list5)):
            if (i == len(list5) - 1):
                file.write(f"{list5[i]}\n")
            else:
                file.write(f"{list5[i]}, ")
        
        file.write(f"Quick Sort, ")
        for i in range(len(list6)):
            if (i == len(list6) - 1):
                file.write(f"{list6[i]}\n")
            else:
                file.write(f"{list6[i]}, ") 
    except:
        print("file fail.")
    else:
        file.close()

def savePNG(selectionY, insertionY, bubbleY, mergeY, heapY, quickY, opc):
    x = [512, 1024, 2048, 4096, 8192, 16384]
    
    plt.plot(x, selectionY, marker='o', color = 'r', label = "Selection Sort")
    plt.plot(x, insertionY, marker='o', color = 'b', label = "Insertion Sort")
    plt.plot(x, bubbleY, marker='o', color = 'y', label = "Bubble Sort")
    plt.plot(x, mergeY, marker='o', color = 'c', label = "Merge Sort")
    plt.plot(x, heapY, marker='o', color = 'm', label = "Heap Sort")
    plt.plot(x, quickY, marker='o', color = 'g', label = "Quick Sort")

    plt.title("Sorting Algorithms")
    plt.xlabel("Number of Elements")
    plt.ylabel("Media of time (seconds)")

    plt.grid(True)
    plt.xscale("log")
    plt.yscale("log")
    plt.legend()

    if opc == 1:
        plt.savefig("results\\aleatory.png")
    elif opc == 2:
        plt.savefig("results\\ascending.png")
    elif opc == 3:
        plt.savefig("results\\descending.png")
