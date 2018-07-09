# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    pass


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


a = float(input("Введите десятичную дробь: "))
b = int(input("Введите кол-во знаков после запятой: "))

def my_round(a, b):
    c = a * (10 ** b)
    c_int = int(c)
    h = (c * 10) % 10
    if h > 5:
        c_int += 1
    result = c_int / (10 ** b)
    return result
print(my_round(a, b))
    



# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    pass


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))


ticket = input("Введите номер билетика: ")

def lucky_ticket(ticket):
    a = int(ticket[0])
    b = int(ticket[1])
    c = int(ticket[2])
    d = int(ticket[3])
    e = int(ticket[4])
    f = int(ticket[5])
    if (a + b + c) == (d + e + f):
        lucky = True
    else:
        lucky = False
    return lucky
print(lucky_ticket(ticket))
