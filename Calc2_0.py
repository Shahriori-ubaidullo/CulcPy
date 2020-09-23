#Подключаем библиотеки
from math import sqrt

lan = int(input('Выберите язык интерфейса/Select to language for interfeis(0/1):'))
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Блок с переводом>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
lan_variable = ['Введите значение', 'Enter the value of']
lan_error = ['Ошибка! Введите числовое выражение...', 'Error! Enter a numeric expression...']
lan_discr_1 = ['Дискриминант больше нуля!\nКорней два!', 'The discriminant is greater than zero!\nThe roots of the two!']
lan_discr_0 = ['Дискриминант равен нулю!\nКорень один!', 'The discriminant is equal to zero!\nThe root of one!']
lan_discr = ['Корней нет! Приходите позднее)', 'No roots! Come back later)']
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Окончание блока с переводом>>>>>>>>>>>>>>>>>>>>>>>>>>>


#((((((((((((((((((((((((((((((((((Блок функций)))))))))))))))))))))))))))))))))))))))

#^^^^^^^^^^^^^^^^^^^Функции проверки введённых данных на тип данных^^^^^^^^^^^^^^^^^^^
def variable_a():
    while 1 == 1:
        try:
            var_a = float(input(f'{lan_variable[lan]} a: '))
        except ValueError:
            #В случае если значение не число, вывести данный текст и перезапустить цикл
            print(f'{lan_error[lan]}')
        else:
            #В случае если значение число, завершить цикл и возвратить значение переменной функции
            return var_a

def variable_b():
    while 1 == 1:
        try:
            var_b = float(input(f'{lan_variable[lan]} b: '))
        except ValueError:
            print(f'{lan_error[lan]}')
        else:
            return var_b

def variable_c():
    while 1 == 1:
        try:
            var_c = float(input(f'{lan_variable[lan]} c: '))
        except ValueError:
            print(f'{lan_error[lan]}')
        else:
            return var_c
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
def discrim(var_a = 0, var_b = 0, var_c = 0):
    var_d = float(var_b ** 2 - 4 * var_a * var_c)
    return var_d

def roots(var_d, var_a, var_b, var_c):
    if var_d > 0:
        var_x1 = (-var_b + sqrt(var_d))/(var_a * 2)
        var_x2 = (-var_b - sqrt(var_d))/(var_a * 2)
        return f'{lan_discr_1[lan]}\n>>> [X1 = {var_x1}\n>>> [X2 = {var_x2}'
    
    elif var_d == 0:
        var_x = -var_b/(var_a * 2)
        return f'{lan_discr_0[lan]}\n>>> [X = {var_x}'
    
    elif var_d < 0:
        return f'{lan_discr[lan]}'

def int_var():
    print(f'ax^2 + bx + c = 0\n')
    var_a = variable_a()
    print(f'>> {var_a}x^2 + bx + c = 0\n')

    var_b = variable_b()
    print(f'>> {var_a}x^2 + {var_b}x + c = 0\n')

    var_c = variable_c()
    print(f'>> {var_a}x^2 + {var_b}x + {var_c} = 0\n')

    var_d = discrim(var_a, var_b, var_c)
    print(f'D = {var_b}^2 - 4 * {var_a} * {var_c} = {var_d}\n')

    root = roots(var_d, var_a, var_b, var_c)
    print(root)

def quad_eqt():
    int_var()
#((((((((((((((((((((((((((((((((Окончание блока функций))))))))))))))))))))))))))))))))

quad_eqt()