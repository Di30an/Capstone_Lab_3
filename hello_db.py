import sqlite3

# Creates or opens connection to db file

conn = sqlite3.connect('first_db.sqlite')

# Create a table
conn.execute('create table phones  (brand text, version interger)')

# Add some data 
conn.execute('insert into phones values ("Android", 5)')
conn.execute('insert into phones values ("iPhone", 6)')

conn.commit()


# Excute a query. execute() returns a cusor
# Can use the sursor in a loop to read each row in turn.
for row in conn.execute('select * from phones'):
    print(row)

conn.execute('drop table phones') # Delete table

conn.commit() # Ask the database to save changes - dont forget!

conn.close() # And close connection. 

