import string

def binary_to_any(num1,base2): #binary to decimal
    if base2 == 10:
        num2 = int(str(num1),2)

def octal_to_any(num1,base2): #octal to decimal
    if base2 == 10:
        num2 = int(str(num1),8)

def decimal_to_any(num1,base2): #decimal to any number system except decimal
    if base2 == 2:
        num2 = bin(int(num1))[2:]
    if base2 == 8:
        num2 = oct(int(num1))[2:]
    if base2 == 16:
        num2 = hex(int(num1))[2:]
        num2 = num2.capitalize()

def hex_to_any(num1,base2): #hex to decimal
    if base2 == 10:
        num2 = int(str(num1),16)

def numchecker(base): # Checks if num is a number, if not it asks you to reinput
    while True:
        try:
            int(base)
        except ValueError:
            print("Not an integer!")
            base = input("Reinput your base [2] [8] [10] [16]: ")
            continue 
        else:
            return base

def not_that_value(num1, base1): #checks if the value cannot be an octal or binary
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

def operations():
    

def calculator():
    print("Number System Calculator")
    while True:
        base = int(input("Input the base of the two numbers to be added: "))
        num1 = input("First number: ")
        num2 = input("Second number: ")
        op = input("[1] Addition\
                   [2] Subtraction\
                   [3] Multiplication\
                   [4] Division")
        
        if base == 2:
            binary_to_any(num1,10)
            binary_to_any()
        elif base == 8:
            octal_to_any(num1,10)
            pass
        elif base == 10:
            
            pass
        elif base == 16: 
            hex_to_any(num1,10)
            pass
        else:
            print("Invalid format!")
            continue

