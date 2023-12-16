from stats import init_dataframe, save_2_file
import os
from dotenv import load_dotenv
import pan.pan as pan
import pan.bench_pan as bench_pan

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
    df = init_dataframe()
    csv_path = os.environ.get("CSV_PATH")
    db_params = get_postgres_data()
    conn = pan.setup(db_params)
    stats = []
    stats.append(bench_pan.pandas_1(conn))
    for s in stats:
        print(s)
        df.loc[len(df)] = s
        print(df)
    save_2_file(df, csv_path)
    pan.cleanup(conn)