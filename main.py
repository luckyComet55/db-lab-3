from profiler import measure_n_times_with_stats
from stats import print_stats
import os
from dotenv import load_dotenv
from psycopg import setup, cleanup, ps2_one_query

def get_postgres_data():
    return {
        'dbname': os.environ.get('DB_NAME'),
        'user': os.environ.get('DB_USER'),
        'password': os.environ.get('DB_PASSWORD'),
        'host': os.environ.get('DB_HOST'),
        'port': os.environ.get('DB_PORT')
    }

def load_env():
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
    else:
        raise Exception('No .env file')

@measure_n_times_with_stats(100)
def ps2_1q_100(cursor):
    ps2_one_query(cursor)

@measure_n_times_with_stats(1000)
def ps2_1q_1000(cursor):
    ps2_one_query(cursor)

if __name__ == "__main__":
    load_env()
    db_params = get_postgres_data()
    [conn, cursor] = setup(db_params)
    stats = []
    stats.append(ps2_1q_100(cursor))
    stats.append(ps2_1q_1000(cursor))
    print_stats(stats)
    cleanup(conn, cursor)