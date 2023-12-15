import time

def measure_time_once(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        return (end-start)*1000
    
    return wrapper