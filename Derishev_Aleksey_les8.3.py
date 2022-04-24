from functools import wraps


def type_logger(num=0):
    def logg(func):
        @wraps(func)
        def wrapper(*argv):
            if num > 0:
                return 'calc_cube(' + ", ".join([f"{func(x)}:{type(func(x))}" for x in argv]) + ")"
            else:
                return "calc_cube(" + ", ".join([str(func(x)) for x in argv]) + ")"
        return wrapper
    return logg


@ type_logger(2)
def calc_cube(x):
    return x ** 3

if __name__ == '__main__':
    print(calc_cube(5, 12, 45))