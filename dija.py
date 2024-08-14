created_pin=int(input("Create pin"))
confirmed_pin=int(input("confirm pin"))
pin=None

if confirmed_pin==created_pin:
    pin=created_pin
    print("pin created successfully")
    entered_pin=int(input("enter pin"))
    if entered_pin==pin:
       print("log in successfully")
    elif entered_pin!=pin:
        print("invalid pin attempt remain 3")
        entered_pin=(input("enter pin"))
        if entered_pin==pin:
            print("log in successfully")
        elif entered_pin!=pin:
            print("invalid pin attempt remain 2")
            entered_pin=(input("enter pin"))
            if entered_pin==pin:
                print("log in successfully")
            elif entered_pin!=pin:
                print("invalid pin attempt remain 1")
                entered_pin=(input("enter pin"))
                if entered_pin==pin:
                    print("log in successfully")
                elif entered_pin!=pin:
                    print("blocked")
elif confirmed_pin!=created_pin:
    print("pin did not match")
    









# entered_pin=int(input("Enter pin"))
# elif created_pin==entered_pin:
#     print("log in successfully")
# else:
#     print("invalid pin")