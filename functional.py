def curry(func, *args, **kwargs):
    def _curried(*_args, **_kwargs):
        return func(*args, *_args, **{**kwargs, **_kwargs})

    return _curried
