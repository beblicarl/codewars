class vehicle:

    Truth = 'in the world'

    def __init__(self,name,colour,wheelsize, speedlimit):
        self.name = name 
        self.colour = colour
        self.wheelsize = wheelsize
        self.speedlimit = speedlimit

    @classmethod
    def good(cls):
        return f'Jida is the best tutor {cls.Truth}'
    
    @staticmethod
    def pleasantries(Hello = 'This is my second coding assignment'):
        return f'Hello!! {Hello}, I hope i did great...'

    def drive(self):
        return f'I drive a {self.colour} {self.name}. I have a {self.wheelsize} wheel size  and a speed limit of {self.speedlimit}'

Picanto = vehicle('Picanto','yellow','small', '180 km/h')
print(f'My car is {Picanto.name}')
print(f'It is {Picanto.colour} in colour')
print(f'It has a {Picanto.wheelsize} wheel size')
print(f'And the speed limit of the {Picanto.name} is {Picanto.speedlimit}')
print(Picanto.drive())


Toyota = vehicle('Toyota corolla','red','medium', '240 km/h')
print(f'My car is a {Toyota.name}')
print(f'It is {Toyota.colour} in colour')
print(f'It has a {Toyota.wheelsize} wheel size')
print(f'And the speed limit of the {Toyota.name} is {Toyota.speedlimit}')
print(Toyota.drive())

Benz = vehicle('Benz C-class','black','large', '240 km/h')
print(f'My car is a {Benz.name}')
print(f'It is {Benz.colour} in colour')
print(f'It has a {Benz.wheelsize} wheel size')
print(f'And the speed limit of the {Benz.name} is {Benz.speedlimit}')
print(Benz.drive())
print(vehicle.good())
print(vehicle.pleasantries())