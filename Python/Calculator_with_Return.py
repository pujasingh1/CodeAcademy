#calculator
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operation = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  for symbol in operation:
    print(symbol)

  should_continue = True
  while should_continue:
    pick_operation = input("Pick the operation: ")
    num2 = float(input("what's the next number?: "))
    calculation_function = operation[pick_operation]
    answer = calculation_function(num1, num2)

    print(f"{num1} {pick_operation} {num2} = {answer}")

    if input(f"Type 'y' to continue with {answer}, or type 'n' to start a new calcualtion: ") == "y":
      num1 = answer
    else:
      should_continue = False
      calculator()


calculator()
