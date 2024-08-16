email =input("Enter your  email:  ")
if len(email) >=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")== 1):
            if (email[-4]== ".") ^ (email[-3]=="."):
                print("your email is right")
             
                     
                  
           
                
        
            else:
                print("wrong email")
        else:
            print("wrong email 3")

    else:
        print("wrong email")
else:
    print("wrong email syntax 1")