# Imports
import sqlite3
# Establish connection to database
conn = sqlite3.connect('python.db')
c = conn.cursor()
# Create global variable name
name = ""

def create_table():
  global name # Retrieve global variable name
  c.execute('CREATE TABLE IF NOT EXISTS RecordONE (Number REAL, Name TEXT)') # DB execution
  name = input("What is your name?") # Input to global variable name

def data_entry():
  number = "1234"
  c.execute("INSERT INTO RecordONE (Number, Name) VALUES(?, ?)", (number, name)) # Execute sql

# Call functions
create_table()
data_entry()

# Save changes to DB
conn.commit()

# Close connection
c.close()
conn.close()