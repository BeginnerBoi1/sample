class Person:
    race = 'Filipino' # This is a class attribute
                      # shared among object

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age              # This is an instance attribute
        self.gender = gender
    
    def introduce(self):
        print(f"Hello im {self.name} and I'm {self.age} years old")
    
# WTF is a self?
student = Person("Jan Randolph", 15, "Male")
print(student.race)
student.introduce()

