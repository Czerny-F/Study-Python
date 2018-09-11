from inspect import currentframe


def curry(func, *args, **kwargs):
    def _curried(*_args, **_kwargs):
        return func(*args, *_args, **{**kwargs, **_kwargs})

    return _curried


def curring(*args, **kwargs):
    def deco(func):
        def curried(*_args, **_kwargs):
            return func(*args, *_args, **{**kwargs, **_kwargs})
        return curried
    return deco


def noargs_deco(func):
    print('scope:', currentframe().f_code.co_name)

    def wrapper(*args, **kwargs):
        print('scope:', currentframe().f_code.co_name)
        return func(*args, **kwargs)

    return wrapper


def noret_deco(*dargs, **dkwargs):
    print('scope:', currentframe().f_code.co_name)
    print('args:', dargs, dkwargs)

    def wrapper(func):
        print('scope:', currentframe().f_code.co_name)
        print('func:', func)
        return func

    return wrapper


def full_deco(*dargs, **dkwargs):
    print('scope:', currentframe().f_code.co_name)
    print('args:', dargs, dkwargs)

    def deco(func):
        print('scope:', currentframe().f_code.co_name)
        print('func:', func)

        def wrapper(*args, **kwargs):
            print('scope:', currentframe().f_code.co_name)
            print('args:', args, kwargs)

            return func(*args, **kwargs)
        return wrapper
    return deco
