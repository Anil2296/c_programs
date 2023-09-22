from collections import Counter
list_of_numbers=[1,2,2,3,3,3,4,4,4,4]
up=[]
c=Counter(list_of_numbers)
k=list(c.keys())
print(k)
v=list(c.values())
print(k)
for i in range(0,len(v)):
    print(i)
    if v[i]>1:
       up.append(k[i])
print(up)         
