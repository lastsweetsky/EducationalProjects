from colorama import Fore
from functools import wraps


def catchErrorInFunction(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            return res
        except Exception as e:
            print(f"{Fore.RED} Exception in {func.__name__}:{Fore.BLUE} {e}")

    return wrapper
