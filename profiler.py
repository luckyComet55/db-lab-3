import time
from stats import get_stats

def measure_n_times_with_stats(n: int):
    def inner_func(func):
        def wrapper(*args, **kwargs):
            data = []
            f_output = None
            for _ in range(n):
                start = time.time()
                f_output = func(*args, **kwargs)
                end = time.time()
                res = (end-start)*1000
                data.append(res)
            stats = get_stats(data, func.__name__)
            return [f_output, stats]
        return wrapper
    return inner_func