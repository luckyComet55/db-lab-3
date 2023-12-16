import psycopg as psc
from profiler import measure_n_times_with_stats

@measure_n_times_with_stats(1)
def ps2_1q_1(cursor):
    psc.ps2_one_query(cursor)

@measure_n_times_with_stats(1)
def ps2_2q_1(cursor):
    psc.ps2_two_query(cursor)

@measure_n_times_with_stats(1)
def ps2_3q_1(cursor):
    psc.ps2_three_query(cursor)

@measure_n_times_with_stats(1)
def ps2_4q_1(cursor):
    psc.ps2_four_query(cursor)