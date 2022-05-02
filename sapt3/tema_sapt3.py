def suma(*args,**kwargs):
    s=0
    for i in args:
        if type(i)==int or type(i)==float:
            s+=i
    return s

print(suma(2,4,'abc',-2,param=2))


def sum1(n):
    if n==0:
        return n
    else: return n+sum1(n-1)
print(sum1(3))


def sum2(n):
    if n==0:
        return 0
    elif n%2==0:
        return n+sum2(n-1)
    else:
        return sum2(n-1)
print(sum2(5))


def sum3(n):
    if n==1:
        return 1
    elif n%2==1:
        return n+sum3(n-1)
    else:
        return sum3(n-1)
print(sum3(5))


def numar():
    x=input()
    if(type(x)==int or type(x)==float):
        print(x)
    else:
        print(0)
numar()