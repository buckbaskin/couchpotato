from couchpotato.very.lazy import Lazy as LazyStandin

def lazy(func):
    def new_function(*args, **kwargs):
        return LazyStandin(func, args, kwargs)
    new_function.__name__ = func.__name__
    return new_function

