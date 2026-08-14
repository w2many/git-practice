from typing import Callable
import time

def Hello():
    print("hello!!!")

def get_user():
    return {"id": 1, "name": "user"}

def get_users():
    return [{"id": 1, "name": "user"},
            {"id": 2, "name": "user2"},
            {"id": 3, "name": "user3"}]


def deco(func: Callable):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        call = func(*args, **kwargs)
        end_time = time.time()
        print(f"функция {func.__name__} выполнялась {end_time-start_time}")
        return call
    return wrapper

@deco
def func1(a: int, b: int):
    return a + b

print(func1(4,5))