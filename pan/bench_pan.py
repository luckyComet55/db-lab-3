import pan.pan as pan
from profiler import measure_n_times_with_stats
from sqlalchemy import Connection
from const import measure_times

@measure_n_times_with_stats(measure_times)
def pandas_1(conn: Connection):
    pan.one_query(conn)

@measure_n_times_with_stats(measure_times)
def pandas_2(conn: Connection):
    pan.two_query(conn)

@measure_n_times_with_stats(measure_times)
def pandas_3(conn: Connection):
    pan.three_query(conn)

@measure_n_times_with_stats(measure_times)
def pandas_4(conn: Connection):
    pan.four_query(conn)