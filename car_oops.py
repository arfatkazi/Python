# class Car:
#     def __init__(self,model,year,color,for_sale):
#         self.model = model
#         self.year = year
#         self.color = color
#         self.for_sale = for_sale

#     def drive(self):
#         print(f"You drive the {self.model}")


#     def stop(self):
#         print(f"You stop the {self.model}")


# class Students:
#     class_year = 2025
#     num_student = 1
#     def __init__(self,name,age,height,roll_no,is_present):
#         self.name = name
#         self.age = age
#         self.height = height
#         self.roll_no = roll_no
#         self.is_present = is_present
#         Students.num_student += 1




class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")



# Inheritance

class Dog(Animal):
    pass


class Cat(Animal):
    pass


class Rabbit(Animal):
    pass


dog = Dog('Scooby')
cat = Cat('sohail')
rabbit = Rabbit('aiyaan')

print(dog.name)
print(cat.name)
print(rabbit.name)


print(dog.is_alive)
print(cat.is_alive)
print(rabbit.is_alive)


dog.sleep()
cat.sleep()
rabbit.sleep()


dog.eat()
cat.eat()
rabbit.eat()