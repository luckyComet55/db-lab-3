from profiler import measure_n_times_with_stats
from stats import print_stats
import os
from dotenv import load_dotenv
import alch.alch as alch
import alch.bench_alch as bench_alch
import psy.psycopg as psy

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

times_to_execute = 10

if __name__ == "__main__":
    load_env()
    db_params = get_postgres_data()
    conn = alch.setup(db_params)
    stats = []
    stats.append(bench_alch.q1_1(conn))
    stats.append(bench_alch.q2_1(conn))
    stats.append(bench_alch.q3_1(conn))
    stats.append(bench_alch.q4_1(conn))
    print_stats(stats)
    alch.cleanup(conn)