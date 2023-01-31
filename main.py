# LOG
# Записать и вывести на экран условие, которое является истинным, когда хотя бы одно из чисел x, y и z больше 80.
# Записать и вывести на экран условие, которое является истинным, когда оба числа a и b одновременно положительны или отрицательны.
# Даны три числа: 130, 25 и 70. Выведите на экран наименьшее из них, использовав для этого программную проверку.

# 1
x = 323
y = 3
z = 55
if y > 80 or x > 80 or z > 80:
    print(True)

# 2
a = 5
b = 5
if (a > 0 and b > 0) or (a < 0 and b < 0):
    print(True)

# 3
a = 130
b = 25
c = 70
if c < a and c < b:
    print(c)
if b < a and b < c:
    print(b)
if a < c and a < b:
    print(a)



# LINE
# 1
def get_kilo():
    gr = int(input('Введите граммы: '))
    kg = gr / 1000
    print(kg)
get_kilo()

#2 Даны две переменные x = 10 и y = 55. Поменяйте их значения местами. Выведите значения переменных на экран до и после замены.

x = 10
y = 55
print(x, y)

def change_value(a, b):
    c = a
    a = b
    b = c
    print(a, b)
change_value(x, y)

# 3 С клавиатуры вводится расстояние L в метрах. Необходимо найти и вывести на экран количество полных километров в нем.

def get_km():
    metr = int(input('Введите расстоняие в метрах: '))
    km = metr // 1000
    print(km)
get_km()

#4  С клавиатуры вводится целое число. Необходимо вывести число, обратное введенному по порядку составляющих его цифр. 
# Например, если было введено число 12345, программа должна вывести пользователю на экран число 54321.

def get_revers():
    rev = input('Введите число: ')
    spis = list(rev)
    spis.reverse()
    print("".join(spis))
get_revers()

# 5 Получите и преобразуйте текущую системную дату, возвращаемую методом date.today() 
# модуля стандартной библиотеки datetime, из формата «год-месяц-день» в формат «день.месяц.год». 
# Выведите оба формата даты на экран.

import datetime

print(datetime.date.today())
print(datetime.date.today().strftime("%d.%m.%Y"))



# CYCLES
# Посчитайте количество символов в строке 'Python - это Питон!', использовав счетчики на основе циклов for и while.
# Найдите сумму всех элементов списка [1, '2', 3, 4, '5'], предварительно приводя строки к целым числам.
# Используя циклы, проверьте при помощи оператора in наличие символов строки 'abcde123' в строке 'bad_cat_23', 
# выводя результаты проверки на экран в виде «Символ "a" есть в "bad_cat_23".» или «Символа "n" нет в "bad_cat_23".».
# Cгенерируйте и выведите на экран мозаичное изображение гексагональной сетки, напоминающее мелкоячеистую проволочную сетку.

# 1
stroka = 'Python - это питон'

k = 0
for i in stroka:
    k += 1
print(k)

# 2
summa = [1, '2', 3, 4, '5']
sum = 0
for elem in summa:
    if type(elem) is str:
        sum += int(elem)
    else:
        sum += elem
print(sum)

# 3
stroka_1 = 'abcde123'
stroka_2 = 'bad_cat_23'

for  sim in stroka_1:
    if sim in stroka_2:
        print('Символ ', sim, ' есть в "', stroka_2, '".', sep='')
    else:
        print('Символ ', sim, ' нет в "', stroka_2, '".', sep='')
print()

# 4

for i in range(2, 15):
    if i % 2 == 0:
        for j in range(2, 15):
            print('/ \_', end='')
    else:
        for j in range(2, 15):
            print('\_/ ', end='')
    print('')

# 5

spis1=['1','2','3','4','5','6','7','8','9']
print('----+------------------------------------------------------------------------')
print('|  x  |','\t'.join(spis1))
print('----+------------------------------------------------------------------------')


for i in spis1:
    spis=[]
    for j in spis1:
        spis.append(str(int(i)*int(j)))
    print(f'|  {i}  |','\t'.join(spis))

print('----+------------------------------------------------------------------------')

#  6