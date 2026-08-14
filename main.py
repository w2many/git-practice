import inspect
import asyncio
from typing import Callable

def Hello():
    print("hello!!!")

def get_user():
    return {"id": 1, "name": "user"}

def get_users():
    return [{"id": 1, "name": "user"},
            {"id": 2, "name": "user2"},
            {"id": 3, "name": "user3"}]


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

print(multiply(1,7))