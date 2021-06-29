from schema_creation import connection, execute_sql_code
from tables_fulfill import fill
from report import make_report

def main():
    """
    there will be execution of all the other code from final_code directory
    """

    conn = connection(password='8nqw$NS54Yh7FgWU')
    # connect to Db
    # conn = connection()
    cur = conn.cursor()

    with open('../db_schema/db_creation.sql') as file:
        a = file.read()

    execs = a.split(';')

    for i, item in enumerate(execs):
        item = item.replace('\n', ' ')
        if len(item) == 0:
            pass
        else:
            execute_sql_code(cur, item)

    # data fill
    fill(cur)
    conn.commit()


if __name__ == "__main__":
    main()
    make_report()
    # with open('../db_schema/db_creation.sql') as file:
    #     a = file.read()
    # execs = a.split(';')
    # for i, item in enumerate(execs):
    #     execs[i] = item.replace('\n', '')
    #     print(execs[i])
