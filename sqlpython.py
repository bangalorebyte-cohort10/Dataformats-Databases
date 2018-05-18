import sqlite3

con = sqlite3.connect('test.db')

cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS students (id NUMBER, name VARCHAR(30));''')
print("Created DB and Table Student")

for i in range(3):
	f = int(input("Enter the value: "))
	k = input("Enter the name: ")
	cur.execute('''INSERT INTO students VALUES (?, ?)''', [f, k])
	# cur.execute('''INSERT INTO students VALUES ({}, '{}')'''.format(f, k))
print("Record has been inserted!!")

r = cur.execute('''SELECT * FROM students''')
row = r.fetchall()
print(row)

h = int(input("Enter id:"))
i = input("Enter name: ")
cur.execute('''UPDATE students SET name=? WHERE id=?''', [i, h])
print("Record has been updated!!")

# cur.execute('''DELETE FROM students WHERE id=5''')
# print("Record has been deleted!")

con.commit()

con.close()