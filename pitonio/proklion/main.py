from functools import singledispatch, update_wrapper


class ResolverManual(object):
    def multiply(self, *, a=None, b=None):
        if a is None and b is None:
            print('Method called without arguments')
            return

        if a is None and b is not None:
            print('b is provided')
            return b

        if a is not None and b is None:
            print('a is provided')
            return a

        print('Both values are present. Product is')
        return a*b


@singledispatch
def multiply2(a, b):
    print('Generic function for {a}, {b}'.format(a=a, b=b))


def multiply_float(a: float, b: float):
    print('Multiplying two floats: {a}x{b}'.format(a=a, b=b))
    return a*b


def multiply_lists(a: list, b: list):
    print('Cartesian product of {a} and {b}'.format(a=a, b=b))
    return sum([val_a*val_b for val_a in a for val_b in b])


multiply2.register(float, multiply_float)
multiply2.register(list, multiply_lists)


def methdispatch(func):
    dispatcher = singledispatch(func)

    def wrapper(*args, **kw):
        return dispatcher.dispatch(args[1].__class__)(*args, **kw)

    wrapper.register = dispatcher.register
    update_wrapper(wrapper, func)
    return wrapper


class ResolverMethDispatch(object):
    @methdispatch
    def multiply(self, a, b):
        print('Generic method for {a}, {b}'.format(a=a, b=b))
        return '{a}x{b}'.format(a=a, b=b)

    @multiply.register(int)
    def multiply_int(self, a, b):
        print('Multiplying two ints: {a}x{b}'.format(a=a, b=b))
        return a*b

    @multiply.register(str)
    def multiply_str(self, a, b):
        print('Making string "{a}" {b} characters long'.format(a=a, b=b))
        return a*b


class ResolverGetatt(object):
    def _multiply(self, a, b):
        print('Generic method for {a}, {b}'.format(a=a, b=b))
        return '{a}x{b}'.format(a=a, b=b)

    def __getattr__(self, item, *args, **kwargs):
        if item == 'multiply':
            print('here', args, kwargs)
            return self._multiply
        raise AttributeError('No such attribute {}'.format(item))

    def __getattribute__(self, item):
        print(item)


class ResolverGetattribute(object):
    def _multiply(self, a, b):
        print('Generic method for {a}, {b}'.format(a=a, b=b))
        return '{a}x{b}'.format(a=a, b=b)

    def __getattribute__(self, item, *args, **kwargs):
        print(item, args, kwargs)
        return super().__getattribute__(item)


class _multiply4(object):
    def __call__(self, *args, **kwargs):
        if len(args) == 2:
            a, b = args
            if isinstance(a, int) and isinstance(b, int):
                return self._multiply_int(a, b)
            elif isinstance(a, float) and isinstance(b, float):
                return self._multiply_float(a, b)
            elif isinstance(a, str) and isinstance(b, int):
                return self._multiply_str(a, b)
        return self._multiply_generic(*args)

    def _multiply_generic(self, *args):
        print('Generic method for arguments: {}'.format(args))

    def _multiply_float(self, a: float, b: float):
        print('Multiplying two floats: {a}x{b}'.format(a=a, b=b))
        return a*b

    def _multiply_int(self, a: int, b: int):
        print('Multiplying two ints: {a}x{b}'.format(a=a, b=b))
        return a*b

    def _multiply_str(self, a: str, b: int):
        print('Making string "{a}" {b} characters long'.format(a=a, b=b))
        return a*b
multiply4 = _multiply4()


class multiply5(object):
    def __new__(cls, *args, **kwargs):
        if len(args) == 2:
            a, b = args
            if isinstance(a, int) and isinstance(b, int):
                return cls._multiply_int(a, b)
            elif isinstance(a, float) and isinstance(b, float):
                return cls._multiply_float(a, b)
            elif isinstance(a, str) and isinstance(b, int):
                return cls._multiply_str(a, b)
        return cls._multiply_generic(*args)

    @classmethod
    def _multiply_generic(cls, *args):
        print('Generic method for arguments: {}'.format(args))

    @classmethod
    def _multiply_float(cls, a: float, b: float):
        print('Multiplying two floats: {a}x{b}'.format(a=a, b=b))
        return a*b

    @classmethod
    def _multiply_int(cls, a: int, b: int):
        print('Multiplying two ints: {a}x{b}'.format(a=a, b=b))
        return a*b

    @classmethod
    def _multiply_str(cls, a: str, b: int):
        print('Making string "{a}" {b} characters long'.format(a=a, b=b))
        return a*b


def main():
    # r1 = ResolverManual()
    # multiply1 = r1.multiply
    # print(multiply1())
    # print(multiply1(a=1))
    # print(multiply1(b=2))
    # print(multiply1(a=1, b=2))

    r3 = ResolverMethDispatch()
    multiply3 = r3.multiply
    print(multiply3([3], [4]))
    print(multiply3(3, 4))
    print(multiply3('a', 4))

    # print(multiply2(3, 4))
    # print(multiply2(4.1, 5.2))
    # print(multiply2([1, 2, 3], [4, 5, 6]))

    # print(multiply4())
    # print(multiply4(5, 6))
    # print(multiply4(8.0, 9.1))
    # print(multiply4('d', 4))

    # print(multiply5(7, 10))
    # print(multiply5(8.0, 9.0))
    # print(multiply5('b', 4))
    # print(multiply5(3, 4, 5))


if __name__ == '__main__':
    main()
