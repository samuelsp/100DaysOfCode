from art import logo

# calculator

# add
def add(n1, n2):
  return n1 + n2

# subtract
def sub(n1, n2):
  return n1 - n2

# multiply
def mul(n1, n2):
  return n1 * n2

# divide
def div(n1, n2):
  return n1 / n2

print(logo)
operations = {'+': add, '-': sub, '*': mul, '/': div}

def calculator():  
  should_continue = True
  
  try:
    num1 = float(input("What's the first number? "))  
  
    for key in operations:
      print(key)

    while should_continue:  
      operation = input("What's the operation? ")
      
      if operation not in operations:      
        raise Exception("Invalid operation!")   
      
      num2 = float(input("What's the second number? "))
      
      result = operations[operation](num1, num2)
      print(f"{num1} {operation} {num2} = {result}")

      question = f"Type 'y' to continue calculating with {result}, " + \
      "or type 'n' to start a new calculation: "
      
      continue_calculation = input(question).lower()
      if continue_calculation == 'y':
        num1 = result
        continue
      else:
        should_continue = False

    answer = input("Do you want to continue? (y/n) ").lower()

    if answer == 'n':      
      print("Bye!")
      return

  except ValueError:
    print("Invalid input! Try again!")
  
  except Exception:
    print("Invalid operation! Try again!")
    
  calculator()

calculator()
