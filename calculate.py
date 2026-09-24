import math
print("Это крутой калькулятор")
print("Доступные опции : + , - , * , / , **, sqrt, sin , cos, tan, ctn")

opperation  = input("Воин, введи, какую операцию ты хочешь сотворить")

#Операции с 1 числом 

if opperation in ["sqrt", "sin", "cos", "tan", "ctn"]:
    number1 = float(input("Воин, введи число, с которым ты хочешь сотворить магию: "))
    if opperation == "sqrt":
        result = math.sqrt(number1)
    elif opperation == "sin":
        result = math.sin(math.radians(number1))
    elif opperation == "cos":
        result = math.cos(math.radians(number1))
    elif opperation == "tan":
        result = math.tan(math.radians(number1))
    elif opperation == "ctn":
        if number1 == 0:
            result = "Ошибка: ctn не определен для 0"
        else:
            result = 1 / math.tan(math.radians(number1))
    print(f"Результат: {result}")

#Операции с 2 числами
if opperation in ["+", "-", "*", "/", "**"]:
    number1 = float(input("Воин, введи первое число: "))
    number2 = float(input("Воин, введи второе число: "))
    if opperation == "+":
        result = number1 + number2
    elif opperation == "-":
        result = number1 - number2
    elif opperation == "*":
        result = number1 * number2
    elif opperation == "/":
        if number2 == 0:
            result = "Ошибка: деление на ноль"
        else:
            result = number1 / number2
    elif opperation == "**":
        result = number1 ** number2
    print(f"Результат: {result}")