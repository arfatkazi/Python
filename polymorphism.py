# from abc import ABC,abstractmethod
# class Shape:
#     @abstractmethod
#     def area(self):
#         pass


# class Circle(Shape):
#     def __init__(self,radius): # constructor
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2
        





# class Square(Shape):
#     def __init__(self,side): # constructor
#         self.side = side

#     def area(self):
#         return self.side ** 2
        




# class Triangle(Shape):
#     def __init__(self,base,height): # constructor
#         self.base = base
#         self.height = height

#     def area(self):
#         return self.base * self.height * 0.5
        


# class  Pizza(Circle):
#     def __init__(self,name,radius):
#         self.name = name
#         super().__init__(radius)



# shapes = [Circle(4),Square(5),Triangle(6,7),Pizza("marghreita",15)]


# for shape in shapes:
#     print(shape.area())




# Duck Typing

# static method using direct class it doesn't depend on object
class Employee:
    def __init__(self,name,position):
        self.name = name
        self.position = position


    def get_info(self):
        print(f"{self.name} = {self.position}")

    @staticmethod
    def is_valid_position(position):
        valid_position = ["Data Analyst","Data science","AI/ML","Android Developer"]
        return position in valid_position
    



employee1 = Employee("Raj","Actor")
employee2 = Employee("Aiyaan","Data science")
employee3 = Employee("furkan","Data Analyst")




# print(Employee.is_valid_position('Data science'))


print(employee1.name)
print(employee1.position)

employee1.get_info()
employee2.get_info()
employee3.get_info()



# class method


class Student:
    count  = 0
    total_gpa = 0

    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        Student.count +=1
        Student.total_gpa += gpa



    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"total # of students: {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"{cls.total_gpa / cls.count}"

student1 = Student("Arfat",7.5)
student2 = Student("Aiyaan",5.5)

print(Student.get_count())
print(Student.get_average_gpa())




# magic method