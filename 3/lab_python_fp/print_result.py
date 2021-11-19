from typing import Iterable

def print_result(func):
    def wrapper(*args, **kwargs):
        print("{} : ".format(func.__name__), end='')
        
        result = func(*args, **kwargs)

        if (isinstance(result, Iterable)):
            print('')
            for i in result:
                print(i)
        elif (isinstance(result, dict)):
            print('')
            for i in result.items():
                print("{} = {}".format(i[0], i[1]))
        else:
            print("{}".format(result))
        
        return func(*args, **kwargs)

    return wrapper

@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()