from sqlalchemy import create_engine, Connection, text

def setup(db_params):
    engine = create_engine(f'postgresql+psycopg2://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}:{db_params["port"]}/{db_params["dbname"]}')
    conn = engine.connect()
    return conn

def cleanup(conn: Connection):
    conn.close()

def one_query(conn: Connection):
    q = text('SELECT pickup_location_id, count(*) FROM data GROUP BY 1')
    conn.execute(q)

def two_query(conn: Connection):
    q = text('SELECT passenger_count, avg(total_amount) FROM data GROUP BY 1')
    conn.execute(q)

def three_query(conn: Connection):
    q = text('SELECT passenger_count, extract(year from tpep_pickup_datetime), count(*) FROM data GROUP BY 1, 2')
    conn.execute(q)

def four_query(conn: Connection):
    q = text('SELECT passenger_count, extract(year from tpep_pickup_datetime), round(trip_distance) FROM data GROUP BY 1, 2, 3 ORDER BY 2, 3 DESC')
    conn.execute(q)