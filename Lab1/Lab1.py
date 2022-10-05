import math

import delete as d
import read as r
import save as s
import matplotlib.pyplot as plt

import write as w

def bubble_sort(list):
    for run in range(len(list)-1):
        for i in range(len(list)-1-run):
            if list[i]> list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
    return list



def CreateDifference(liststandart):
    list = []
    max = len(liststandart)
    counter: int = 0
    i: int = 0
    while i < len(liststandart):
        if max > liststandart[i]:
            counter +=1
            i+=1
        else:
            if counter > 0:
                for j in range(counter):
                    list.append(f'{str(max - len(liststandart))} - {str(max)}')
            counter = 0
            max = max + 10
        if i == len(liststandart):
            list.append(f'{str(max - len(liststandart))} - {str(max)}')
    return list


def CreateTable10(list):
    cumulative = 0

    print("Amount      Frequency   Cumulative\n--------------------------------")

    for i in list:
        cumulative += i[1]
        print(f"{i[0]}\t\t\t{i[1]}\t\t\t{cumulative}")

def Task2(list, default):
    print("Moda:")
    max: int = 1
    for j in list:
        if (max < j[1]):
            max = j[1]
    for j in list:
        if (max == j[1]):
            print(f"Element: {j[0]}     Frequency: {max}")

    #Mediana
    if (len(default) % 2 == 0):
        mid = int(len(default) / 2)
        x = (abs(default[mid-1] + default[mid]) / 2)
        print(f"Mediana: {x}")
    else:
        mid = int(len(default) / 2)
        x = default[mid]
        print(f"Mediana: {x}")

    for i in list:
        s.save(str(len(list)) + ".txt", f"Number: {i[0]}\t\tAmount: {i[1]}\n")


    #Save moda and mediana
    for j in list:
        if (max == j[1]):
            s.save(str(len(list)) + ".txt", f"Moda: {j[0]}\t\tFrequncy: {max}\n")
    s.save(str(len(list)) + ".txt", f"Mediana: {x}\n")


def Upside(list, average):
    up = 0
    for i in list:
        up += i[1] * pow(i[0] - average, 2)
    return up


def Task3(list):
    up = 0
    for i in list:
        up += i[0] * i[1]

    down = 0
    for i in list:
        down += i[1]

    #down -= 1

    average = up / down

    Dispercion = Upside(list, average) / down
    print(f"Dispertion: {Dispercion}")
    print(f"Average square: {math.sqrt(Dispercion)}")

    s.save(str(len(list)) + ".txt", f"Dispertion: {Dispercion}\nAverage square: {math.sqrt(Dispercion)}\n")


def Frequency(list, freq):
    i: int = 0
    k: int = 0
    while (i < len(list)):
        counter: int = 0
        j: int = i
        while (j < len(list)):
            if (i == len(list)-1):
                counter += 1
                i = len(list)
                break
            if (list[i] != list[j]):
                i = j
                break
            counter += 1
            j += 1
        #freq[k][1] = [list[i]][counter]
        freq.insert(k, [list[i-1],counter])
        k += 1
    return freq


def Task4(list):
    plt.hist(list, bins = 200)
    plt.ylabel("Frequency")
    plt.xlabel("Amount")
    plt.title("Histogram")
    plt.show()


list10 = r.read('input_10.txt')
list100 = r.read('input_100.txt')
list1000 = r.read('input_1000.txt')


d.DeleteFirst(list10)
d.DeleteFirst(list100)
d.DeleteFirst(list1000)


list10 = bubble_sort(list10)
list100 = bubble_sort(list100)
list1000 = bubble_sort(list1000)


freq10 = [[],[]]
freq100 = [[],[]]
freq1000 = [[],[]]


freq10 = Frequency(list10, freq10)
freq100 = Frequency(list100, freq100)
freq1000 = Frequency(list1000, freq1000)


for i in range(2):
    freq10.pop()
    freq100.pop()
    freq1000.pop()


CreateTable10(freq10)
CreateTable10(freq100)
CreateTable10(freq1000)
print("\n\n\n")


print("\t\tFor 10 elements")
Task2(freq10, list10)
print("\n\t\tFor 100 elements")
Task2(freq100, list100)
print("\n\t\tFor 1000 elements")
Task2(freq1000, list1000)


print("\n\n\t\tFor 10 elements")
Task3(freq10)
print("\t\tFor 100 elements")
Task3(freq100)
print("\t\tFor 1000 elements")
Task3(freq1000)

Task4(list10)
Task4(list100)
Task4(list1000)
