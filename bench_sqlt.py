from sqlite3 import Cursor
import sqlite as sqlt
from profiler import measure_n_times_with_stats

@measure_n_times_with_stats(1)
def sqlt_1q_1(c: Cursor):
    sqlt.sqlt_one_query(c)

@measure_n_times_with_stats(1)
def sqlt_2q_1(c: Cursor):
    sqlt.sqlt_two_query(c)

@measure_n_times_with_stats(1)
def sqlt_3q_1(c: Cursor):
    sqlt.sqlt_three_query(c)

@measure_n_times_with_stats(1)
def sqlt_4q_1(c: Cursor):
    sqlt.sqlt_four_query(c)