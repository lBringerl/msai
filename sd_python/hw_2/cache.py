from collections import deque


def update_wrapper(wrapper, func, assignments, updates):
    for assignment in assignments:
        try:
            setattr(wrapper, assignment, getattr(func, assignment))
        except AttributeError:
            pass
    for update in updates:
        getattr(wrapper, update).update(getattr(func, update, {}))
    return wrapper


def cache(cache_size):
    assignments = ('__module__',
                   '__name__',
                   '__qualname__',
                   '__doc__',
                   '__annotations__')
    updates = ('__dict__',)

    def _cache_wrapper(func):
        _cache = {}
        _key_queue = deque([None] * cache_size)
        sentinel = object()

        def hash_args(args, kwargs):
            res_args = args
            if kwargs:
                res_args += (sentinel,)
                for item in kwargs.items():
                    res_args += item
            return hash(res_args)

        def wrapper(*args, **kwargs):
            key = hash_args(args, kwargs)
            cached_result = _cache.get(key, sentinel)
            if cached_result is not sentinel:
                return cached_result
            _cache[key] = func(*args, **kwargs)
            _key_queue.appendleft(key)
            to_remove = _key_queue.pop()
            if to_remove:
                _cache.pop(to_remove)
            return _cache[key]
        return update_wrapper(wrapper, func,
                              assignments=assignments,
                              updates=updates)
    return _cache_wrapper


@cache(2)
def check(*args, **kwargs):
    return 1


class SomeObj:
    a = 1
    b = 2

    def __init__(self, a):
        self.a = a
    
    def __hash__(self):
        return hash(self.a)


@cache(2)
def foo(value):
    """CHECK FUNCTION

    :param args:
    :param kwargs:
    :return:
    """
    # __doc__ = 'Some description'
    print('calculate foo for {}'.format(value))
    return value


if __name__ == '__main__':
    # check(1, 2, 3, a=1, b=2, c=3, o=SomeObj(1))
    # check(1, 2, 3, a=1, b=2, c=3, o=SomeObj(2))
    # check(1, 2, 3, a=1, b=2, c=3, o=SomeObj(2))
    # check(1, 2, 3, a=1, b=2, c=3, o=SomeObj(1))
    # check(1, 2, 3, a=1, b=2, c=3, o=SomeObj(1))
    # check(1, 2, 3, a=1, b=2, c=3, o=SomeObj(2))

    foo(1)
    foo(2)
    foo(1)
    foo(2)
    foo(3)
    foo(1)
    print(foo.__doc__)
