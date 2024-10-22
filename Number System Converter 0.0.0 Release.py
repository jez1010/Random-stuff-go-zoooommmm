import string

def binary_to_any(num1):
    if base2 == 8:
        num2 = oct(int(str(num1),2))[2:]
        print(str(num1) + "₂ = " + str(num2) + "₈")
    if base2 == 10:
        num2 = int(str(num1),2)
        print(str(num1) + "₂ = " + str(num2) + "₁₀")
    if base2 == 16:
        num2 = hex(int(str(num1),2))[2:]
        num2 = num2.capitalize()
        print(str(num1) + "₂ = " + str(num2) + "₁₆")

def octal_to_any(num1):
    if base2 == 2:
        num2 = bin(int(str(num1),8))[2:]
        print(str(num1) + "₈ = " + str(num2) + "₂")
    if base2 == 10:
        num2 = int(str(num1),8)
        print(str(num1) + "₈ = " + str(num2) + "₁₀")
    if base2 == 16:
        num2 = hex(int(str(num1),8))[2:]
        num2 = num2.capitalize()
        print(str(num1) + "₈ = " + str(num2) + "₁₆")

def decimal_to_any(num1):
    if base2 == 2:
        num2 = bin(int(num1))[2:]
        print(str(num1) + "₁₀ = " + str(num2) + "₂")
    if base2 == 8:
        num2 = oct(int(num1))[2:]
        print(str(num1) + "₁₀ = " + str(num2) + "₈")
    if base2 == 16:
        num2 = hex(int(num1))[2:]
        num2 = num2.capitalize()
        print(str(num1) + "₁₀ = " + str(num2) + "₁₆")

def hex_to_any(num1):
    if base2 == 2:
        num2 = bin(int(str(num1),16))[2:]
        print(str(num1) + "₁₆ = " + str(num2) + "₂")
    if base2 == 8:
        num2 = oct((int(str(num1),16)))[2:]
        print(str(num1) + "₁₆ = " + str(num2) + "₈")
    if base2 == 10:
        num2 = int(str(num1),16)
        print(str(num1) + "₁₆ = " + str(num2) + "₁₀")

while True:
    num1 = input("What number do you wish to convert? Enter 'end' to exit. ")
    if num1.lower() == "end": #ends program
        break
    else: #checks if the input is unconvertable or not
        compare = num1.lower()
        compare = set(compare)
        ch = string.hexdigits
        ch = set(ch)
        if compare & ch:
            pass
        else:
            print("Invalid format!") #loops back to the start
            continue
    base1 = int(input("What is your number's base? [2] [8] [10] [16] ")) #determines the base of the inputted number


    base2 = int(input("To which base? [2] [8] [10] [16] ")) #determines the base the number is to be converted to
    if base1 == base2: #checks if similar bases
        print("Similar bases! Choose again.")
        continue
    else:
        if base1 == 2:
            binary_to_any(num1)
        if base1 == 8:
            octal_to_any(num1)
        if base1 == 10:
            decimal_to_any(num1)
        if base1 == 16: 
            hex_to_any(num1)
        if base1 == 64 or base2 == 64:
            print("You unlocked a secret base!")
            b64_to_any(num1)
        else:
            print("Invalid format!")
    print("Session ended.")