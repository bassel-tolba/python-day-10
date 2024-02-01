def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 -n2
def divide(n1, n2):
    return n1 / n2
def multiply(n1, n2):
    return n1 * n2
def square(n1, n2):
    return n1 ** n2

operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply,
    "square": square
    }
answer = "new"
while answer == "yes" or answer == "new":
    


    if answer == "yes":
        
        for char in operations:
            print(char)
        need = input("witch operation do you want to continue with ?: ")
        num2 = float(input("what is the next number?: "))    
        func = operations[need]
        result2 = func(result, num2)
        print(f"{result} {need} {num2} = {result2}")
    if answer == "new":
        num1 = float(input("what is the first number?: "))
        for char in operations:
            print(char)
        need = input("witch operation do you want to do?")
        num2 = float(input("what is the second number?: "))    
        func = operations[need]
        result = func(num1, num2)

        print(f"{num1} {need} {num2} = {result}")
    answer = input(f"type yes to continue by adding to the result of {result} or no to finish or 'new' to refresh ")


