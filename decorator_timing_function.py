import time


def time_me(func):
    """Decorator function to time the runtime of another function"""
    def wrapper(*args, **kwargs):
        """Wrapper function of the decurator"""
        _start = time.time()
        _ret = func(*args, **kwargs)
        print(f"Executed {func.__name__} with args: {args} kwargs: {kwargs} in {round(time.time() - _start, 2)} seconds")
        return _ret
    return wrapper


@time_me
def example_function(some_arg=None):
    print("Function start")
    time.sleep(2)
    print("Function end")
    return some_arg**2


if __name__ == "__main__":
    some_arg = example_function(5)
    print(f"Example function returned: {some_arg}")
