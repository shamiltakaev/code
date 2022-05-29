# Практическое задание №4 
# Задача Пользователь вводит номер месяца (от 1 до 12). Вывести название сезона года на
# экран (зима, весна, лето, осень);
# number_month = int(input())

# print("Зима" if number_month <= 2 or number_month == 12 
#       else "Весна" if 3 <= number_month <= 5 
#       else "Лето" if 6 <= number_month <= 8 
#       else "Осень")


# Практическое задание №4 
# Задача № 2:
# Пользователь вводит число. Программа должна проверить делится ли число на 6

# number = int(input())

# print("Делится" if number % 6 == 0 
#        else "Не делится")


# Практическое задание №6
# Задача № 1:
# Напишите программу перевода введенного веса в граммы, килограммы, тонны.
# Приставки, которые будет использовать программа: g – граммы, kg – килограммы, t –
# тонны.

# weight = input()

# if "kg" in weight:
#     kg = int(weight[:-2])
#     gr = kg * 1000
#     tonn = kg / 1000
#     print(str(gr) + "g")
#     print(str(tonn) + 't')
# elif "g" in weight:
#     gr = int(weight[:-1])
#     kg = gr / 1000
#     tonn = kg / 1000
#     print(f"{kg}kg")
#     print(f"{tonn}t")
# else:
#     tonn = int(weight[:-1])
#     kg = tonn * 1000
#     gr = kg * 1000
#     print(f"{kg}kg")
#     print(f"{gr}g")
    

# Практическое задание №8
# Задача № 1:
# Написать программу, которая считывает 5 чисел со стандартного ввода и выводит на
# экран результат их произведения.

# nums = list(map(int, input().split()))
# mult = 1
# [mult := mult * i for i in nums]
# print(mult)


# Практическое задание №8
# Задача № 2 :
# Написать программу которая получает со стандартного ввода строку и выводит на
# экран количество заглавных символов
# word = input()

# print(len([i for i in word if i.isupper()]))


# Практическое задание №10
# 1 Создайте список чисел от 10 до 45 с шагом 5
# 2 Используя цикл while выведите на экран числа от 1 до 5
# 3 Дана строка “123467”, но в ней пропущена одна цифра. 
# Использую функцию, выведите на экран строку со вставленной цифрой.
# 4 Дана строка “Если долго будешь писать на питоне - начнёшь говорить со
# змеями”. Нужно вывести на экран количество букв “о”

# nums = list(range(10, 46, 5))

# i = 1
# while i <= 5:
#     print(i)
#     i += 1

# line = '123467'
# line = list(line)
# line.insert(4, '5')
# line = "".join(line)
# print(line)

# line = "Если долго будешь писать на питоне - начнёшь говорить со змеями."

# print(line.count("о"))

# Практическое задание №13
# 1. Даны два параметра вывода “Я ученик”. Используя функцию def выведите на
# экран “Я лучший ученик Синергии!”

# line = "Я ученик".split()

# line.insert(1, 'лучший')
# line.append("Синергии!")

# line = " ".join(line)
# print(line)

# Практическое задание №13
# 2. Даны числа “2, 4, 6, 8, 10”. В этом списке нужно выписать все числа кратные “4”
# и умножить их на 2 Вывести на экран.

# nums = [2, 4, 6, 8, 10]

# print(*[i * 2 for i in nums if i % 4 == 0])


# Практическое задание №17
# Создать текстовой файл, в котором будет хранится: Приветствие, Ваше имя и Ваше направление в обучении.

# with open("file.txt", "w") as file:
#     welcome = input()
#     name = input()
#     direction_learn = input()
#     file.write(f"{welcome}\n{name}\n{direction_learn}")


# Практическое задание №19
# Используя библиотеку NumPy:
# 1 Создайте строку от 0 до 10
# 2 Поменяйте местами цифры 5 8
# 3 Выведите на экран два массива: первоначальный и изменённый
# 4 Объедините их
# 5 Сделайте из этой строки 3 столба

# import numpy

# nums = numpy.arange(0, 11)
# new_nums = nums.copy()

# new_nums[5], new_nums[8] = new_nums[8], new_nums[4]
# print(*nums, *new_nums)

# res_nums = "".join(map(str, numpy.concatenate((nums, new_nums))))

# for i in range(0, len(res_nums), 3):
#     print(res_nums[i], res_nums[i+1], res_nums[i+2])


# Практическое задание №20
# 1 Создайте класс студентов
# 2 Создайте класс предметов
# 3 Используя новый проект, загрузите данные классов и задайте примеру двух
# студентов и двух направлений

# class Student:
#     def __init__(self, name, fname, age):
#         self.name = name
#         self.fname = fname
#         self.age = age

#     def getInfo(self):
#         return f"{self.name} {self.fname}"

# class Subject:
#     def __init__(self, name, student):
#         self.name = name
#         self.student = student

#     def getInfo(self):
#         if self.student.age < 17 or self.student.age > 25:
#             return f"{self.student.getInfo()} без дисциплины"
#         return f"{self.student.getInfo()} - {self.name}"

# from test import Student, Subject

# studentFirst = Student("Shamil", "Takaev")
# studentSecond = Student("Adam", "Takaev")

# subjFirst = Subject("Mathematics", studentFirst)
# subjSecond = Subject("English language", studentSecond)

# print(subjFirst.getInfo())
# print(subjSecond.getInfo())

# Практическое задание №21
# 1 Используйте работу с прошлого задания
# 2 Добавьте в неё исключения в виде школьников и закончивших ВУЗ

class Student:
    def __init__(self, name, fname, age):
        self.name = name
        self.fname = fname
        self.age = age

    def getInfo(self):
        return f"{self.name} {self.fname}"

class Subject:
    def __init__(self, name, student):
        self.name = name
        self.student = student

    def getInfo(self):
        if self.student.age < 17 or self.student.age > 25:
            return f"{self.student.getInfo()} без дисциплины"
        return f"{self.student.getInfo()} - {self.name}"

from test import Student, Subject
studentFirst = Student("Shamil", "Takaev", 23)
studentSecond = Student("Adam", "Takaev", 14)

subjFirst = Subject("Mathematics", studentFirst)
subjSecond = Subject("English language", studentSecond)

print(subjFirst.getInfo())
print(subjSecond.getInfo())
