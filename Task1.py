import time

def decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print('Execution time:', end_time - start_time)
    return wrapper

@decorator
def func():
    time.sleep(2)

func()