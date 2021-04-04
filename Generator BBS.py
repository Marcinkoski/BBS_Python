import random
#wybór liczb p i q
p=12899
q=12979   #p i q to liczby pierwsze, dające resztę 3 mod 4
n=p*q
war= True
def NWD(a,b):
    while war:
        if a==b:
            return a
        elif a>b:
            a=a-b
        else:
            b=b-a
war=True
d=0
while war:
    d=random.randrange(2,n-1)
    if NWD(d,n)==1:
        war=False
print('podaj k ')
k=int(input())
for i in range(1,k):
    d=pow(d,2,n)
print('podaj zakres losowania - od i do')
print('od:')
od=int(input())
print('do:')
do=int(input())
wynik=d%(do-od)+od
print(wynik)
