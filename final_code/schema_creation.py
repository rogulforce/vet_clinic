import mariadb
import sys


def connection(user: str = "root", password: str = "admin",
               host: str = "localhost", port: int = 3306, **kwargs):
    """ Connection function

    Args:
        user (str): Defaults to 'root'
        password (str): Defaults to 'admin'
        host (str): Defaults to 'localhost'
        port (int): Defaults to 3306
        **kwargs (str): database=, if you want to connect to exact database.

    Returns (mariadb.connect()): current connection
    """
    try:
        conn = mariadb.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            **kwargs
        )
        print(f'connected to @{host} on port {port}')

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    return conn


def schema_creation(cursor, name: str = 'vet_clinic'):
    """ function creating new schema.

    Args:
        cursor (mariadb.connect().cursor()): execution cursor
        name: schema name
    """
    cursor.execute(f"CREATE OR REPLACE SCHEMA {name};")


def create_tables(cursor, database):
    """ function creating tables. TUTAJ TRZEBA ZROBIĆ ŁADNE TABELKI!!!!
    Args:
        cursor (mariadb.connect().cursor()): execution cursor
    """
    # PRZYKŁADOWA
    cursor.execute(f"CREATE OR REPLACE TABLE {database}.sample (id INT, name TEXT);")
    cursor.execute(f"CREATE OR REPLACE TABLE {database}.sample2 (id INT, name TEXT);")
    # itd


def insert_to_tables(cursor, database):
    # tutaj dodatkowe argumenty, co wrzucać kiedy itd
    for i in range(10):
        cursor.execute(f"INSERT INTO {database}.sample (id, name) VALUES ({i},'hwdp')")


def exectute_sql_code(cursor, code: str):
    """ function executing given text

    Args:
        cursor (mariadb.connect().cursor()): execution cursor
        code: SQL code to execute
    """
    cursor.execute(code)


if __name__ == "__main__":
    conn = connection()
    cur = conn.cursor()
    schema_creation(cur, "vet_clinic")
    create_tables(cur, "vet_clinic")
    insert_to_tables(cur, "vet_clinic")
    cur.execute("SELECT * FROM vet_clinic.sample")
    for item in cur:
        print(item)
