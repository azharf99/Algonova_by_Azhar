import sqlite3

# conn = sqlite3.connect("artistc.db")
conn = sqlite3.connect("PythonPro2-Web/artistc.db")
cursor = conn.cursor()

# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS quiz 
#     (id INTEGER PRIMARY KEY, name VARCHAR)
# """)
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS question (
#     id INTEGER PRIMARY KEY,
#     pertanyaan VARCHAR,
#     jawaban VARCHAR,
#     wrong1 VARCHAR,
#     wrong2 VARCHAR,
#     wrong3 VARCHAR)
# """)
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS quiz_content (
#     id INTEGER PRIMARY KEY,
#     quiz_id INTEGER,
#     question_id INTEGER,
#     FOREIGN KEY (quiz_id) REFERENCES quiz (id),
#     FOREIGN KEY (question_id) REFERENCES question (id))
# """)
# cursor.execute('''PRAGMA foreign_keys=on''')

# cursor.execute("""
#     DROP TABLE IF EXISTS quiz_content 
# """)

# list_question = [
#     ('Berapa bulan dalam setahun yang memiliki 28 hari?', 'All', 'One', 'None','Two'),
#     ('Berapakah bilangan Pi', 'Approximately 3.14', '3', '0', ' Exactly 3.14'),
#     ]

# list_quiz_name = [
#     ('Orang pintar dan rajin',),
#     ('Aku ingin mengetahui semuanya',),
#     ('Kekuatan pengetahuan',),
#     ]

# cursor.executemany('''INSERT INTO question 
#                  (pertanyaan, jawaban, wrong1, wrong2, wrong3) 
#                   VALUES (?,?,?,?,?)''', list_question)

# cursor.executemany('''INSERT INTO quiz (name) VALUES (?)''', list_quiz_name)

cursor.execute('''PRAGMA foreign_keys=on''')
query = "INSERT INTO quiz_content (quiz_id, question_id) VALUES (?,?)"
cursor.executemany(query, [(4,2)])

conn.commit()
conn.close()


# cursor.execute('SELECT * FROM artists')
# data = cursor.fetchall()
# #Question #1. How many artists are represented in the database? 
# print("Total number of artists:", len(data))

# #Question #2. How many women (Female) are in the database?
# cursor.execute('SELECT * FROM artists WHERE Gender = "Female"  ')
# data = cursor.fetchall()
# print("Total number of female artists:", len(data))

# #Question #3. How many people in the database were born before 1900?
# cursor.execute('SELECT * FROM artists WHERE "Birth Year" < 1900 ')
# data = cursor.fetchall()
# print("Total number of artists where born before 1900:", len(data))

# #Question #4*. What is the name of the oldest artist?
# cursor.execute('SELECT * FROM artists WHERE "Birth Year" = (SELECT MIN("Birth Year") FROM artists) ')
# # cursor.execute('SELECT MIN("Birth Year") FROM artists ')
# data = cursor.fetchone()
# # print("The oldest artist was born in:", data)
# print("The oldest artist is:", data[1])  # Assuming the name is in the second column

