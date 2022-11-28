import math
import os
from decimal import Decimal


def OutputFile():
    f = open("./output/output.txt", "r")
    print(f.read())
    f.close()


def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


def gauss(x):
    return (1 / math.sqrt(2 * math.pi)) * (math.e ** (-((x ** 2) / 2)))


def laplas(p, n, m):
    q = 1 - p
    np = n * p
    npq = np * q
    sqrtnpq = math.sqrt(npq)
    x = (m - np) / sqrtnpq
    return gauss(x) / sqrtnpq


def combination(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))


def bernulli(n,k,p):
    return combination(n,k)*(p**k)*((1-p)**(n-k))


def bernulliBetween(n,m1,m2,p):
    sum = 0
    for i in range(m1, m2):
        sum += bernulli(n, i, p)
    return sum


def task1():        # 1
    probability = 0.2
    fromThree = 3
    toFive = 5
    return bernulli(toFive,fromThree,probability)


def task2():        # 2
    probability = 0.8
    a = 4
    b = 5
    general = 5
    result = []
    result.append(bernulli(general, a, probability))
    result.append(bernulli(general, b, probability) + bernulli(general, a, probability))
    return result


def task3():        # 3
    probability = 0.2
    general = 400
    item = 80
    return laplas(probability, general, item)


def task4():        # 4
    general = 100_000
    probability = 0.0001
    false = 5
    return laplas(probability, general, false)


def task5():        # 5
    probability = 0.4
    general = 600
    min = 228
    max = 252
    answer = 0
    for m in range(min, max):
        answer += laplas(probability, general, m)
    return answer


#q = 1 - p
def task6():        # 6
    probability = 0.04
    general = 100
    high = probability * general + probability
    return high


def task7():        # 7
    general = 4000
    min = 1
    max = 170
    probability = 0.04
    answer = 0
    for m in range(min, max):
        answer += laplas(probability, general, m)
    return answer


def task8():        # 8
    general = 10_000
    amount = 5000
    probability = 0.5
    return laplas(probability, general, amount)


def task9():        # 9
    general = 1000
    false = 5
    probability = 0.002
    return laplas(probability, general, false)


def task10():       # 10
    probability = 0.03
    general = 150
    high = probability * general + probability
    return high


def check_results(number, result):
    task1_analytics = 0.0511
    task2_analytics = [0.4096, 0.73728]
    task3_analytics = 0.049
    task4_analytics = 0.0375
    task5_analytics = 0.683
    task6_analytics = 4
    task7_analytics = 0.789
    task8_analytics = 0.00798
    task9_analytics = 0.0361
    task10_analytics = 4
    if number == 1:
        return result - task1_analytics
    if number == 2:
        return result[0] - task2_analytics[0] + result[1] - task2_analytics[1]
    if number == 3:
        return result - task3_analytics
    if number == 4:
        return result - task4_analytics
    if number == 5:
        return result - task5_analytics
    if number == 6:
        return result - task6_analytics
    if number == 7:
        return result - task7_analytics
    if number == 8:
        return result - task8_analytics
    if number == 9:
        return result - task9_analytics
    if number == 10:
        return result - task10_analytics


def print_results():
    check1 = 0.051
    check2 = [0.4096, 0.73728]
    check3 = 0.0498
    check4 = 0.0375
    check5 = 0.6826
    check6 = 4
    check7 = 0.7881
    check8 = 0.007978
    check9 = 0.0361
    check10 = 4
    file = open("./output/output.txt", 'w')
    file.write("№\t| Result\t\t\t\t\t\t | Calculations\t\t | Deviation\n")
    file.write("1.\t| " + str(task1()) + "\t\t\t | " + str(check1) + "\t\t\t | " + str(check_results(1, task1())) + "\n")
    file.write("2.\t| " + str(task2()) + "\t | " + str(check2) + " | " + str(check_results(2, task2())) + "\n")
    file.write("3.\t| " + str(task3()) + "\t\t\t | " + str(check3) + "\t\t\t | " + str(check_results(3, task3())) + "\n")
    file.write("4.\t| " + str(task4()) + "\t\t\t | " + str(check4) + "\t\t\t | " + str(check_results(4, task4())) + "\n")
    file.write("5.\t| " + str(task5()) + "\t\t\t | " + str(check5) + "\t\t\t | " + str(check_results(5, task5())) + "\n")
    file.write("6.\t| " + str(task6()) + "\t\t\t\t\t\t\t | " + str(check6) + "\t\t\t\t | " + str(check_results(6, task6())) + "\n")
    file.write("7.\t| " + str(task7()) + "\t\t\t\t | " + str(check7) + "\t\t\t | " + str(check_results(7, task7())) + "\n")
    file.write("8.\t| " + str(task8()) + "\t\t\t | " + str(check8) + "\t\t\t | " + str(check_results(8, task8())) + "\n")
    file.write("9.\t| " + str(task9()) + "\t\t\t | " + str(check9) + "\t\t\t | " + str(check_results(9, task9())) + "\n")
    file.write("10.\t| " + str(int(task10())) + "\t\t\t\t\t\t\t\t | " + str(check10) + "\t\t\t\t | " + str(check_results(10, int(task10()))) + "\n")


print("Task 1:\nЙмовірність знаходження в кожному прибулому потязі вагонів на дане призначення 0,2.\nВизначити ймовірність того, що в трьох із п’яти потягів, які прибувають протягом однієї години, будуть вагони на дане призначення.\n")
print("Task 2:\nЗнайти ймовірність того, що в п’яти незалежних випробуваннях подія А відбудеться:\nа) рівно 4 рази; б) не менше 4 разів, якщо в кожному випробуванні ймовірність появи події становить 0,8.\n")
print("Task 3:\nНа кондитерській фабриці 20% всіх цукерок складають льодяники.\nЗнайти ймовірність того, що серед 400 вибраних навмання цукерок буде рівно 80 льодяників.\n")
print("Task 4:\nНа автомобільному заводі у звичному режимі роботи з конвеєра сходить 100000 автомобілів.\nЙмовірність бракованого автомобіля дорівнює 0,0001.\nЗнайти ймовірність того, що з конвеєра зійшло 5 бракованих автомобілів.\n")
print("Task 5:\nЙмовірність того, що пара взуття, яка взята навмання з виготовленої партії виявиться вищого ґатунку дорівнює 0,4.\nЧому дорівнює ймовірність того, що серед 600 пар, які поступили на контроль, виявиться від 228 до 252 пар взуття вищого ґатунку?\n")
print("Task 6:\nБанк обслуговує 100 клієнтів, від кожного з яких може надійти вимога на проведення фінансової операції на наступний день з ймовірністю 0,4.\nЗнайти найімовірніше число вимог клієнтів кожного дня.\n")
print("Task 7:\nЗавод випускає в середньому 4% нестандартних виробів.\nЯка ймовірність того, що число нестандартних виробів у партії з 4000 штук не більше 170?\n")
print("Task 8:\nЯка ймовірність того, що при 10000 незалежних киданнях монети герб випаде 5000 разів?\n")
print("Task 9:\nФірма відправила на базу 1000 якісних виробів. Ймовірність того, що вироби в дорозі пошкодяться дорівнює 0,002.\nЗнайти ймовірність того, що на базу прибуде 5 пошкоджених виробів.\n")
print("Task 10:\nНехай ймовірність того, що грошовий приймальник автомату при опусканні монети скидає неправильно дорівнює 0,03.\nЗнайти найімовірніше число випадків правильної роботи автомату, якщо буде кинуто 150 монет.\n")
print("\n")


print_results()
OutputFile()