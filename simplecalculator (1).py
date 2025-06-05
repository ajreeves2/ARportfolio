1#anyla reeves
11/19/24

#calculator

#init

#Function
def add(number1, number2):
    answer= number1 + number2
    print(answer)
def sub(number1, number2):
    answer= number1-number2
    print(answer)
def mult(number1, number2):
    answer= number1 *number2
    print(answer)
def div(number1, number2):
    answer= number1 / number2
    print(answer)

def simplecalculator():
    while True:
        print("please choose an operation")
        print("""1.addition
 2. subtract
 3. multiplication
 4. divison
 5. quit""")
        option= int(input("1-5: "))

        if option==1:
            number1=int(input("you have selected addition. enter the first number: "))
            number2=int(input("enter the second number:"))
            add(number1, number2)

        if option==2:
            number1=int(input("you have selected subtraction. enter the first number: "))
            number2=int(input("enter the second number:"))
            sub(number1, number2)

        if option==3:
            number1=int(input("you have selected multiplication. enter the first number: "))
            number2=int(input("enter the second number:"))
            mult(number1, number2)

        if option==4:
            number1=int(input("you have selected division. enter the first number:"))
            number2=int(input("enter the second number:"))
            div(number1, number2)

        if option==5:
            print("Thank you for using simple calculator!")
            break

#main
print("welcome to simple calculator")
simplecalculator()



