from functools import wraps

from src.sql import settings


def create_session():

    session = settings.Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def provide_session(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        arg_session = 'session'

        func_params = func.__code__.co_varnames
        session_in_args = arg_session in func_params and \
                          func_params.index(arg_session) < len(args)
        session_in_kwargs = arg_session in kwargs

        if session_in_kwargs or session_in_args:
            return func(*args, **kwargs)
        else:
            with create_session() as session:
                kwargs[arg_session] = session
                return func(*args, **kwargs)

    return wrapper

def parent(num):
    def func1():
        print("Hello from func - 1")

    def func2():
        print("Hello from func - 2")
    if num == 1:
        return func1
    else:
        return func2


def my_decorator(fun):

    def wrapper():
        print("Before func")

        fun()
        print("After func")
    return wrapper


@my_decorator
def say_hello():
    print("Hello from say_hello")
    print("Say bye")


if __name__ == '__main__':

    say_hello()


    generator = (x * x for x in range(3))
    for i in generator:
        print(i)

    def create_generator():
        for x in range(5):
            yield x * x

    result = create_generator()
    print(result.__class__)
    for i in result:
        print(i)

    first = parent(1)
    second = parent(2)
    first()
    second()
    print("---------------")
    # say = my_decorator(say_hello)
    # say()
