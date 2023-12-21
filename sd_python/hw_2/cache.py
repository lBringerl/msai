# from functools import cache
from functools import wraps


def cache(func):
    _cache = {}
    sentinel = object()

    def hash_args(args, kwargs):
        res_args = args
        if kwargs:
            res_args += (sentinel,)
            for item in kwargs.items():
                res_args += item
        return hash(res_args)

    @wraps(func)
    def wrapper(*args, **kwargs):
        hashed_args = hash_args(args, kwargs)
        cached_result = _cache.get(hashed_args, sentinel)
        if cached_result is not sentinel:
            print('HIT!')
            return cached_result
        _cache[hashed_args] = func(*args, **kwargs)
        print('MISS!')
        return func(*args, **kwargs)
    return wrapper


@cache
def check(*args, **kwargs):
    return 1


class SomeObj:
    a = 1
    b = 2

    def __init__(self, a):
        self.a = a
    
    def __hash__(self):
        return hash(self.a)


if __name__ == '__main__':
    check(1, 2, 3, a=1, b=2, c=3, o=SomeObj(1))
    check(1, 2, 3, a=1, b=2, c=3, o=SomeObj(2))
    check(1, 2, 3, a=1, b=2, c=3, o=SomeObj(2))
