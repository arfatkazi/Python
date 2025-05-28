# def happy_birthday(name,age):
#     print(f"Happy Birthday {name}")
#     print(f"You are {age} old!\n")


# happy_birthday('Arfat',25)
# happy_birthday('Aiyaan',23)
# happy_birthday('Abdulla',14)



# def display_invoice(username,amount,due_date):
#     print(f"Hello {username}")
#     print(f"Your bill of ₹{amount} is due: {due_date}")

# display_invoice('Arfat',4000,'11/04/2025')



# def add(x,y):
#     z = x + y
#     return z



# def subtract(x,y):
#     z = x - y
#     return z


# def multiply(x,y):
#     z = x * y
#     return z

# print(add(1,2))
# print(subtract(4,2))
# print(multiply(4,2))


# def create_names(first_name,last_name):
#     first_name = first_name.capitalize()
#     last_name = last_name.capitalize()
#     return first_name + " " + last_name


# full_name = create_names(last_name="kazi",first_name="arfat")

# print(full_name)



# count time function
# import time
# def count_time(end,start=0):
#     for x in range(start,end+1):
#         print(x)
#         time.sleep(1)
#     print("Done!")


# count_time(10)



# *args
# **kwargs

# def add(*args):
#     total = 0
#     for arg in args:
#         total+= arg
#     print(total)


# add(1,2,3,6)


# def full_names(*args):
#     for arg in args:
#         print(arg,end=" ")


# full_names("arfat","kazi","misbha","kazi")



# **kwargs


# def full_info(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key }: {value:10}")

# full_info(name="arfat",city="thane",gender="male",occupation="IT")



# def shipping_label(*args,**kwargs):
#     for arg in args:
#         print(arg,end=" ")
#     print()
#     for value in kwargs.values():
#         print(value)


# shipping_label("arfat","kazi",city="thane",gender="male",occupation="IT")



# membership operator IN NOT IN



# word = "apple"


# letter = input("Guess a letter in the secret word: ")


# if letter not in word:
#     print(f"letter was not found: {letter}")

# else: 
#     print(f"letter was found: {letter}")




# list comprehension



# doubles = [x*2 for x in range(1,11) ]

# print(doubles)



numbers = [1,-3,4,-10,2,-100,-4,-76]


positive_num = [ num for num in numbers if num >=0]

negative_num = [ num for num in numbers if num <0]

print(positive_num)

print(negative_num)