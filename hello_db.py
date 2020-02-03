import sqlite3

# Creates or opens connection to db file
conn = sqlite3.connect('first_db.sqlite')
conn.row_factory = sqlite3.Row  # Upgrade row_factory

# Create a table
conn.execute('create table if not exists phones  (brand text, version interger)')

# Add some data 
conn.execute('insert into phones values ("Android", 5)')
conn.execute('insert into phones values ("iPhone", 6)')

conn.commit()  # Finalize updates

for row in conn.execute('select * from phones'):
    print(row)

for row in conn.execute('select * from phones'):
    print (row[0]) # The brand
    print (row[1]) # The version


conn.commit() # Ask the database to save changes - dont forget!

for row in conn.execute('select * from phones'):
    print(row['brand'])
    print(row['version'])


conn.close() # And close connection. 

