


# name = input("Enter your name: ")

# while name == "":
#     print("you did not enter your name")
#     name = input("Enter your name: ")
# print(f"my name is {name}")
# food = input("Enter a food you like (or 'q' to quit): ")

# while food.lower() != "q":
#     print(f"You like {food}.")
#     food = input("Enter another food you like (or 'q' to quit): ")

# print("Bye!")



# # python compound interest calculator
# import math
# principal = 0
# rate = 0
# time = 0

# # while principal <=0:
# #     principal = float(input("Enter the principal amount: "))
# #     if principal<=0:
# #         print("principal can't be less than equal to zero")

# while True:
#     principal = float(input("Enter the principal amount: "))
#     if principal<0:
#         print("principal can't be less than equal to zero")
#     else:
#         break


# # while rate <=0:
# #     rate = float(input("Enter the rate amount: "))
# #     if rate<=0:
# #         print("rate can't be less than equal to zero")


# while True:
#     rate = float(input("Enter the rate amount: "))
#     if rate<0:
#         print("rate can't be less than equal to zero")
#     else:
#         break

# # while time <=0:
# #     time = float(input("Enter the time in year/s: "))
# #     if time<=0:
# #         print("time can't be less than equal to zero")

# while True:
#     time = float(input("Enter the time in year/s: "))
#     if time<0:
#         print("time can't be less than equal to zero")
#     else:
#         break

# total = principal * pow((1 + rate / 100),time)

# print(f"Balance after {time} year/s: ${total:^.2f}")

# FOR LOOP


# for x in reversed(range(1,11)):
 
#         print(x)



# for x in range(1,21):
#     if x == 13:
#         continue
#     else:
#         print(x)

# for x in range(1,21):
#     if x == 13:
#         break
#     else:
#         print(x)


# # sleep countdown timer

# import time
# my_time = int(input("Enter the time in seconds: "))


# for x in reversed(range(0,my_time+1)):
#     print(x)
#     time.sleep(1)

# print("Time's UP!")

# for x in range(my_time,0,-1):
#     seconds = x % 60
#     minutes = int(x/60) % 60
#     hour = int(x/3600)
#     print(f"{hour:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)

# print("Time's UP!")



# nested loop
# for x in range(3):
#     for y in range(1,10):
#         print(y,end=" ")
#     print()


rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbols = input("Enter the symbols to use: ")


for x in range(rows):
    for y in range(columns):
        print(symbols,end=" ")
    print()


#