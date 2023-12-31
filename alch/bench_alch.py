from profiler import measure_n_times_with_stats
import alch.alch as alch
from sqlalchemy import Connection
from const import measure_times

@measure_n_times_with_stats(measure_times)
def sqlalchemy_1(conn: Connection):
    alch.one_query(conn)

@measure_n_times_with_stats(measure_times)
def sqlalchemy_2(conn: Connection):
    alch.two_query(conn)

@measure_n_times_with_stats(measure_times)
def sqlalchemy_3(conn: Connection):
    alch.three_query(conn)

@measure_n_times_with_stats(measure_times)
def sqlalchemy_4(conn: Connection):
    alch.four_query(conn)