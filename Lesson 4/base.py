import sqlite3 as sq
con = sq.connect(r'Lesson 4\stud.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS class(
    st_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name TEXT,
    age INTEGER,
    avarage_score REAL);''')
name = 'Ira'
age = 23
av = 4.5
# cur.execute('''INSERT INTO  class(name,age,avarage_score)
#     VALUES(?,?,?);''',(name,age,av,))
# con.commit()
# sel = cur.execute('''SELECT * FROM class WHERE name = 'Ira'; ''')
# for i in sel:
#     print(i, type(i))

import time
# start = time.time()
# for i in range(50000000):
#     cur.execute('''INSERT INTO  class(name,age,avarage_score)
#     VALUES(?,?,?);''',(name,age,float(i),))
# con.commit()
# print(time.time()-start)
start = time.time()
sel = cur.execute('''SELECT * FROM class WHERE avarage_score = 46849605.0; ''')
for i in sel:
    print(i, type(i))
print(time.time()-start)

