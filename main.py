from profiler import measure_time_once

@measure_time_once
def count_10000_powers_to_2():
    return [x**2 for x in range(10000)]

if __name__ == "__main__":
    res = count_10000_powers_to_2()
    print(f'It took {res} millis to complete {count_10000_powers_to_2.__name__}')