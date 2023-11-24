'''''
# 1 задание:
s=0
k=15
d=k-10
k=4*d
s=k-50
print(s)
# 2 задание:
x=3
y=4
z=x+y
z=z+1
x=y
y=5
x=z+y+7
print(x)
# 3 задание:
a =int(input())
b=a+1
c=b+1
print(a)
print(b)
print(c)
# 4 задание:
a=int(input())
b=int(input())
c=int(input())
d=a+b+c
print(d)
# 5 задание:
a=int(input())
s=6*a**2
v=a**3
print('Площадь полной поверхности=',s)
print('Объем куба=',v)
# 6 задание:
a=int(input())
b=int(input())
f=3*(a+b)**3+275*b*2-127*a-41
print(f)
# 7 задание:
a =int(input())
b=a+1
c=a-1
print("Следующее за числом",a,"число:",b)
print("Для числа",a,"предыдущее число:",c)
# 8 задание:
mo=int(input())
sis=int(input())
clav=int(input())
mis=int(input())
print((mo+sis+clav+mis)*3)
# 9 задание:
a=int(input())
b=int(input())
print(a,"+",b,"=",a+b)
print(a,"-",b,"=",a-b)
print(a,"*",b,"=",a*b)
# 10 задание:
a=int(input())
b=int(input())
n=int(input())
print(a+b*(n-1))
# 11 задание:
a=int(input())
b=a*2
c=a*3
d=a*4
g=a*5
print(a,b,c,d,g,sep'---')
# 12 задание:
b=int(input())
q=int(input())
n=int(input())
print(b*q**(n-1))
# 13 задание:
a=int(input())
print(a//100)
# 14 задание:
a=int(input())
b=int(input())
print(b//a)
print(b%a)

# 15 задание:
n=int(input())
if n%2==0:
    print(n/2)
else:
    print((n+1)/2)

# 16 задание:
a=int(input())
if a%4==0:
    print(a//4)
else:
    print((a//4)+1)

# 17 задание:
a=int(input())
m=a%60
h=a//60
print(a,'мин - это',h,'час',m,'минут')
# 18 задание:
a=int(input())
b=a%10
c=(a%100)//10
d=(a%1000)//100
print('Сумма цифр =',b+c+d)
print('Произведение цифр',b*c*d)

# 19 задание:
a=int(input())
b=a%10
c=(a%100)//10
d=(a%1000)//100
b=str(b)
c=str(c)
d=str(d)
print(d+c+b)
print(d+b+c)
print(c+d+b)
print(c+b+d)
print(b+d+c)
print(b+c+d)

# 20 задание:
a=int(input())
b=a%10
c=(a%100)//10
d=(a%1000)//100
f=(a%10000)//1000
b=str(b)
c=str(c)
d=str(d)
f=str(f)
print('Цифра в позиции тысяч равна',f)
print('Цифра в позиции сотен равна',d)
print('Цифра в позиции десятков равна',c)
print('Цифра в позиции едениц равна',b)
# 21 задание:
a,b=input(),input()
if a==b:
    print('Пароль принят')
else:
    print('Пароль не принят')

# 22 задание:
a=int(input())
if a%2==0:
    print('Четное')
else:
    print('Нечетное')

# 23 задание:
a=int(input())
b=a%10
c=(a%100)//10
d=(a%1000)//100
f=(a%10000)//1000
if f+b==d-c:
    print('ДА')
else:
    print('НЕТ')

# 24 задание:
a=int(input())
if a>=18:
    print('Доступ разрешен')
else:
    print('Доступ Запрещен')

# 25 задание:
a=int(input())
b=int(input())
c=int(input())
d=b-a
if c==b+d:
    print('YES')
else:
    print('NO')

# 26 задание:
a=int(input())
b=int(input())
if a>b:
    print(b)
else:
    print(a)

# 27 задание:
a=int(input())
b=int(input())
c=int(input())
d=int(input())
if a > b:
    a = b
if c > d:
    c = d
if a > c:
    a = c
print(a)


# 28 задание:
a=int(input())
if a<=13 and a>0:
    print('детство')
elif a>13 and a<25:
    print('молодость')
elif a>24 and a<60:
    print('зрелость')
elif a>59:
    print('старость')

# 29 задание:
i=0
sum=0
while i<3:
    i=i+1
    a=int(input())
    if a>0:
        sum=sum+a
print(sum)

# 30 задание:
a=int(input())
if 10000>a>999 and (a%7==0 or a%17==0):
    print('YES')
else:
    print('NO')

# 31 задание:
a=int(input())
b=int(input())
c=int(input())
if a+b>c and a+c>b and b+c>a:
    print('YES')
else:
    print('NO')

# 32 задание:
a=int(input())
if (a%4==0 and (a%100!=0)) or a%400==0:
    print('YES')
else:
    print('NO')

# 33 задание:
a=int(input())
b=int(input())
c=int(input())
d=int(input())
if a==c or b==d:
    print('YES')
else:
    print('NO')

# 34 задание:
a=int(input())
b=int(input())
c=int(input())
d=int(input())
if (a-1 <= c <= a+1) and (b-1 <= d <= b+1):
    print('YES')
else:
    print('NO')


# 35 задание:
a=int(input())
b=int(input())
if a>b:
    print('NO')
elif a<b:
    print('YES')
else:
    print("Don't know")

# 36 задание:
a=int(input())
b=int(input())
c=int(input())
if (a==b or b==c or a==c) and not(a==b==c):
    print('Равнобедренный')
elif a==b==c:
    print('Равносторонний')
else:
    print('Разносторонний')

# 37 задание:
a=int(input())
b=int(input())
c=int(input())
if (a>b>c) or (c>b>a)  :
    print(b)
elif (c>a>b) or (b>a>c):
    print(a)
elif (b>c>a) or (a>c>b):
    print(c)

# 38 задание:
a=int(input())
if (a%2!=0 and 0<a< 8) or (a%2==0 and 8<=a<=12):
    print('31')
elif (a%2==0 and 2<a<7 ) or (a%2!=0 and 8<a<12):
    print('30')
elif a==2:
    print('28')

# 39 задание:
a=int(input())
if 0<a<60:
    print('Легкий вес')
elif 60<=a<64:
    print('Первый полусредний вес')
elif 64<=a<69:
    print('Полусредний вес')

# 40 задание:
a=int(input())
b=int(input())
c=input()
if b==0 and c=='/':
    print('На ноль делить нельзя!')
elif c=='*':
    print(a*b)
elif c=='-':
    print(a-b)
elif c=='+':
    print(a+b)
elif c=='/':
    print(a/b)
else:
    print('Неверная операция')

# 41 задание:
a=input()
b=input()
if (a=='красный' and b=='синий') or (a=='синий' and b=='красный') :
    print('фиолетовый')
elif (a=='красный' and b=='желтый') or (a=='желтый' and b=='красный'):
    print('оранжевый')
elif (a=='синий' and b=='желтый') or (a=='желтый' and b=='синий'):
    print('зеленый')
elif (a == 'синий' or a == 'красный' or a == 'желтый') and a == b:
    print(a)
else:
    print('ошибка цвета')

# 41 задание:
a=int(input())
if a==0:
    print('зеленый')
elif 1<=a<=10:
    if a%2==0:
        print('черный')
    else:
        print('красный')
elif 11<=a<=18:
    if a%2==0:
        print('красный')
    else:
        print('черный')
elif 19<=a<=28:
    if a%2==0:
        print('черный')
    else:
        print('красный')
elif 29<=a<=36:
    if a%2==0:
        print('красный')
    else:
        print('черный')
else:
    print('ошибка ввода')

# 42 задание:
a=int(input())
b=int(input())
c=int(input())
d=int(input())
if c < a:
    if d < a:
        print('пустое множество')
    elif d == a:
        print(d)
    elif a < d <= b:
        print(a, d)
    elif d > b:
        print(a, b)
elif c == a:
    if d <= b:
        print(c, d)
    else:
        print(c, b)
elif c < b:
    if d <= b:
        print(c, d)
    else:
        print(c, b)
elif c == b:
    print(c)
else:
    print('пустое множество')

# 43 задание:
a=float(input())
b=float(input())
print((a*b)/2)

# 44 задание:
a=float(input())
b=float(input())
c=float(input())
print(a/(b+c))

# 45 задание:
a=float(input())
if a==0:
    print('Обратного числа не существует')
else:
    print(1/a)

# 46 задание:
a=float(input())
print((5/9)*(a-32))

# 47 задание:
a=int(input())
if 0<a<3:
    sum=0
    while a!=0:
        a=a-1
        sum=sum+10.5
    print(sum)
elif 2<a:
    a=a-2
    sum = 21
    while a!=0:
        a=a-1
        sum=sum+4
    print(sum)

# 48 задание:
a=float(input())
a=a%1
a=(a*10)//1
print(int(a))

# 49 задание:
a=float(input())
a=a%1
print(a)

# 50 задание:
a=int(input())
b=int(input())
c=int(input())
d=int(input())
g=int(input())
mal=min(a,b,c,d,g)
bol=max(a,b,c,d,g)
print('Наименьшее число =', mal)
print('Наибольшее число =', bol)

# 51 задание:
a=int(input())
b=int(input())
c=int(input())
mal=min(a,b,c)
bol=max(a,b,c)
srd=(a+b+c)-(bol+mal)
print(bol)
print(srd)
print(mal)

# 52 задание:
a=int(input())
b=a%10
c=(a%100)//10
d=(a%1000)//100
mal=min(d,b,c)
bol=max(d,b,c)
if bol-mal==(b+c+d)-(bol+mal):
    print('Число интересное')
else:
    print('Число неинтересное')

# 53 задание:
a=float(input())
b=float(input())
c=float(input())
d=float(input())
g=float(input())
print(abs(a)+abs(b)+abs(c)+abs(d)+abs(g))
'''
# 54 задание:
a=int(input())
b=int(input())
c=int(input())
d=int(input())
print(abs(a-c)+abs(b-d))





