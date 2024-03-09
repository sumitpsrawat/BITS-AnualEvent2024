import psycopg2

def connect_to_db():
    try:
        connection = psycopg2.connect(
            dbname="your_database_name",
            user="your_database_user",
            password="your_database_password",
            host="your_database_host",
            port="your_database_port"
        )
        return connection
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

def close_connection(connection):
    if connection:
        connection.close()
