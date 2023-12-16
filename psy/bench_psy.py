import psy.psycopg as psc
from profiler import measure_n_times_with_stats

@measure_n_times_with_stats(1)
def psycopg2_1(cursor):
    psc.ps2_one_query(cursor)

@measure_n_times_with_stats(1)
def psycopg2_2(cursor):
    psc.ps2_two_query(cursor)

@measure_n_times_with_stats(1)
def psycopg2_3(cursor):
    psc.ps2_three_query(cursor)

@measure_n_times_with_stats(1)
def psycopg2_4(cursor):
    psc.ps2_four_query(cursor)