import psycopg2

def setup(db_params):
    conn = None
    cursor = None
    try:
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()
    except psycopg2.Error as e:
        print('Ошибка при подключении к базе данных', e)
    return [conn, cursor]

def cleanup(conn, cursor):
    try:
        cursor.close()
        conn.close()
    except psycopg2.Error as e:
        print('Ошибка при закрытии подключения к базе данных', e)


def ps2_one_query(cursor):
    cursor.execute('SELECT pickup_location_id, count(*) FROM data GROUP BY 1')