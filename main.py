import math
def Calculator():
    x=input('Deshiron te /,x,+,-,√')
    if x == '/':
        a=int(input())
        b=int(input())
        print(a,'/',b,'=',a/b)
    elif x == 'x':
        a=int(input())
        b=int(input())
        print(a, 'x',b,'=',a*b)
    elif x == '+':
        a=int(input())
        b=int(input())
        print(a,'+',b,'=',a+b)
    elif  x == '-':
        a=int(input())
        b=int(input())
        print(a,'-',b,'=',a-b)
    elif   x == '√':
        a=int(input())
        print(a,'√','=', math.sqrt(a))
Calculator()