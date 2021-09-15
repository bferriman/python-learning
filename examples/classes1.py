class Dog:
    #initiation method will be called every time a Dog is created
    # self is used much like "this" is used in JS
    # using = lets you assign a default value if one is not passed
    def __init__(self, name="", height=0, weight=0):
        self.name = name
        self.height = height
        self.weight = weight

    def run(self):
        print("{} the dog runs".format(self.name))
    
    def eat(self):
        print("{} the dog eats".format(self.name))

    def bark(self):
        print("{} the dog barks".format(self.name))

def main():

    spot = Dog("Spot", 66, 26)
    spot.bark()

main()