def addN(number1, number2):
    number1 = number1 + number2
    print(f'Result: {number1}')
    return number1
def subN(number1, number2):
    number1 = number1 - number2
    print(f'Result: {number1}')
    return number1
def divN(number1, number2):
    number1 = number1 / number2
    print(f'Result: {number1}')
    return number1
def multN(number1, number2):
    number1 = number1 * number2
    print(f'Result: {number1}')
    return number1

value1 = int(input("Enter first number: "))
choice = input('Enter operator (+, -, *, /): ')
value2 = int(input('Enter second number: '))

if choice == '+':
    addN(value1, value2)
elif choice == '-':
    subN(value1, value2)
elif choice == '/':
    divN(value1, value2)
elif choice == '*':
    multN(value1, value2)
else:
    print('Please enter in a valid choice.')