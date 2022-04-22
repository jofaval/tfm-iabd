# TODO: implement decorator that allows for a decorator to take parameters, (stackoverflow python bootcamp)
import functools, time

def logger(filename:str = 'log.txt') -> None:
    """
    Log any sort of error

    filename : str
        The name of the file in which to store the message

    returns None
    """
    raise NotImplementedError()

def error_boundary(use_logger: bool = False, propagate: bool = False) -> None:
    """
    Prevent any sort of error

    use_logger : bool
        Log the error? It won't by default
    propagate : bool
        Raise another error, or even the same? It won't by default

    returns None
    """
    raise NotImplementedError()

def benchmark(func):
    """
    Print the runtime of the decorated function

    Reference:
        https://realpython.com/primer-on-python-decorators/#timing-functions

    returns None
    """
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time

        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value

    return wrapper_timer