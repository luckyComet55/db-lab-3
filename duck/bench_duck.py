from profiler import measure_n_times_with_stats
from duckdb import DuckDBPyConnection
import duck.dcdb as dcdb

@measure_n_times_with_stats(1)
def duckdb_1(c: DuckDBPyConnection):
    dcdb.one_query(c)

@measure_n_times_with_stats(1)
def duckdb_2(c: DuckDBPyConnection):
    dcdb.two_query(c)

@measure_n_times_with_stats(1)
def duckdb_3(c: DuckDBPyConnection):
    dcdb.three_query(c)

@measure_n_times_with_stats(1)
def duckdb_4(c: DuckDBPyConnection):
    dcdb.four_query(c)