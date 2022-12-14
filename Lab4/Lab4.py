import math
import os


def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

def combination(m, n):
    return math.factorial(m) / (math.factorial(n) * math.factorial(m-n))


def ShoesTask(black, brown, red, blue):         #(40, 26, 22, 12)
    return round((red + blue) / (black + brown + red + blue), 3)


def BankTask(q1, q2):                   #(10, 8)
    return round((1 - (combination(q2, 1) / combination(q1, 2))), 3)


def CompanyTask(a1, a2, a3):            #(10, 2, 3)
    return round(1 - (combination(a1-a2, a3) / combination(a1, a3)), 3)


def MinimarketTask(p1, p2, p3, p4):     #(0.15, 0.25, 0.2, 0.1)
    return round((1 - (p1 + p2 + p3 + p4)), 3)


def TrainTask(m, n):                    #(120, 80)
    f = combination(n, 2)
    s = combination(m, 2)
    return round((f / s), 3)


def ToolTask(x, y):                     #6
    return round(x * y, 3)


def GroupTask():                        #7
    p = 3/10 * 20/20 * 19/19 * 18/18 +\
        4/10 * 16/20 * 15/19 * 14/18 +\
        2/10 * 10/20 * 9/19 * 8/18 +\
        1/10 * 5/20 * 4/19 * 3/18
    positiv = round(3/10 * 1/p, 3)
    negative = round(1/10 * 5/20 * 4/19 * 3/18 / p, 3)
    rez = [positiv, negative]
    return rez

def ModernToolsTask(p1, p2, p3):        #8
    return round(0.4 * p1 + 0.3 * p2 + 0.3 * p3, 3)


def DoctorkaTask(p1, p2, p3, el1, el2, el3):        #9
    percent = p2 * el2
    amount = p1 * el1 + p2 * el2 + p3 * el3
    return round(percent / amount, 3)


def PowerfulEngineerTask(p1, p2, el1, el2):         #10
    value = p1 * el1
    general = p1 * el1 + p2 * el2
    return round(1 - value / general, 3)


rez7 = []
rez1 = ShoesTask(40, 26, 22, 12)
rez2 = BankTask(10, 8)
rez3 = CompanyTask(10, 2, 3)
rez4 = MinimarketTask(0.15, 0.25, 0.2, 0.1)
rez5 = TrainTask(120, 80)
rez6 = ToolTask(0.9, 0.8)
rez7 = GroupTask()
rez8 = ModernToolsTask(0.9, 0.95, 0.95)
rez9 = DoctorkaTask(0.4, 0.3, 0.3, 0.8, 0.7, 0.85)
rez10 = PowerfulEngineerTask(0.3, 0.7, 0.9, 0.8)


file = "Lab4.txt"
if os.path.exists(file):
    os.remove(file)


f = open(file, "a")
f.write(f"Task 1:\t\t{rez1}\n")
f.write(f"Task 2:\t\t{rez2}\n")
f.write(f"Task 3:\t\t{rez3}\n")
f.write(f"Task 4:\t\t{rez4}\n")
f.write(f"Task 5:\t\t{rez5}\n")
f.write(f"Task 6:\t\t{rez6}\n")
f.write(f"Task 7:\texcellent student:\t{rez7[0]}\tbad student:\t{rez7[1]}\n")
f.write(f"Task 8:\t\t{rez8}\n")
f.write(f"Task 9:\t\t{rez9}\n")
f.write(f"Task 10:\t\t{rez10}\n")
f.close()


print(f"\n\n1. В магазин надійшла партія взуття одного фасону і розміру, але різного кольору. Партія містить 40\nпарчорного кольору, 26 – коричневого, 22 – червоного і 12 пар синього. Коробки із взуттям виявились невідсортовані за кольором.\nЯка ймовірність того, що навмання взята коробка виявиться із взуттям червоного або синього кольору?\n{rez1*100}%\n")
print(f"2. У банку працює 10 співробітників, 8 з яких є консультантами. Знайти ймовірність того, що серед\nнавмання вибраних двох співробітників, хоча б один буде консультантом.\n{rez2*100}%\n")
print(f"3. В компанії працює 10 менеджерів, серед яких двоє – родичі. Жеребкуванням вибирають трьох. Знайдіть\nймовірність того, що серед вибраних фахівців буде принаймні один із родичів.\n{rez3*100}%\n")
print(f"4. До мінімаркету з п’ятьма відділами прибував товар до одного з них. Ймовірність призначення товару для\nпершого відділу р1=0,15, для другого р2=0,25, для третього р3=0,2, а для четвертого р4=0,1. Знайти\nймовірність р5 того, що цей товар призначений для п’ятого відділу.\n{rez4*100}%\n")
print(f"5. У графіку руху потягів на дільниці є 120 колій для вантажних потягів. З цієї дільниці на станцію\nприбувають за розбіркою 80 потягів. Знайти ймовірність прибуття двох розбіркових потягів по двох сусідніх\nколіях.\n{rez5*100}%\n")
print(f"6. Ймовірність виготовлення стандартного виробу даним станком дорівнює 0,9. Ймовірність появи виробу\nпершого ґатунку серед стандартних виробів становить 0,8. Визначити ймовірність виготовлення виробу\nпершого ґатунку даним станком.\n{rez6*100}%\n")
print(f"7. В групі з 10 студентів, які прийшли на екзамен, 3 підготовлені відмінно, 4 – добре, 2 – посередньо і 1 \nпогано. В екзаменаційних білетах є 20 питань. Студент, який підготовлений відмінно може відповісти на всі\n20 питань, який підготовлений добре – на 16, посередньо – на 10, погано – на 5. Визваний навмання студент\nвідповів на три довільно заданих питання. Знайти ймовірність того, що цей студент підготовлений:\nа)відмінно:\t{rez7[0]}\t\t\tб) погано:\t{rez7[1]*100}%\n")
print(f"8. На трьох автоматизованих лініях виготовляють однакові деталі, причому 40% - на першій лінії, 30% - на\nдругій та 30% - на третій. Ймовірність виготовлення стандартної деталі для цих ліній становить відповідно\n0,9, 0,95 та 0,95. Виготовлені деталі надходять на склад. Яка ймовірність того, що навмання взята деталь\nстандартна?\n{rez8*100}%\n")
print(f"9. У лікарню поступають (в середньому) 40% хворих на пневмонію, 30% -на перитоніт та 30% хворих на\nангіну. Ймовірність повного одужання від пневмонії – 0,8; від перитоніту – 0,7 та ангіни – 0,85. Виписано\nхворого, який повністю одужав. Яка ймовірність того, що він був хворий на перитоніт?\n{rez9*100}%\n")
print(f"10. 30% приладів збирає фахівець високої кваліфікації і 70% середньої. Надійність роботи приладу,\nзібраного фахівцем високої кваліфікації 0,9, надійність приладу, зібраного фахівцем середньої кваліфікації\n0,8. Взятий прилад виявився надійним. Визначити ймовірність того, що він зібраний фахівцем високої\nкваліфікації.\n{rez10*100}%\n")