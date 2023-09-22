while(1):
    n=int(input())
    if n<0:
        n=n+2**32
    if n==0:
        print("0")
    res={10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
    sum1=[]
    s=""
    while(n>0):
        rem=n%16
        sum1.append(rem)
        n=n//16
    for i in range(0,len(sum1)):
        if sum1[i] in res:
            sum1[i]=res[sum1[i]]
    ans=sum1[::-1]
    for i in ans:
        s+=str(i)
    print(s)

