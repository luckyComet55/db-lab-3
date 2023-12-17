from stats import init_dataframe, save_2_file
import os
from dotenv import load_dotenv
import pan.pan as pan
import pan.bench_pan as bench_pan
import sqlt.sqlite as sqlt
import sqlt.bench_sqlt as bench_sqlt
import psy.psycopg as psy
import psy.bench_psy as bench_psy
import duck.dcdb as duck
import duck.bench_duck as bench_duck
import alch.alch as alch
import alch.bench_alch as bench_alch

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

if __name__ == '__main__':
    load_env()
    df = init_dataframe()
    csv_path = os.environ.get('CSV_PATH')
    db_params = get_postgres_data()
    sqlite_path = os.environ.get('SQLT_DATA_SOURCE')
    duck_path = os.environ.get('DUCK_DATA_SOURCE')
    stats = []

    conn_pan = pan.setup(db_params)
    [conn_psy, curs_psy] = psy.setup(db_params)
    [conn_sqlt, curs_sqlt] = sqlt.setup(sqlite_path)
    conn_duck = duck.setup(duck_path)
    conn_alch = alch.setup(db_params)

    def save_data(df, data):
        for d in data:
            df.loc[len(df)] = d
        save_2_file(df, csv_path)

    def benchmarker(b_pan, b_psy, b_sqlt, b_d, b_sqla, st):
        st.append(b_pan(conn_pan))
        print('Done pandas')
        st.append(b_psy(curs_psy))
        print('Done psycopg')
        st.append(b_sqlt(curs_sqlt))
        print('Done sqlite')
        st.append(b_d(conn_duck))
        print('Done duckdb')
        st.append(b_sqla(conn_alch))
        print('Done sqlalchemy')
        return st

    stats = benchmarker(bench_pan.pandas_1, bench_psy.psycopg2_1, bench_sqlt.sqlite_1, bench_duck.duckdb_1, bench_alch.sqlalchemy_1, stats)
    save_data(df, stats)
    stats = benchmarker(bench_pan.pandas_2, bench_psy.psycopg2_2, bench_sqlt.sqlite_2, bench_duck.duckdb_2, bench_alch.sqlalchemy_2, stats)
    save_data(df, stats)
    stats = benchmarker(bench_pan.pandas_3, bench_psy.psycopg2_3, bench_sqlt.sqlite_3, bench_duck.duckdb_3, bench_alch.sqlalchemy_3, stats)
    save_data(df, stats)
    stats = benchmarker(bench_pan.pandas_4, bench_psy.psycopg2_4, bench_sqlt.sqlite_4, bench_duck.duckdb_4, bench_alch.sqlalchemy_4, stats)
    save_data(df, stats)

    alch.cleanup(conn_alch)
    duck.cleanup(conn_duck)
    sqlt.cleanup(conn_sqlt, curs_sqlt)
    psy.cleanup(conn_psy, curs_psy)
    pan.cleanup(conn_pan)