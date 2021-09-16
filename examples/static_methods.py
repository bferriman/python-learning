# A static method is class method that can be used without creating
# an instance of the class. These are typically utility functions.

class Sum:
    @staticmethod
    def get_sum(*args):
        sum_1 = 0
        for i in args:
            sum_1 += i

        return sum_1

def main():
    print("Sum :", Sum.get_sum(1, 2, 3, 4, 5))

main()