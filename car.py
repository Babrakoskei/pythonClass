class Car:
    name= "Tesla"

    def __init__(self,registration,color,speed, make):
        self.registration= registration
        self.color= color
        self.speed= speed
        self.make= make

    def accelerate(self):
        return f"My Tesla cars are going to have a {self.color}. They will have a speed of{self.speed}, a registration of {self.registration} and a make of {self.make}"
    def stop(self):
        return f"I bought a {self.color} Tesla  with a speed of {self.speed}, a registration of {self.registration} and a make of {self.make}"
            