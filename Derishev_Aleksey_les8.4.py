from functools import wraps


def val_checker(func_filter):
    def check(func):
        @wraps(func)
        def wrapper(x):
            if func_filter(x):
                return func(x)
            raise ValueError
        return wrapper
    return check


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3

if __name__ == '__main__':
    print(calc_cube(5))