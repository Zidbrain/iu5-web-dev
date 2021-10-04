from typing import Generator
from random import randint

def gen_random(amount: int, begin: int, end: int) -> Generator[int, None, None]:
    for i in range(amount):
        yield randint(begin, end)