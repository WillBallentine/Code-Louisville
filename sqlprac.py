import sqlite3
from os import path

#basic python database code

conn = sqlite3.connect("/Users/willballentine/Documents/datasort/sample.db")
c = conn.cursor()
x = 'jane@mail.com', 'Jane', 'Doe'
c.execute('Insert into users values (?,?,?)', x)
conn.commit()
conn.close()
print(c.rowcount)