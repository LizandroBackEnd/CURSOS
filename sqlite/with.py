import sqlite3 
 
with sqlite3.connect("sqlite/app.db") as conn: 
    cursor = conn.cursor() 
    cursor.execute( 
        """ 
        CREATE TABLE if not exists users 
        (id INTEGER PRIMARY KEY, name VARCHAR(50));
        """
    ) 

 
#Con with, no es necesario llamar a commit() ni close() ya que se hace automáticamente.