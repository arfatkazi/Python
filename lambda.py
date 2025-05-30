# add = lambda x,y : x + y

# x = 2 
# y =3
# print(f"Addition of {x} + {y}: {add(x,y)}")



# subtract = lambda x,y : x-y



# print(subtract(5,2))


# Lambda with maps
# nums = [1,3,4,5,6]


# squares = list(map(lambda x: x**2,nums))


# print(squares)

# Lambda with filters

# even = list(filter(lambda x: x % 2 == 0,nums))


# print(even)



# lambda with reduce from functools


# from functools import reduce

# numbers = [1,2,3,4,5,6]




# product = reduce(lambda x,y : x*y,numbers)



# print(product)


# data = [(1, 'a'), (3, 'c'), (2, 'b')]

# # Sort by second element in tuple
# # sorted_data = sorted(data, key=lambda x: x[1])
# # print(sorted_data)

# sorted_data = sorted(data,key=lambda x:x[1])

# print(sorted_data)


max_func = lambda x, y: x if x > y else y
print(max_func(10, 20))  # Output: 20