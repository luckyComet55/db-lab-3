from profiler import measure_n_times_with_stats
from stats import print_stats
import os
from dotenv import load_dotenv
import psycopg as psc

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

@measure_n_times_with_stats(times_to_execute)
def ps2_1q_1(cursor):
    psc.ps2_one_query(cursor)

@measure_n_times_with_stats(times_to_execute)
def ps2_2q_1(cursor):
    psc.ps2_two_query(cursor)

@measure_n_times_with_stats(times_to_execute)
def ps2_3q_1(cursor):
    psc.ps2_three_query(cursor)

@measure_n_times_with_stats(times_to_execute)
def ps2_4q_1(cursor):
    psc.ps2_four_query(cursor)

if __name__ == "__main__":
    load_env()
    db_params = get_postgres_data()
    [conn, cursor] = psc.setup(db_params)
    stats = []
    stats.append(ps2_1q_1(cursor))
    stats.append(ps2_2q_1(cursor))
    stats.append(ps2_3q_1(cursor))
    stats.append(ps2_4q_1(cursor))
    print_stats(stats)
    psc.cleanup(conn, cursor)