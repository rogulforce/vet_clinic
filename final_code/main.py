from schema_creation import connection, schema_creation

def main():
    """
    there will be execution of all the other code from final_code directory
    """
    conn = connection(password='8nqw$NS54Yh7FgWU')
    cur = conn.cursor()
    schema_creation(cur, "vet_clinic")


if __name__ == "__main__":
    main()
