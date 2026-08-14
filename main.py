from typing import Callable
import time
import functools

def Hello():
    print("hello!!!")

def get_user():
    return {"id": 1, "name": "user"}

def get_users():
    return [{"id": 1, "name": "user"},
            {"id": 2, "name": "user2"},
            {"id": 3, "name": "user3"}]


def repeat(times: int):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for i in range(times):
                start_time = time.time()

                call = func(*args, **kwargs)
                results.append(call)
                
                end_time = time.time()

                print(f"функция {func.__name__} выполнялась {end_time-start_time}")
            return results
        return wrapper
    return decorator

@repeat(3)
def func1(a: int, b: int):
    return a + b

print(func1(4,5))