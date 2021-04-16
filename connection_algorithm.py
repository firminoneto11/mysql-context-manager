import mysql.connector as connector

# Getting the necessary info
info = {
    'host': 'hostname',
    'user': 'username',
    'passwd': 'password',
    'database': 'database_name'
}

# Try to connect to the database. Unpacking the dictionary.
try:
    connection = connector.connect(**info)
# Showing an error message if the connection is not completed successfully
except Exception as error:
    print(f'An error occurred while trying to connect to the database with the provided info. More details about it:'
          f'\n{error}')
# Creating the cursor if everything goes ok
else:
    cursor = connection.cursor()
    # Trying to execute any transactions
    try:
        """
        Here we execute our transactions -
        """
        cursor.execute('Any MySQL command')
    # Rollback the database changes if any errors are encountered
    except Exception as error2:
        print(f'An error occurred while trying to complete the transaction. More details about it:\n{error2}')
        connection.rollback()
    # Commit the changes if everything goes ok
    else:
        connection.commit()
    # Closing both the cursor and the database connection
    finally:
        cursor.close()
        connection.close()
