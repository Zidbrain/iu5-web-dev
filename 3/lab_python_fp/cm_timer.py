from typing import ContextManager
import time
from contextlib import contextmanager

@contextmanager
def cm_timer_2():
    tick = time.time()
    yield None
    print('time: {}'.format(time.time() - tick))

class cm_timer_1(ContextManager):
    def __init__(self):
        pass
        
    def __enter__(self):
        self._time = time.time()
        
    def __exit__(self, exp_type, exp_value, traceback):
        if exp_type is not None:
            print(exp_type, exp_value, traceback)
        else:
            print("time: {}".format(time.time() - self._time))

if __name__ == '__main__':
    with cm_timer_1():
        time.sleep(1.2)
    with cm_timer_2():
        time.sleep(1.5)