import sqlite3

conn = sqlite3.connect("PythonPro2-Web/artistc.db")
cursor = conn.cursor()
cursor.execute('SELECT * FROM artists')
data = cursor.fetchall()
#Question #1. How many artists are represented in the database? 
print("Total number of artists:", len(data))

#Question #2. How many women (Female) are in the database?
cursor.execute('SELECT * FROM artists WHERE Gender = "Female"  ')
data = cursor.fetchall()
print("Total number of female artists:", len(data))

#Question #3. How many people in the database were born before 1900?
cursor.execute('SELECT * FROM artists WHERE "Birth Year" < 1900 ')
data = cursor.fetchall()
print("Total number of artists where born before 1900:", len(data))

#Question #4*. What is the name of the oldest artist?
cursor.execute('SELECT * FROM artists WHERE "Birth Year" = (SELECT MIN("Birth Year") FROM artists) ')
# cursor.execute('SELECT MIN("Birth Year") FROM artists ')
data = cursor.fetchone()
# print("The oldest artist was born in:", data)
print("The oldest artist is:", data[1])  # Assuming the name is in the second column

