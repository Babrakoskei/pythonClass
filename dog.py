class Dog:
    breed= "German shepherd"

    def __init__(self,color,height,weight,age):
        self.color= color
        self.height= height
        self.weight= weight
        self.age= age

    def bite(self):
        return f"My dog is a German shepherd it has a nice {self.color}, height of {self.height} and a weight of {self.weight} when it was {self.age} years old He bit someone" 
    def eat(self):
        return f"Her dog loves to eat it is a {self.color} German shepherd with a weight of {self.weight} a height of {self.weight}. The dog just turned {self.age} years old"      
        