class Dog:
    def __init__(self,name,breed,owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    def bark(self):
        print("Woof")

class Owner:
    def __init__(self,name,address,contact_number):
        self.name = name
        self.address = address
        self.phone = contact_number

owner1 = Owner("Akash","Shivpuram","9102823628")
dog1 = Dog("Lucy","German Shepard",owner1)
dog1.bark()
print(dog1.name)
print(dog1.breed)
print(dog1.owner.name)

dog2 = Dog("Tom","Scottish Terrier",owner1)
dog2.bark()
print(dog2.name)
print(dog2.breed)
print(dog2.owner.address)

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello I am {self.name} and I am {self.age} years old")

person1 = Person("Akash","19")
print("Name:",person1.name)
print("Age:",person1.age)
person1.greet()        

class Student:
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.result = marks
    
    def details(self):
        print(f"Student name:{self.name}\nStudent age:{self.age}\nStudent marks:{self.result}")
    
student1 = Student("Akash","19","98")
student2 = Student("Astha","25","99")
student3 = Student("Nutan","50","97")
student1.details()
student2.details()
student3.details()

class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.age = year

    def details(self):
        print(f"Brand:{self.brand}\nModel:{self.model}\nYear:{self.age}")

car1 = Car("Audi","S11","2011")
car2 = Car("Mercedez","A9","2009")
car3 = Car("Ferrari","N19","1996")

car1.details()
car2.details()
car3.details()
        
class Book:
    def __init__(self,title,author,price):
        self.name = title
        self.author = author
        self.cost = price

    def details(self):
        print(f"Title:{self.name}\nAuthor:{self.author}\nPrice:{self.cost}")

book1 = Book("The Alchemist","Paulo Coelho","Rs.300")
book2 = Book("Ayomic Habits","James Clear","Rs.500")
book3 = Book("The Monk Who Sold His Ferrari","Robin Sharma","Rs.350")

book1.details()
book2.details()
book3.details()
        