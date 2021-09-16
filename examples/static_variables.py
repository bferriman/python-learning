# A static variable is a field that is declared inside a class but outside
# of any methods. Its value is shared by every object of that class.

class Dog:
    num_of_dogs = 0

    def __init__(self, name="Unknown"):
        self.name = name
        Dog.num_of_dogs += 1

    @staticmethod
    def get_num_of_dogs():
        print("There are currently {} dogs".format(Dog.num_of_dogs))


def main():
    spot = Dog("Spot")
    astro = Dog("Astro")
    april = Dog("April")
    copernicus = Dog("Copernicus")
    Dog.get_num_of_dogs()
    # could also call as spot.get_num_of_dogs(), astro.get_num_of_dogs(), etc.

main()