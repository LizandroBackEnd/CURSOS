import sqlite3 
 
with sqlite3.connect("sqlite/app.db") as conn: 
    cursor = conn.cursor()  
    users = [ 
        (3, "Luis"),
        (2, "Juan"),
    ]
    cursor.executemany( 
        "INSERT INTO users VALUES(?, ?)", 
        users,
    ) 
