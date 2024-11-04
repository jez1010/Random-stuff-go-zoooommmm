import string

def binary_to_any(num1): #binary to decimal
    num2 = int(str(num1),2)
    return num2

def octal_to_any(num1): #octal to decimal
    num2 = int(str(num1),8)
    return num2

def decimal_to_any(num1,base2): #decimal to any number system except decimal
    if base2 == 2:
        num2 = bin(int(num1))[2:]
    if base2 == 8:
        num2 = oct(int(num1))[2:]
    if base2 == 16:
        num2 = hex(int(num1))[2:]
    return num2

def hex_to_any(num1): #hex to decimal
    num2 = int(str(num1),16)
    return num2

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
        
def choicechecker(op): # Checks if op is a number, if not it asks you to reinput, also checks if it is within the choices
    while True:
        try:
            int(op)
        except ValueError:
            print("Not an integer!")
            op = input("Reinput your choice [1] [2] [3] [4]: ") 
            continue 
        else:
            return op

def not_that_value(num1, num2, base): #checks if the value cannot be an octal or binary
    while True:
        try:
            num1 = int(str(num1),int(base))
            num2 = int(str(num2),int(base))
        except:
            print("The base " + base + " cannot be a base to this number!")
            base = input("Reinput your base: ")
            continue
        else:
            return base

def hex_checker(num1, num2, base): #if the number is a hexadecimal and the base is not 16, the function sets it into 16, if not, it bypasses
    while True:
        if (set(num1) & (set(string.hexdigits) - set(string.digits))) or (set(num2) & (set(string.hexdigits) - set(string.digits))): 
            if base != 16:
                print("This number is a hexadecimal value! The base is set to 16.") 
                base = 16
                continue
            elif base == 16:
                return base
        else:
            return base

def operations(f_num, s_num, op, base):
    f_num = int(f_num)
    s_num = int (s_num)
    remainder = 0
    if op == "1":
        ans = f_num + s_num
    elif op == "2":
        ans = f_num - s_num
    elif op == "3":
        ans = f_num * s_num
    elif op == "4":
        if base == 2 or base == 8 or base == 16:
            ans, remainder = division(f_num, s_num, base)
        else:
            ans = f_num/s_num
            remainder = f_num % s_num    
    return ans, remainder

def division(f_num, s_num, base):
    try:
        ans = f_num/s_num
        if base == 2:
            decimal_to_any(str(ans), 2)
        elif base == 8:
            decimal_to_any(str(ans), 8)
        elif base == 16:
            decimal_to_any(str(ans), 16)
    except:
        ans = int(f_num/s_num)
        remainder = f_num % s_num
        return ans, remainder
    else:
        ans = f_num/s_num
        remainder = 0
        return ans, remainder

def main():
    print("Number System Calculator")
    while True:
        num1 = input("First number: ").strip() #input for the first number
        compare1 = set(num1.lower())
        ch = set(string.printable) - set(string.hexdigits)
        if compare1 & ch:
            print("Invalid format!")
            continue
        else:
            pass

        num2 = input("Second number: ").strip() #input for the second number
        compare2 = set(num2.lower())
        if compare2 & ch:
            print("Invalid format!")
            continue
        else:
            pass

        base = input("Input the base of the two numbers: ").strip() #input for the base of the number
        base = numchecker(base)
        base = int(not_that_value(num1, num2, hex_checker(num1, num2, base)))
        

        print("[1] Addition\n[2] Subtraction\n[3] Multiplication\n[4] Division")
        op = input("Which operations? Enter 'end' to exit. ")
        op = choicechecker(op) #checks if the choice is in the choices
        
        if base == 2:
            f_num = binary_to_any(num1)
            s_num = binary_to_any(num2)
            ans, remainder = operations(f_num, s_num, op, 2)
            if remainder == 0:
                print("Result: " + decimal_to_any(str(ans), 2))
            else: #for division
                print("Result: " + decimal_to_any(str(ans), 2))
                print("Remainder: " + decimal_to_any(str(remainder), 2))

        elif base == 8:
            f_num = octal_to_any(num1)
            s_num = octal_to_any(num2)
            ans, remainder = operations(f_num, s_num, op, 8)
            if remainder == 0:
                print("Result: " + decimal_to_any(str(ans), 8))
            else: #for division
                print("Result: " + decimal_to_any(str(ans), 8))
                print("Remainder: " + decimal_to_any(str(remainder), 8))

        elif base == 10:
            f_num = num1
            s_num = num2
            ans, remainder = operations(f_num, s_num, op, 10)
            if remainder == 0:
                print("Result: " + str(int(ans)))
            else: #for division
                print("Result, Decimal Form: " + str(ans))
                print("Result: " + str(int(ans)))
                print("Remainder: " + str(remainder))

        elif base == 16: 
            f_num = hex_to_any(num1)
            s_num = hex_to_any(num2)
            ans, remainder = operations(f_num, s_num, op, 16)
            if remainder == 0:
                print("Result: " + decimal_to_any(str(ans), 16))
            else: #for division
                print("Result: " + decimal_to_any(str(ans), 16).capitalize())
                print("Remainder: " + decimal_to_any(str(remainder), 16).capitalize())

        else:
            print("Invalid format!")
            continue

if __name__ == "__main__": #allows the main Hub py to import without running the code
    main()