import sqlite3 
 
conn = sqlite3.connect("sqlite/app.db") 
cursor = conn.cursor() 
cursor.execute( 
    """ 
    CREATE TABLE if not exists users 
    (id INTEGER PRIMARY KEY, name VARCHAR(50));
    """
) 
conn.commit() 
conn.close() 
 
#Nota: Luego de realizar una consulta, siempre hay que comprometer con cambios con commit()