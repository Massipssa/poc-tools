import sys


# enclosing
def outer_fun():
    test_var = 10

    def inner_fun():
        test_var = 10


var = "this is global "


def get_fun_info(test_arg):
    hello = "hello"
    x = 1 + 2


if __name__ == '__main__':

    print(get_fun_info.__code__.co_varnames)
    print(get_fun_info.__code__.co_argcount)
    print(get_fun_info.__code__.co_consts)
    print(get_fun_info.__code__.co_name)
    print(__name__)
    print(dir())

    print(var)

    keys = sys.__dict__.keys()
    print(keys)

    import builtins
    print(len(dir(__builtins__)))
    print(builtins.sum([1, 2, 3, 4]))
    print(sum([1, 2, 3, 4]))

    # dot notation
    # ps = sys.ps1
    # subscription operation
    # sys.__dict__['ps1']
