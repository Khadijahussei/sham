pin="0000"
entered_pin=(input("enter pin"))
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
