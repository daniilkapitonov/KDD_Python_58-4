import sqlite3 as sq
import time
con = sq.connect(r'Lesson 5\book.db')
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS publisher(
    pub_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name TEXT UNIQUE,
    director TEXT,
    address TEXT,
    mark REAL);''')

cur.execute('''CREATE TABLE IF NOT EXISTS book(
    book_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name TEXT UNIQUE,
    autor TEXT,
    pages INTEGER,
    avarage_score REAL,
    publusher_id INTEGER NOT NULL,
    FOREIGN KEY (publusher_id) REFERENCES publisher (pub_id)
    );''')

cur.execute('''INSERT OR IGNORE INTO publisher(name,director,address,mark) VALUES(?,?,?,?) ''',('Avrora','Vasua','Pupkina 12',4.3))
cur.execute('''INSERT OR IGNORE INTO publisher(name,director,address,mark) VALUES(?,?,?,?) ''',('Popcorn','Oil','Kino 14',3.3))
cur.execute('''INSERT OR IGNORE INTO publisher(name,director,address,mark) VALUES(?,?,?,?) ''',('Rosmen','Max','Mad 19',4.0))
con.commit()
cur.execute('''INSERT OR IGNORE INTO book(name,autor,pages,avarage_score,publusher_id) VALUES(?,?,?,?,?)''',("Duna",'Gerbert',400,9.0,1))
cur.execute('''INSERT OR IGNORE INTO book(name,autor,pages,avarage_score,publusher_id) VALUES(?,?,?,?,?)''',("It",'King',600,10.0,2))
cur.execute('''INSERT OR IGNORE INTO book(name,autor,pages,avarage_score,publusher_id) VALUES(?,?,?,?,?)''',("War and piece",'Tolstoy',1000,10.0,2))
cur.execute('''INSERT OR IGNORE INTO book(name,autor,pages,avarage_score,publusher_id) VALUES(?,?,?,?,?)''',("Infero",'Den Brown',350,7.0,3))
cur.execute('''INSERT OR IGNORE INTO book(name,autor,pages,avarage_score,publusher_id) VALUES(?,?,?,?,?)''',("Idiot",'Dostoevski',150,6.0,1))

con.commit()
# cur.execute('''UPDATE book set pages = 550 WHERE avarage_score=10.0 ''')
# con.commit()
# cur.execute('''DELETE FROM book WHERE avarage_score=9.0 ''')
# con.commit()
print('book')
sel = cur.execute('''SELECT * FROM book''')
for i in sel:
    print(i)
print('publisher')
sel = cur.execute('''SELECT * FROM publisher''')
for i in sel:
    print(i)

print('select')
sel = cur.execute('''SELECT book.name,publisher.name FROM book INNER JOIN publisher WHERE 
    publisher.pub_id = book.publusher_id and publisher.name = 'Avrora' ''')
for i in sel:
    print(i)

# name = 'Ira'
# age = 23
# av = 4.5
# cur.execute('''INSERT INTO  class(name,age,avarage_score)
#     VALUES(?,?,?);''',(name,age,av,))
# con.commit()
# sel = cur.execute('''SELECT * FROM class WHERE name = 'Ira'; ''')
# for i in sel:
#     print(i, type(i))

# start = time.time()
# for i in range(50000000):
#     cur.execute('''INSERT INTO  class(name,age,avarage_score)
#     VALUES(?,?,?);''',(name,age,float(i),))
# con.commit()
# print(time.time()-start)
# start = time.time()
# sel = cur.execute('''SELECT * FROM class WHERE avarage_score = 46849605.0; ''')
# for i in sel:
#     print(i, type(i))
# print(time.time()-start)
