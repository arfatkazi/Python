# class Animal:
    
#         def eat(self):
#             print("This animal is eating.")

#         def sleep(self):
#             print("This animal is sleeping.")

# class Prey(Animal):
#     def flee(self):
#         print("This animal is fleeing.")


# class Predator(Animal):
#     def hunt(self):
#         print("This animal is hunting.")



# class Rabbit(Prey):
#     pass



# class Hawk(Predator):
#     pass

# class Fish(Prey,Predator):
#     pass



# rabbit  = Rabbit()
# hawk  = Hawk()
# fish  = Fish()


# rabbit.flee()
# hawk.hunt()



# fish.hunt()
# fish.flee()



# fish.sleep()
# fish.eat()


# rabbit.sleep()





# SUPER


class Shape:
    def __init__(self,color,is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"This is {self.color} and it's {self.is_filled}")


class Circle(Shape):
    def __init__(self,color,is_filled,radius):
        super().__init__(color,is_filled)
        self.radius = radius

    def describe(self):
        #method overloading
        super().describe()
        print(f"Radius is {3.14 *self.radius * self.radius} ")


class Square(Shape):
     def __init__(self,color,is_filled,width):
        super().__init__(color,is_filled)
        self.width = width



class Triangle(Shape):
    def __init__(self,color,is_filled,width,height):
        super().__init__(color,is_filled)
        self.width = width
        self.height = height





circle = Circle('RED',True,5)
square = Square('blue',True,width=60)



print(circle.color)
print(circle.is_filled)
print(circle.radius)
circle.describe()