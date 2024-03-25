#creating a class function for the person.
class Person:
    def _init_(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I am a {self.gender}.")

# Creating an instance of the Person class.
person1 = Person("Jokomba Samiat Omotolani", 18, "female")

# Calling the introduce method to display the person's information.
person1.introduce()

class A:
    
    def _init_(self,num):
        num=3
        self.num=num
def change(self):
    self.num=7
a=A(5)
print(a.num)
a.change()
print(a.num)

class A:
    print("Inside class")
A()

A()

obj=A()

class Student:
    def _init_(self,name,id):
        self.name=name
        self.id=id
        print(self.id)



std=Student("adebayo",1)



std.id=2



print(std.id)