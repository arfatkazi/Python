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
# class Employee:
#     def __init__(self,name,position):
#         self.name = name
#         self.position = position


#     def get_info(self):
#         print(f"{self.name} = {self.position}")

#     @staticmethod
#     def is_valid_position(position):
#         valid_position = ["Data Analyst","Data science","AI/ML","Android Developer"]
#         return position in valid_position
    



# employee1 = Employee("Raj","Actor")
# employee2 = Employee("Aiyaan","Data science")
# employee3 = Employee("furkan","Data Analyst")




# # print(Employee.is_valid_position('Data science'))


# print(employee1.name)
# print(employee1.position)

# employee1.get_info()
# employee2.get_info()
# employee3.get_info()



# # class method


# class Student:
#     count  = 0
#     total_gpa = 0

#     def __init__(self,name,gpa):
#         self.name = name
#         self.gpa = gpa
#         Student.count +=1
#         Student.total_gpa += gpa



#     def get_info(self):
#         return f"{self.name} {self.gpa}"
    
#     @classmethod
#     def get_count(cls):
#         return f"total # of students: {cls.count}"
    
#     @classmethod
#     def get_average_gpa(cls):
#         if cls.count == 0:
#             return 0
#         else:
#             return f"{cls.total_gpa / cls.count}"

# student1 = Student("Arfat",7.5)
# student2 = Student("Aiyaan",5.5)

# print(Student.get_count())
# print(Student.get_average_gpa())




# magic method

# class Book:
#     def __init__(self,title,author,num_pages):
#         self.title = title
#         self.author = author
#         self.num_pages = num_pages

#     # def __str__(self):
#     #     return f"📘 '{self.title}' by {self.author} — {self.num_pages} pages"

#     def __lt__(self,other):
#         return self.num_pages < other.num_pages
#     def __add__(self,other):
#         return self.num_pages + other.num_pages

#     def __contains__(self,keyword):
#         return keyword in self.title

#     def __getitem__(self,key):
#         if key == 'title':
#             return self.title
#         elif key == 'author':
#             return self.author
#         elif key == 'num_pages':
#             return self.num_pages
#         else:
#             return f"Not a valid key"

# book1 = Book("2 states",'arfat kazi',300)
# book2 = Book("fift shades of grey",'aiyaan kazi',800)
# book3 = Book("john wick",'ovais',600)




# print(book1 < book2)
# print(book2< book3)
# print(book3 < book1)

# print(book3 < book1)
# # add
# print(book3 + book1)
# print(book1 + book2)
# print(book2 + book3)


# print('2 states' in book1)
# print('lion' in book1)


# print(book1['num_pag'])



# @property



# class Rectangle:
#     def __init__(self,height,width):
#         self._height = height
#         self._width = width


#     @property
#     def height(self):
#             return f"{self._height:.1f}cm"
#     @property
#     def width(self):
#             return f"{self._width:.1f}cm"
    

#     @height.setter
#     def height(self,new_height):
#         if new_height > 0:
#                 self._height = new_height
#         else:
#                 print("Height must be greater than 0")


#     @width.setter
#     def width(self,new_width):
#         if new_width > 0:
#                 self._width = new_width
#         else:
#             print("Width must be greater than 0")

#     @height.deleter
#     def height(self):
#         del self._height
#         print("height has been deleted")



#     @width.deleter
#     def width(self):
#         del self._width
#         print("width has been deleted")

# rectangle = Rectangle(3,5)


# # rectangle.width = 10
# rectangle.height  = 10
# rectangle.width  = 10


# del rectangle.height 
# del rectangle.width 




# @ decorator

def add_sprinkles(func):
        def wrapper(*args,**kwargs):
              
          print("you added some sprinkles🎇.")
          func(*args,**kwargs)
        return wrapper

def added_fudge(func):
        def wrapper(*args,**kwargs):
        
          print("you added some fudge🍫.")
          func(*args,**kwargs)
        return wrapper



@add_sprinkles
@added_fudge

def get_ice_cream(flavor):
    print(f"This is your {flavor} ice cream🍨")

get_ice_cream('chocolate')