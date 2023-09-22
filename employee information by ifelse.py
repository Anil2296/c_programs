
eno=int(input("enter the employee number :"))
ename=input("enter the employee name : ")
sal= int(input("enter the salary :"))
if(sal>=20000):
    hra=sal*.4
    Da=sal*.3
    pf=sal*.2
elif(sal>=10000):
    hra=sal*.3
    Da=sal*.2
    pf=sal*.1
elif(sal>=5000):
    hra=sal*.2
    Da=sal*.1
    pf=sal*.05
else:
    hra=sal*.1
    Da=sal*.08
    pf=sal*.06
gs=hra+Da+sal
ns=gs-pf
print("Employee number is",eno)
print("Employee name is",ename)
print("Employee salary is",sal)
print("Gross salary is",gs)
print("Net salary is",ns)
    
    
