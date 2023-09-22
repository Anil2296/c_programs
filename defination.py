def fact(n):
    f=1
    while n>=1:
        f=f*n
        n=n-1
    return f
def table(n):
    i=1
    while i<=20:
        p=n*i
        print(n,"X",i,"=",p)
        i=i+1
