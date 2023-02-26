number1 = input("First number: ")
number2 = input("Second number: ")

number1 = int(number1)
number2 = int(number2)

addition = number1 + number2
substraction = number1 - number2
multiplication = number1 * number2
division = number1 // number2

message = f"""
For {number1} and {number2}:
their sum is {addition},
their rest is {substraction},
their product is {division},
and their division is {multiplication}
"""

print(message)
