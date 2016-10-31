while True:
    check = 0
    while (check == 0):
        num1 = input("Enter a number (or a letter to exit): ")
        try:
            if num1.isalpha():
                exit()
            elif float(num1).is_integer:
                num1 = int(num1)
                check = 1
        except ValueError:
            print("Wrong value! Please repeat again") 

    check = 0
    while (check == 0):
        op = input("Enter an operation: ") 
        if (op == "+") or (op == "-") or (op == "/") or (op == "*"):
            check = 1
        else:
             print("Wrong value! Please repeat again")

    check = 0
    while (check == 0):
        num2 = input("Enter an other number: ")
        try:
            if float(num2).is_integer:
                num2 = int(num2)
                check = 1
        except ValueError:
            print("Wrong value! Please repeat again")

    if op == "+" :
        sum = num1 + num2
        print("Result:", num1, op, num2, "=", sum)

    if op == "-" :
        sub = num1 - num2
        print("Result:", num1, op, num2, "=", sub)

    if op == "/" :
        div = num1 / num2
        print("Result:", num1, op, num2, "=", div)

    if op == "*" :
        multi = num1 * num2
        print("Result:", num1, op, num2, "=", multi)