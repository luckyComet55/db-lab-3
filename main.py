from profiler import measure_n_times_with_stats
from stats import print_stats

@measure_n_times_with_stats(2020)
def count_10000_powers_to_2():
    return [x**2 for x in range(10000)]

if __name__ == "__main__":
    [res, stats] = count_10000_powers_to_2()
    print_stats([stats])
    