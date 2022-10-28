import math
import math as m
import os
from pylab import *
from sympy import *

def read(txt):
    f = open(txt, 'r')
    return [int(line.strip()) for line in f]

def DeleteFirst(list):
    list.remove(list[0])

def SaveFile(list):
    file = str(len(list)) + ".txt"
    if os.path.exists(file):
        os.remove(file)

def SaveList(list):
    file = str(len(list)) + ".txt"
    f = open(file, "a")
    for i in list:
        f.write(str(i) + ",  ")
    f.write("\n")
    f.close()

def OutputFile(file):
    f = open(file, "r")
    print(f.read())
    f.close()

def bubble_sort(list):
    for run in range(len(list)-1):
        for i in range(len(list)-1-run):
            if list[i]> list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
    return list

def PercentileOrQuertile(percentile,list):
    q = ((percentile / 100) * (len(list) + 1))
    qRounded = int(q)
    value = list[qRounded-1]
    return value + (percentile / 100) * (list[qRounded] - list[qRounded-1])
def Average(list):
    average = 0
    for i in list:
        average += i
    return average / len(list)

def Dispercian(list, average):
    up = 0;
    for i in list:
        up += (i - average) ** 2
    return up / (len(list) - 1)

def AverageSquare(disp):
    return math.sqrt(disp)


def TeacherTask(average, list):
    first = np.array([[100,1],
                      [average,1]])
    second = np.array([100,95])
    x = np.linalg.solve(first,second)
    a = round(x[0], 3)
    b = round(x[1], 3)

    newlist = []
    for i in list:
        newlist.append(round((i*a + b), 3))

    return newlist


def StemLeafDiagram(list):
    numerator = 0
    curMin = 0
    curMax = 10
    line = ""
    listStr = []
    for i in range(11):
        for j in list:
            if (j < curMax and j >= curMin):
                line += str(int(j%10)) + ",  "
        listStr.append(line)
        line = ""
        curMin += 10
        curMax += 10

    file = str(len(list)) + ".txt"
    f = open(file, "a")
    f.write("Diagrama Stem-Leaf:\n")
    for i in listStr:
        f.write(f"{numerator}\t|  {i}\n")
        numerator += 1
    f.close()


def BuildBoxDiagram(list, q1, q3):
    fig, ax = plt.subplots()
    q2 = PercentileOrQuertile(50, list)
    boxes = [
        {
            'label': "Box diagram",
            'Xmin': list[0],
            'q1': q1,
            'q2': q2,
            'q3': q3,
            'Xmax': list[len(list)-1],
            'fliers': []
        }
    ]
    ax.bxp(boxes, showfliers=False)
    plt.show()


def TaskWithList(list):
    q1 = PercentileOrQuertile(25, list)
    q3 = PercentileOrQuertile(75, list)
    p90 = PercentileOrQuertile(90,list)
    average = Average(list)
    disp = Dispercian(list, average)
    aveSquare = AverageSquare(disp)
    teacherTask = TeacherTask(average, list)
    file = str(len(list)) + ".txt"

    SaveList(list)
    f = open(file, "a")
    f.write(f"q1:\t\t\t{q1}\nq3:\t\t\t{q3}\np90:\t\t{p90}\nAverage:\t{average}\nDispercian:\t\t{disp}\nAverage square:\t{round(aveSquare, 3)}\n")
    f.close()
    SaveList(teacherTask)

    StemLeafDiagram(list)

    OutputFile(file)

    BuildBoxDiagram(list, q1, q3)
    print("\n\n")


list10 = read('input_10.txt')
list100 = read('input_100.txt')

DeleteFirst(list10)
DeleteFirst(list100)

list10 = bubble_sort(list10)
list100 = bubble_sort(list100)

SaveFile(list10)
SaveFile(list100)

TaskWithList(list10)
TaskWithList(list100)