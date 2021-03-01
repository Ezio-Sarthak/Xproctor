import sqlite3


# Create a function to connect to a database with SQLite
def sqlite_connect(db_name):
    """Connect to a database if exists. Create an instance if otherwise.
    Args:
        db_name: The name of the database to connect
    Returns:
        an sqlite3.connection object
    """
    try:
        # Create a connection
        conn = sqlite3.connect(db_name)
    except sqlite3.Error:
        print(f"Error connecting to the database '{db_name}'")
    finally:
        return conn

# Create a function that converts a digital file into binary
def convert_into_binary(file_path):
    with open(file_path, 'rb') as file:
        binary = file.read()

    return binary

def insert_file(file_name, db_name, table_name):
    try:
        # Establish a connection
        connection = sqlite_connect(db_name)
        print(f"Connected to the database `{db_name}`")

        # Create a cursor object
        cursor = connection.cursor()

        sqlite_insert_blob_query = f"""
        INSERT INTO {table_name} (name, data) VALUES (?, ?)
        """

        # Convert the file into binary
        binary_file = convert_into_binary(file_name)
        data_tuple = (file_name, binary_file)

        # Execute the query
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        connection.commit()
        print('File inserted successfully')
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to insert blob into the table", error)
    finally:
        if connection:
            connection.close()
            print("Connection closed")

def write_to_file(binary_code, file_name):
    # Convert binary to a proper file and store in memory
    with open(file_name, 'wb') as file:
        file.write(binary_code)
    print(f'Created file with name: {file_name}')

def retrieve_file(file_name, db_name, table_name):
    try:
        # Establish a connection
        connection = sqlite_connect(db_name)
        print(f"Connected to the database `{db_name}`")

        # Create a cursor object
        cursor = connection.cursor()

        sql_retrieve_file_query = f"""SELECT * FROM {table_name} WHERE name = ?"""
        cursor.execute(sql_retrieve_file_query, (file_name,))

        # Retrieve results in a tuple
        record = cursor.fetchone()
        # Save to a file
        write_to_file(record[1], record[0])
    except sqlite3.Error as error:
        print("Failed to insert blob into the table", error)
    finally:
        if connection:
            connection.close()
            print("Connection closed")
