import sqlite3 
 
with sqlite3.connect("sqlite/app.db") as conn: 
    cursor = conn.cursor() 
    cursor.execute( 
        "SELECT * FROM users" 
    ) 
    print(cursor.fetchone())