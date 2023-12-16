import pan.pan as pan
from profiler import measure_n_times_with_stats
from sqlalchemy import Connection

@measure_n_times_with_stats(1)
def q1_1(conn: Connection):
    pan.one_query(conn)

@measure_n_times_with_stats(1)
def q2_1(conn: Connection):
    pan.two_query(conn)

@measure_n_times_with_stats(1)
def q3_1(conn: Connection):
    pan.three_query(conn)

@measure_n_times_with_stats(1)
def q4_1(conn: Connection):
    pan.four_query(conn)