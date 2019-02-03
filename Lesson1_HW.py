#EASY
#Task1

x = 5
y = 6.7
z= x*y
print (z)
a = input('Введите число a: ')
b = input('Введите число b: ')
s = int(a) - int(b)
print(s)

#Task2
a = input('Введите число: ')
s = int(a) + 2
print(s)

#Task3
age = input('How old are you? ')
if int(age) >= 18:
    print ('Доступ разрешен')
else:
    print ('Извините, пользование данным ресурсом только с 18 лет')

#MEDIUM
#Task1
a = int (input('Введите число: '))
while a < 0 or a > 10:
    print ('Неверно. Попробуй ввести число от 0 до 10')
    a = int (input('Введите число: '))
    break
print ('Ты попал в диапазон!')
print (a**2)

#Task2
a = int (input('Введите число a: '))
b = int (input('Введите число b: '))
a = a + b
b = a - b
a = a - b
print (a, b)

#HARD
#Task1
name = input('Введите свое имя: ')
age = int(input('Введите свой возраст: '))
weight = int(input('Введите свой вес: '))

if age < 30 and 50 <= weight < 120:
    print( name,'- вы в хорошем состоянии, так держать!')
elif age > 30 and (weight < 50 or weight > 120):
    print(name, '- вам следует заняться собой')
elif age > 40 and (weight < 50 or weight > 120):
    print(name, '- вам, следует обратиться к врачу!')
else:
    print('Что-то что не предвидено в данном цикле. Надеюсь все хорошо!')