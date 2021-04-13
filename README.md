<h1>mysql-context-manager</h1>
<h2>A class designed to work as a context manager to connect to a MySQL database and create a cursor.</h2>
<hr/>
<!--Intro-->
<div align='center'>
<h3>👻 Why did you made this context manager? 👻</h3>
</div>
<p>When connecting to the MySQL database, often we have to create a connection, create a cursor, execute the queries and then close the cursor and connection. This process can be automated and simplified with via context manager. Also, sometimes, we can forget to close the connections and that can lead to a major bug. So, with all of these things, i did some research and foud that the 'magic methods' could help in the design of the class that will work as context manager.</p>
<hr/>
<!--Requirements-->
<div align='center'>
<h3>🤔 How can i use it? 🤔</h3>
</div>
<p>Untill the day i developed the code, there wasn't a MySQL connector for Python 3.9+ versions, so this context manager should work only for the MySQL supported Python versions. In my case, i used the 3.8.9 Python version.<br/>
So the requirements are:

- [x] Supported Python version by MySQL database. I used 3.8.9, but check your MySQL installer
- [x] MySQL connector

Once more, make sure that your Python version is supported by the MySQL database, and with that being said, you can use the PIP to install the MySQL connector. Type the following command line into your terminal:

```powershell
pip install mysql-connector-python
```

If you encounter any errors when importing the 'mysql.connector' in the source code editor, open up your MySQL installer and also install their version of Python connector.
</p>
<hr/>
<!--Usage-->
<div align='center'>
<h3>🤔 How should i use it? 🤔</h3>
</div>
<p>The usage of this context manager is pretty simple and it works as any other function or class designed to work on a conext manager.Look at the example bellow:<br/>

```python

# Create a dictionary with your database info
database_info = {
    'host': 'host name',
    'user': 'user name',
    'passwd': 'password',
    'database': 'database name'
}

# Creating the cursor in the context manager. You can
# also unpack all the values from the dictionary and
# pass them as arguments for the class
with OpenDB(**database_info) as cursor:
    # Execute your queries/actions here
    cursor.execute('Any SQL command')

# Now when the code reaches out of the context manager, 
# if it encounters any erros it will rollback all the 
# changes, else it will commit the changes and close 
# the cursor and connection!
```
</p>
<hr/>
<!--Author-->
<div align='center'>
<h3>👾 Author 👾</h3>
</div>
<p>Made with ❤ by <a href='https://github.com/firminoneto11'>Firmino Neto</a>.</p>
