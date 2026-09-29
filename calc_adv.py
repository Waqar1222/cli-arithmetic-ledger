
with open("cli_arithmetic_ledger.txt", "a") as f:
        f.write("Calculator History\n")
while True: 
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter another number: "))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        continue

    def add(a, b):
        return a + b
    def subtract(a, b):
        return a - b
    def multiply(a, b):
        return a * b
    def divide(a, b):
        if b == 0:
            return "Error! Division by zero."
        else:
            return a / b

    print("Select operation:")
    print("1. Add ")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == '1':
        with open("cli_arithmetic_ledger.txt", "a") as f:
            f.write(f"{a} + {b} = {add(a, b)}\n")
        print(f"{a} + {b} = {add(a, b)}")
    elif choice == '2':
        with open("calc_history.txt", "a") as f:
            f.write(f"{a} - {b} = {subtract(a, b)}\n")
        print(f"{a} - {b} = {subtract(a, b)}")
    elif choice == '3':
        with open("calc_history.txt", "a") as f:
            f.write(f"{a} * {b} = {multiply(a, b)}\n")
        print(f"{a} * {b} = {multiply(a, b)}")
    elif choice == '4':
        with open("calc_history.txt", "a") as f:
            f.write(f"{a} / {b} = {divide(a, b)}\n")
        print(f"{a} / {b} = {divide(a, b)}")
    else:
        print("Invalid input")


    print("Thank you for using the calculator!")
    pla_ag = input("Do you want to perform another calculation? (yes/no)")
    if pla_ag.lower() == 'no':
        break
    else: 
        continue
