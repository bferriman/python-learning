class ImEmpty:

    def __init__(self, data_list):
        self.__data = data_list[0]

    @property
    def attr1(self):
        return self.__data['thing1']

    @property
    def attr2(self):
        return self.__data['thing2'][0]['thing3']


def do_the_thing():
    some_data = [{
        'thing1': 'corn dog',
        'thing2': [{
            'thing3': 'funnel cake'
        }]
    }]
    full_thing = ImEmpty(some_data)
    print('full_thing attr1 = ', full_thing.attr1)
    print('full_thing attr2 = ', full_thing.attr2)

def do_the_other_thing():
    some_data = [{}]
    empty_thing = ImEmpty(some_data)
    print('empty_thing attr1 = ', empty_thing.attr1)
    print('empty_thing attr2 = ', empty_thing.attr2)

def main():
    do_the_thing()
    do_the_other_thing()

main()