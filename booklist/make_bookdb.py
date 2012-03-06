"""
Import bookdb.py and create a 
"""
import sqlite3
import bookdb

database = sqlite3.connect('book.db') # Create a database file
cursor = database.cursor() # Create a cursor
     
# Insert books into the table
d = bookdb.database
for id in d.keys():
    t = (id, d[id]['title'], d[id]['isbn'], d[id]['publisher'], d[id]['author'])
    cursor.execute('INSERT INTO books_book VALUES %s' % str(t))
    
     
database.commit() # Save our changes
database.close() # Close the connection to the database
     
     
     
     
if __name__ == 'main':
    
    database = sqlite3.connect('book.db') # Open the database file
    cursor = database.cursor() # Create a cursor
     
    cursor.execute("SELECT * FROM books_book") # Select everyone in the table
    results = cursor.fetchall()
    for entry in results:
        print entry
     
    database.close()
