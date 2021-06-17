from schema_creation import connection, schema_creation, exectute_sql_code


def main():
    """
    there will be execution of all the other code from final_code directory
    """
    # conn = connection(password='8nqw$NS54Yh7FgWU')

    # connect to Db
    conn = connection()
    cur = conn.cursor()

    # create or replace schema and create tables
    try:
        exectute_sql_code(cur, 'DROP SCHEMA vet_clinic;')
    except:
        pass

    with open('../db_schema/db_creation.sql') as file:
        a = file.read()

    execs = a.split(';')

    for i, item in enumerate(execs):
        item = item.replace('\n', '')
        if len(item) == 0:
            pass
        else:
            print(item)
            exectute_sql_code(cur, item)



if __name__ == "__main__":
    main()
    # with open('../db_schema/db_creation.sql') as file:
    #     a = file.read()
    # execs = a.split(';')
    # for i, item in enumerate(execs):
    #     execs[i] = item.replace('\n', '')
    #     print(execs[i])