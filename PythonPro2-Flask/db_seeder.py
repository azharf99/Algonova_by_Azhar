import sqlite3

# conn = sqlite3.connect("artistc.db")
conn = sqlite3.connect("PythonPro2-Flask/quiz.db")
cursor = conn.cursor()
# cursor.execute('''PRAGMA foreign_keys=on''')

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

# cursor.execute("""
#     DROP TABLE IF EXISTS quiz_content 
# """)

list_question = [
        ('How many months in a year have 28 days?', 'All', 'One', 'None','Two'),
        ('What will the green cliff look like if it falls into the Red Sea?', 'Wet', 'Red', 'Will not change', 'Purple'),
        ('Which hand is better to stir tea with?', 'With a spoon', 'Right', 'Left', 'Any'),
        ('What has no length, depth, width, or height, but can be measured?', 'Time', 'Stupidity', 'The sea','Air'),
        ('When is it possible to draw out water with a net?', 'When the water is frozen', 'When there are no fish', 'When the goldfish swim away', 'When the net breaks'),
        ('What is bigger than an elephant and weighs nothing?', 'Shadow of elephant','A balloon','A parachute', 'A cloud')
    ]


list_quiz_name = [
    ('Orang pintar dan rajin',),
    ('Aku ingin mengetahui semuanya',),
    ('Kekuatan pengetahuan',),
    ]

list_quiz_content = [
    (1,1),
    (2,2),
    (3,3),
    (1,4),
    (2,5),
    (3,6),
    ]

cursor.execute('''PRAGMA foreign_keys=on''')
cursor.executemany('''INSERT INTO question 
                 (pertanyaan, jawaban, wrong1, wrong2, wrong3) 
                  VALUES (?,?,?,?,?)''', list_question)

cursor.executemany('''INSERT INTO quiz (name) VALUES (?)''', list_quiz_name)

query = "INSERT INTO quiz_content (quiz_id, question_id) VALUES (?,?)"
cursor.executemany(query, list_quiz_content)

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