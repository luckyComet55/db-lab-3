import pandas as pd
import alch.alch as alch
from sqlalchemy import Connection

def setup(db_params):
    return alch.setup(db_params)

def cleanup(conn: Connection):
    conn.close()

def one_query(conn: Connection):
    pd.read_sql('SELECT pickup_location_id, count(*) FROM data GROUP BY 1', conn)

def two_query(conn: Connection):
    pd.read_sql('SELECT passenger_count, avg(total_amount) FROM data GROUP BY 1', conn)

def three_query(conn: Connection):
    pd.read_sql('SELECT passenger_count, extract(year from tpep_pickup_datetime), count(*) FROM data GROUP BY 1, 2', conn)

def four_query(conn: Connection):
    pd.read_sql('SELECT passenger_count, extract(year from tpep_pickup_datetime), round(trip_distance) FROM data GROUP BY 1, 2, 3 ORDER BY 2, 3 DESC', conn)