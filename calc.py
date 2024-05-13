from art import logo

import math

def subtract(a,b):
  """This function will subtract the second input from the first one."""
  return a - b

def add(a,b):
  """This function will add the two inputs together. """
  return a + b

def divide(a,b):
  """This function will divide the first input by the second one."""
  return a/b

def multiply(a,b):
  """This function will multiply the two inputs together. """
  return a*b

operations = {
  "*": multiply,
  "-": subtract,
  "+": add,
  "/": divide
}

def calculator():
  print(logo)
  num_1 = float(input("what should the first number be?\n"))
  contin_ = True
  for operation in operations:
    print(operation)
  while contin_:
    op_symbol = input("what operation would you like to perform?\n")
    num_2 = float(input("what should the next number be? \n"))
    answer = operations[op_symbol](num_1,num_2)
    print(f"{num_1} {op_symbol} {num_2} = {answer}")
    cont_ = input("would you like to continue calculating? type y or n\n")
    if cont_== "y":
      num_1 = answer
    else:
      contin_ = False
      calculator()
calculator()