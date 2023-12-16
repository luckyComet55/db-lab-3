from profiler import measure_n_times_with_stats
import alch.alch as alch
from sqlalchemy import Connection

@measure_n_times_with_stats(1)
def q1_1(conn: Connection):
    alch.one_query(conn)

@measure_n_times_with_stats(1)
def q2_1(conn: Connection):
    alch.two_query(conn)

@measure_n_times_with_stats(1)
def q3_1(conn: Connection):
    alch.three_query(conn)

@measure_n_times_with_stats(1)
def q4_1(conn: Connection):
    alch.four_query(conn)