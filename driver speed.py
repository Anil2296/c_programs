def speed(x):
    if(x<=70):
        print("ok")
    k=70
    count=0
    for i in range(k,x):
        if(i%5==0):
            count+=1
    print("points :",count)
    if(count>=12):
        print("licences suspended")
x=int(input("enter the speed"))
speed(x)

          
          
            
 
