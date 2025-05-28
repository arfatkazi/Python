# python Calculator

# try:
#     operator = input("Enter an operator (+, -, *, /, %): ")

#     num1 = float(input("Enter first number: "))
#     num2 = float(input("Enter second number: "))

#     if operator == '+':
#         result = num1 + num2
#     elif operator == '-':
#         result = num1 - num2
#     elif operator == '*':
#         result = num1 * num2
#     elif operator == '/':
#         result = num1 / num2  # division by zero will be caught
#     elif operator == '%':
#         result = num1 % num2
#     else:
#         raise ValueError("Invalid operator!")

#     print("Result:", result)

# except ValueError as ve:
#     print("Value Error:", ve)
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")
# except Exception as e:
#     print("Something went wrong:", e)



# weight convert

# weight = float(input("Enter your weight: "))
# unit = input("Kilograms or Pounds? (K or L): ").upper()

# if unit == 'K':
#     weight = weight * 2.205
#     unit = "Lbs"
#     print(f"Your weight is: {weight:.2f} {unit}")
# elif unit == 'L':
#     weight = weight / 2.205
#     unit = "Kgs"
#     print(f"Your weight is: {weight:.2f} {unit}")
# else:
#     print(f"'{unit}' is not a valid unit. Please enter 'K' or 'L'.")



# Fahrenheit conversion program
# temp = float(input("Enter the temperature value: "))
# unit = input("Is this in Celsius or Fahrenheit? (C or F): ").upper()

# if unit == 'C':
#     converted = (temp * 9/5) + 32
#     print(f"{temp:.2f}°C is {converted:.2f}°F")
# elif unit == 'F':
#     converted = (temp - 32) * 5/9
#     print(f"{temp:.2f}°F is {converted:.2f}°C")
# else:
#     print("Invalid unit. Please enter 'C' or 'F'.")


num = 6

age = 25
result = "Even" if num % 2 == 0 else "ODD"
my_age = "Adult" if age >= 25 else "child"


print(my_age)