class Person:
    def __init__(self, name, age):
        self.name = name # Attribute
        self.age = age # Attribute

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.") 

# Create an instance of class Person
person1 = Person("Ana", 30)
# Call the greet method
person1.greet() # Output: Hello, my name is Ana and I am 30 years old.

#when using inheritance we saw the __init__() method which is the constructor, it is called automatically when a new instance of a class is created and it is used to initialize the attributes of the object.

### Example of Constructor

class LivingBeing:
    def __init__(self, name):
        self.name = name

class Person(LivingBeing):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

"""class Student(Person):
    def __init__(self, name, age,student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def enter(self):
        print(f"Hi, I'm {self.name}, {self.age} years old, and my student ID is {self.student_id}")
"""
