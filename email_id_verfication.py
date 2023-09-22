from collections import Counter
def validate_name(name):
   if len(name)==0  or  len(name)>15:
        return False
   elif( name.isalpha()):
        return True
       
   
def validate_phone_no(phno):
    c=Counter(phno)
    if len(phno)<10 or phno.isalpha() or len(c)==1 or len(phno)>10:
        return False
    
    elif(phno.isdigit()):
        return True
   

def validate_email_id(email_id):
     if (email_id[-4:]==".com" and len(".com")==1) and (email_id[-9:-4]=="gmail"or "yahoo" or "hotmail" and (len("gmail")==1 and
                                                                                                             and emai_id[-10:-9]=="@"):
          return True
     else:
          return False
     

    

def validate_all(name,phone_no,email_id):
        if(name and  phone_no and email_id):
            n=validate_name(name)
            if not n:
                 print("Invalid Name")
            p=validate_phone_no(phone_no)
            if not p:
                 print("Invalid phone number")
            e=validate_email_id(email_id)
            if not e:
                print("Invalid email id")
        else:
           print("All the details are valid")


#Provide different values for name, phone_no and email_id and test your program
validate_all("Tina", "9989658307", "tina@yahoo.com")
