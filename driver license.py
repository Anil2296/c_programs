def driver(speed):
    points=0
    n=70
    if(speed<=70):
        print("Ok")
    else:
        for i in range(5,(speed-n)+1,5):
            points+=1
        print("points :",points)
    if(points>=12):
        print("License suspended")
speed=int(input("Enter speed "))        
driver(speed)        
    
