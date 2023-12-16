from profiler import measure_n_times_with_stats
from duckdb import DuckDBPyConnection
import dcdb

@measure_n_times_with_stats(1)
def q1_1(c: DuckDBPyConnection):
    dcdb.one_query(c)

@measure_n_times_with_stats(1)
def q2_1(c: DuckDBPyConnection):
    dcdb.two_query(c)

@measure_n_times_with_stats(1)
def q3_1(c: DuckDBPyConnection):
    dcdb.three_query(c)

@measure_n_times_with_stats(1)
def q4_1(c: DuckDBPyConnection):
    dcdb.four_query(c)