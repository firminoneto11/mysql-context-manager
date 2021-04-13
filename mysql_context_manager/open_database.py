import mysql.connector as connector


class OpenDB:

    def __init__(self, host, user, passwd, database):
        # Saving the arguments passed into attributes
        self.host = host
        self.user = user
        self.passwd = passwd
        self.database = database

        # Saving the imported driver connector for mysql into an attribute
        self.driver = connector

        # Authenticating the connection
        self.connection = self.driver.connect(
            host=self.host,
            user=self.user,
            passwd=self.passwd,
            database=self.database
        )

        # Generating the cursor
        self.cursor = self.connection.cursor()

    def __enter__(self):
        """
        This __enter__ method gets and returns the cursor created by the OpenDB class for the context manager to use.
        :return: The MySQL cursor.
        """
        return self.cursor

    def __iter__(self):
        """
        This __iter__ method works as an iterator because sometimes we need to return something from the database when
        it's needed.
        :return: The current item in the iteration
        """
        for item in self.cursor:
            yield item

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        This __exit__ method is called when the context manager is closed. It checks the execution value to see if it
        is instance of the Exception class. If it is, it rollbacks the SQL commands passed and if isn't, it commits the
        changes.
        :param exc_type: Execution type. It's passed by the python interpreter when exiting the context manager.
        :param exc_val: Execution value. It's passed by the python interpreter when exiting the context manager.
        :param exc_tb: Execution traceback. It's passed by the python interpreter when exiting the context manager.
        :return: None
        """
        # Closing the cursor
        self.cursor.close()

        # Checking if the execution value returned is instance of Exception class, meaning that if any errors occurred
        # during the execution of the SQL commands within the context manager, it will take actions based on what
        # happened

        # If the execution value is instance of the Exception class, this will rollback all the changes made within the
        # context manager
        if isinstance(exc_val, Exception):
            self.connection.rollback()
        # If the execution value isn't an instance of the Exception class, this will commit the changes made within the
        # context manager.
        else:
            self.connection.commit()

        # Closing the connection.
        self.connection.close()


# Standard usage
if __name__ == '__main__':
    db_info = {
        'host': 'insert here your host name',
        'user': 'insert here your mysql server user name',
        'passwd': 'insert here your mysql server password',
        'database': 'insert here your database name that you want to use'
    }

    with OpenDB(**db_info) as cursor:
        cursor.execute('Any SQL command')
