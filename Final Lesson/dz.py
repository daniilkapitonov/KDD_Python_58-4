# 1 - Создать БД бургер, поля: название, тип котлеты, кол-во котлет, соус, кол-во булок. 
# Добавить туда 20 случайных бургеров. (Сделать массив с случайными именами и рандомить туда значения). 
# Сделать запросы: найти кол-во бургеров с кол-вом котлет от 1 до 3, кол-во бургеров без соуса и список 
# бургеров с 1 случайным названием.
import sqlite3 as sq
from random import randint
conn = sq.connect(r"Final Lesson/burger.db")
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS menu(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name TEXT,
    kotleta TEXT,
    k_amount INTEGER,
    souse TEXT,
    bread_amount INTEGER
); ''')
name_l = ['Чизубургер','Гамбургер','Крастикраб','Бабушкина котлета','Чамбакет','СССР Бургер','Салями','Фишбургер']
souse_l = ['Кекчук','Кечонез','Сырный','Мазик','Вишневый','Без соуса']
kotleta_l = ['Куриная','Свинная','Говяжья','Без котлеты']
# for i in range(20):
#     cur.execute('''INSERT INTO menu(name, kotleta, k_amount, souse, bread_amount) VALUES(?,?,?,?,?)''',(name_l[randint(0,len(name_l)-1)],
#     kotleta_l[randint(0,len(kotleta_l)-1)], randint(1,4),souse_l[randint(0,len(souse_l)-1)], randint(1,4)))
# conn.commit()

l = list(cur.execute('''SELECT * FROM menu WHERE k_amount <=2 and k_amount >=1'''))
print('sel 1', "amount - ",len((l)))
for i in l:
    print(i)

l = list(cur.execute('''SELECT count(*) FROM menu WHERE souse == 'Без соуса' '''))
print('sel 2', "amount - ",len((l)))
for i in l:
    print(i)

l = list(cur.execute('''SELECT * FROM menu WHERE name==? ''',(name_l[randint(0,len(name_l)-1)],)))
print('sel 3', "amount - ",len((l)))
for i in l:
    print(i)