import math
import math as m
import os
import matplotlib.pyplot as plt
from pylab import *
from sympy import *



def read(txt):
    f = open(txt, 'r')
    return [line.strip() for line in f]

def OutputFile(file):
    f = open(file, "r")
    print(f.read())
    f.close()

def SaveFile(list):
    file = str(len(list)) + ".txt"
    if os.path.exists(file):
        os.remove(file)

def SaveTable(x, y):
    file = str(len(x)) + ".txt"
    f = open(file, "a")
    for i in range(12):
        f.write(f"x:\t{x[i]}\t\ty:\t{y[i]}\n")
    f.close()

def SplitFiles(list, x, y):
    for i in list:
        a = i.split("\t")
        y.append(float(a[0]))
        x.append(float(a[1]))

def BuildScatter(x,y):
    plt.scatter(x, y)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

def Average(list):
    average = 0
    for i in list:
        average += i
    return average / len(list)

def Dispercian(list, average):
    up = 0
    for i in list:
        up += (i - average) ** 2
    return up / (len(list) - 1)
def Covariacion(x, y, aveX, aveY):
    cov = 0
    for i in range(len(x)-1):
        cov += (x[i] - aveX)* (y[i] - aveY)
    return cov/len(x)

def Koeficient(cov, disp):
    return cov / disp

def Corelation(x, y, aveX, aveY, cov, k):
    dispX = Dispercian(x, aveX)
    dispY = Dispercian(y, aveY)
    return cov / sqrt(dispX * dispY)

def CheckRegression(corelation):
    if corelation == -1:
        return "Line on points and falling"
    elif corelation > -1 and corelation < 0:
        return "Line almost on points and falling"
    elif corelation > 0 and corelation < 1:
        return "Line almost on points and growing"
    elif corelation == 1:
        return "Line on points and growing"
    else: return "Line miss all points"

def Trend(corelation):
    if corelation > 0:
        return "Trend is positive"
    elif corelation < 0:
        return "Trend is positive"
    else: return "Trend is missing"

def TaskWithList(list):
    x = []
    y = []
    SplitFiles(list, x, y)
    file = str(len(x)) + ".txt"

    aveX = round(Average(x), 3)
    aveY = round(Average(y), 3)

    covariation = round(Covariacion(x, y, aveX, aveY), 3)
    disp = Dispercian(x, aveX)

    Center = [aveX, aveY]
    k = round(Koeficient(covariation, disp), 3)
    b = round(aveY - k * aveX, 3)
    newY = [round(k * i + b, 3) for i in x]
    corelation = round(Corelation(x, y, aveX, aveY, covariation, k), 3)
    trend = Trend(corelation)
    checkrezult = CheckRegression(corelation)

    #ADD Save
    SaveTable(x, y)

    f = open(file, "a")
    f.write(f"Center is:\t{Center}\n")
    f.write(f"Covariation:\t{covariation}\n")
    f.write(f"Koeficient:\t{k}\n")
    f.write(f"Regression line:\ty = {k} * x + {b}\n")
    f.write(f"\t\t\tNew Y:\n")
    f.close()

    SaveTable(x, newY)

    f = open(file, "a")
    f.write(f"Corelation koeficient:\t{corelation}\n")
    f.write(f"Trend conclusion:\t{trend}\n")
    f.write(f"Conclusion:\t{checkrezult}")
    f.close()
    print("\n")

    #ADD Readfile
    OutputFile(file)
    BuildScatter(x, y)




list10 = read("input_10.txt")
list100 = read("input_100.txt")

list10.remove(list10[0])
list100.remove(list100[0])

SaveFile(list10)
SaveFile(list100)


TaskWithList(list10)
TaskWithList(list100)