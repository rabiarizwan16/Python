logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)
num=int(input("Enter any number:- "))
num2=int(input("Enter second number :- "))
def sum():
    add= num + num2
    print(f"{num}+{num2}= {add}")
def sub():
    s = num - num2
    print(f"{num}-{num2}={s}")
def multiply():
    mult = num * num2
    print(f"{num}*{num2}={mult}")
def remainder():
    rem = num % num2
    print(f"{num}+{num2}={rem}")
def division():
    div = num // num2
    print(f"{num}/{num2}={div}")

def calculator():
    print(f"operations are:- \n + \n - \n * \n % \n / ")
    pick = input("choose an operation:- ")
    if pick == "+":
        sum()
    if pick == "-":
        subtract()
    if pick=="*":
        multiply()
    if pick == "%":
        remainder()
    if pick == "//":
        division()

calculator()







'''print(logo)
num=int(input("Enter any number:- "))
print(f"operations are:- \n + \n - \n * \n % \n / ")
num2=int(input("Enter second number :- "))
pick=input("choose an operation:- ")
if pick == "+":
    add= num + num2
    print(f"{num}+{num2}= {add}")
elif pick == "-":
    sub=num-num2
    print(f"{num}-{num2}={sub}")
elif pick == "*":
    mult=num*num2
    print(f"{num}*{num2}={mult}")
elif pick == "%":
    rem=num%num2
    print(f"{num}+{num2}={rem}")
elif pick == "/":
    div=num/num2
    print(f"{num}/{num2}={div}")'''
