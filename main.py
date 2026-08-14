from typing import Callable
import time
import functools
import inspect
import asyncio

def Hello():
    print("hello world!!!")

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


def deco(func: Callable):
    if inspect.iscoroutinefunction(func):
        async def wrapper(*args, **kwargs):
            print("this is async decorator")
            call = await func(*args, **kwargs)
            return call
        return wrapper
    else:
        def wrapper(*args, **kwargs):
            print("this is sync decorator")
            call = func(*args, **kwargs)
            return call
        return wrapper

@deco
async def sum(a: int, b: int):
    return a+b

@deco
def multiply(a: int, b: int):
    return a*b

result = asyncio.run(sum(5,4))
print(result)

print(multiply(1, 7))

print(multiply(4, 5))