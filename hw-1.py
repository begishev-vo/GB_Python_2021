
# 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные,
# выведите на экран.

print('Exercise #1')
print('_________________')
b = 5
c = 4
a = b + c
q_word = 'Привет,'
q_word_next = ' Мир!'
q_word_all = q_word + q_word_next
str_1 = input('Введите 1-е слово= ')
str_2 = input('Введите 2-е слово= ')
number_1 = int(input('Введите 1-е число= '))
number_2 = int(input('Введите 2-е число= '))
print('Сумма: a = ',a)
print(q_word_all)
print("Деление: ", b / c)
print('Произведение: ', b * c)
print('Вы ввели следующее:', str_1, str_2, number_1, number_2)
print('_________________')

# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите
# в формате чч:мм:сс. Используйте форматирование строк.

print('Exercise #2')
print('_________________')
time = int(input('Введите время в секундах '))
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time - (hours * 3600 + minutes * 60)
print(f'Наше время чч:мм:сс {hours} : {minutes} : {seconds}')
print('_________________')


# 3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
print('Exercise #3')
print('_________________')
n = int(input("Введите число - "))
total = (n + int(str(n) + str(n)) + int(str(n) + str(n)+ str(n)))
print("Сумма чисел n + nn + nnn - %d" % total)
print('_________________')

# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции

print('Exercise #4')
print('_________________')
n = abs(int(input("Введите целое положительное число ")))
max = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > max:
        max = n % 10
    if n > 9:
        continue
    else:
        print("Максимальное цифра в числе ", max)
        break

print('_________________')

# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки
# (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
print('Exercise #5')
print('_________________')
revenue = float(input("Введите выручку  "))
costs = float(input("Введите издержки  "))
if revenue > costs:
    print(f"Фирма работает с прибылью, рентабельность выручки составила {revenue / costs:.2f}")
    employees = int(input("Введите количество сотрудников фирмы "))
    print(f"прибыль в расчете на одного сторудника сотавила {revenue / employees :.2f}")
elif revenue == costs:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")
print('_________________')

# 6. Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат
# спортсмена составить не менее b километров. Программа должна принимать
# значения параметров a и b и выводить одно натуральное число — номер дня.

print('Exercise #6')
print('_________________')
a = int(input("Введите результаты 1 дня в км "))
b = int(input("Введите желаемый результат в км "))
results_days = 1
results_km = a
while results_km < b:
        a = a + 0.1 * a
        results_days += 1
        results_km = results_km + a
print(f"Вы достигнете требуемых показателей на %.d день" % results_days)
print('_________________')