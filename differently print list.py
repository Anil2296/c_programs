n = 6
l= [16 ,17 ,4, 3, 5, 2]
max1=[l[-1]]
max2=l[-1]
for i in range(n-1,-1,-1):
    print(l[i-1],l[i])
    if l[i-1]>=l[i] and l[i-1]>=max2:
        print(i)
        print(l[i-1])
        max2=l[i-1]
        max1.append(l[i-1])
k=max1[::-1]
print(*k)

                   
    
    
    
    
