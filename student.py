class Student:
    school= "AkiraChix"
#constructor which is a function
    def __init__(self,name,age):
        self.name= name
        self.age = age

    def speak(self):
         return  f'Hello my name is {self.name} and I am {self.age} years old and I love {self.school}'   
#To create a class use class keyword
#start the class name with a capital letter. If the class has more than one word capitalize each word
#you cannot have spaces in a class name
#When you save your code in a .py file it is called a module 
# To import a class from a module use dot notation from module import class Name
#Modules in a dir form a package.

