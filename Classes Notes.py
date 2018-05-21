# Defining a class
class Cat(object):
    # TWO underscores before and after
    def __init__(self, color, pattern,):
        # Things that a Cat has
        self.color = color
        self.patter = pattern
        self.state = "happy"
        self.hungry = False

# Things that a Cat can do
    def jump(self):
        self.state = "Scared"
        print("The cat jumps in the air")

    def play(self):
        self.state = "happy"
        print("You play with the cat")


# Initiating(creating) two cats
cute_cat = Cat("brown", "Spots")
cute_cat2 = Cat("grey", "deformed spots")

# Getting information about the cats
print(cute_cat.color)
print(cute_cat2.state)

cute_cat.jump()
print(cute_cat.state)
print(cute_cat2.state)

cute_cat.play()
print(cute_cat.state)


class Car(object):

    def __init__(self, color, brand, num_cylinders_cylinders):
        self.color = color
        self.brand = brand
        self.cylinders = num_cylinders_cylinders
        self.engineOn = False

    def turn_on(self):
        if self.engineOn:
            print("Nothing Happens")
        else:
            print("The engine turns on")
            self.engineOn = True

    def move_forward(self):
        if self.engineOn:
            print("You move forward")
        else:
            print("Nothing Happens")

    def turn_off(self):
        if self.engineOn:
            print("The engine turns off")
            self.engineOn = False
        else:
            print("Nothing happens")


my_car = Car("Blue", "Subaru", 4)

my_car.turn_on()
my_car.move_forward()
my_car.turn_off()
