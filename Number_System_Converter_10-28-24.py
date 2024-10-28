import string

def binary_to_any(num1,base2): #binary to any number system except binary
    if base2 == 8:
        num2 = oct(int(str(num1),2))[2:]
        print(str(num1) + "₂ = " + str(num2) + "₈")
    elif base2 == 10:
        num2 = int(str(num1),2)
        print(str(num1) + "₂ = " + str(num2) + "₁₀")
    elif base2 == 16:
        num2 = hex(int(str(num1),2))[2:]
        num2 = num2.capitalize()
        print(str(num1) + "₂ = " + str(num2) + "₁₆")

def octal_to_any(num1,base2): #octal to any number system except octal
    if base2 == 2:
        num2 = bin(int(str(num1),8))[2:]
        print(str(num1) + "₈ = " + str(num2) + "₂")
    elif base2 == 10:
        num2 = int(str(num1),8)
        print(str(num1) + "₈ = " + str(num2) + "₁₀")
    elif base2 == 16:
        num2 = hex(int(str(num1),8))[2:]
        num2 = num2.capitalize()
        print(str(num1) + "₈ = " + str(num2) + "₁₆")

def decimal_to_any(num1,base2): #decimal to any number system except decimal
    if base2 == 2:
        num2 = bin(int(num1))[2:]
        print(str(num1) + "₁₀ = " + str(num2) + "₂")
    elif base2 == 8:
        num2 = oct(int(num1))[2:]
        print(str(num1) + "₁₀ = " + str(num2) + "₈")
    elif base2 == 16:
        num2 = hex(int(num1))[2:]
        num2 = num2.capitalize()
        print(str(num1) + "₁₀ = " + str(num2) + "₁₆")

def hex_to_any(num1,base2): #hex to any number system except hex
    if base2 == 2:
        num2 = bin(int(str(num1),16))[2:]
        print(str(num1) + "₁₆ = " + str(num2) + "₂")
    elif base2 == 8:
        num2 = oct((int(str(num1),16)))[2:]
        print(str(num1) + "₁₆ = " + str(num2) + "₈")
    elif base2 == 10:
        num2 = int(str(num1),16)
        print(str(num1) + "₁₆ = " + str(num2) + "₁₀")

def numchecker(base): # Checks if num is a number, if not it asks you to reinput
    while True:
        try:
            int(base)
        except ValueError:
            print("Not an integer!")
            base = input("Reinput your base [2] [8] [10] [16]: ")
            continue 
        else:
            base = int(base)
            return base

def not_that_value(num1, base1): #checks if the value cannot be an octal or an
    while True:
        try:
            num1 = int(str(num1),int(base1))
        except:
            print("The base " + base1 + " cannot be a base to this number!")
            base1 = input("Reinput your base: ")
            continue
        else:
            return base1

def hex_checker(compare, ch2, base1): #if the number is a hexadecimal and the base is not 16, the function sets it into 16, if not, it bypasses
    while True:
        if (compare & (ch2 - set(string.digits))): 
            if base1 != 16:
                print("This number is a hexadecimal value! The base is set to 16.") 
                base1 = 16
                continue
            if base1 == 16:
                return base1
        else:
            return base1

def converter():
    print("Number System Converter")
    while True:
        num1 = input("What number do you wish to convert? Enter 'end' to exit. ")
        if num1.lower() == "end": #ends program
            break
        else: #checks if the input is unconvertable or not
            compare = set(num1.lower())
            ch1 = set(string.printable)
            ch2 = set(string.hexdigits)
            ch = ch1 - ch2
            if compare & ch:
                print("Invalid format!")
                continue
            else:
                pass
        
        base1 = input("What is your number's base? [2] [8] [10] [16] ") #determines the base of the inputted number
        base1 = numchecker(base1)
        base1 = not_that_value(num1, hex_checker(compare, ch2, base1))

        base2 = input("To which base? [2] [8] [10] [16] ") #determines the base the number is to be converted to
        base2 = numchecker(base2)

        if base1 == base2: #checks if similar bases
            print("Similar bases! Choose again.")
            continue
        elif base1 == 2:
            binary_to_any(num1,base2)
        elif base1 == 8:
            octal_to_any(num1,base2)
        elif base1 == 10:
            decimal_to_any(num1,base2)
        elif base1 == 16: 
            hex_to_any(num1,base2)
        else:
            print("Invalid format!")

    print("Session ended.")



converter() #The program is all in this single function. This allows it to be retrieved easily for the main "Hub" program.
