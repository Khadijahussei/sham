set_pin=int(input("set pin"))
att=3
c=True

while c:
    enter_pin=int(input("enter pin"))
    if set_pin==enter_pin:
        print("correct pin")
        c=False
    else:
        print("incorrect pin",att,"attempts remaining")
       
        if att==0:
           print("blocked")
           c=False
    att-=1
        
                     
