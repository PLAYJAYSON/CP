from math import sqrt
my_dict1 = {'1':{'DEBUG':'Tracemod'}, '2' : {'ERROR':'Null pointer exeption'}, '3' :{'INFO' : 'startGame allert'}, '4' : {'DEBUG' : 'sendAllert'}, '5' : {'ERROR' : 'Novalidate JSON'}}
def UltiMath(*args):
    m = 0
    d = 0
    a = tuple(map(float, input().split()))
    for i in a:
            m+=i
    for k in a:
            d+=(k - m)**2
    print('математическое ожидание>>> ~',round(m/len(a),3))
    print('дисперсия>>>',d)
    print('среднеквадратическое отклонение>>> ~',round(sqrt(d),3))
    print('коэффициент вариации>>> ~',round(sqrt(d)/m,3))
def SortData(*args):
    num = []
    strg = []
    booler = []
    other = []
    a = tuple(args)
    for i in range(len(a)):
        if str(a[i])=='True' or str(a[i])=='False':
            booler.append(a[i])
        elif str(a[i]).isalpha():
            strg.append(a[i])
        elif type(a[i]) == float or type(a[i])==int:
            num.append(a[i])
        else :
            other.append(a[i])

    print('List_of_num :',num)
    print('List_of_str :',strg)
    print('List_of_bool :',booler)
    print('List_of_other :',other)
def DictSearch(d, **kwargs):
    a = dict(kwargs)
    for i in a.values():
        if d in i:
            print(i)
UltiMath()
SortData(1,'hi', False, 2.3, 'Yes', True, (1, 2))
DictSearch('ERROR',**my_dict1)