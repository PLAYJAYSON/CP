import math
def funtext(x1,x2,h)   
    l = []
    while round(x1, 1) <= x2:
        l.append(str(round((1 + x1 * x1) / 2 * math.atan(x1) - x1 / 2, 5)) + ',' + ' ' + 'При х = ' + str(round(x1, 2)))
        x1 += h
    print(l)
funtext(x1 = float(input('Введите от:')),x2 = float(input('и до какого значения рассматриваем функцию:')), h = float(input('Введите шаг смещения по оси x:')))

#####################################################################################
import string
def analyz(k):
    b = 0 #количество букв
    g = 0 #количество цифр
    l = 0 #количество спецсимволов
    o=len(k.split())#количество слов
    for i in range(len(k)):
        if k[i].isalpha():
            b+=1
        elif k[i].isdigit():
            g+=1
        elif k[i] in string.punctuation:
            l+=1
    print('Длина строки:',len(k), '\nКоличество слов:',o, '\nКоличество букв:',b,'\nКоличество цифр:',g, '\nКоличество знаков:',l)
analyz(input('Введите любую строку >>>'))
##########################################################################################
def textsplit(k):
     with open('CP3.txt', encoding='utf-8', mode='r') as myfile:
        file_contents = myfile.read().splitlines()
     print(file_contents.pop(k))
textsplit(k=int(input('Введите номер строки из текста>>>')))
