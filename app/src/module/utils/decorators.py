# TODO: implement decorator that allows for a decorator to take parameters, (stackoverflow python bootcamp)

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