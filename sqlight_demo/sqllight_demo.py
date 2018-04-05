import sqlite3

conn = sqlite3.connect('demo.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE example(Language VARCHAR, Version REAL, Skill TEXT)")

#create_table()

def enter_data():
    c.execute("INSERT INTO example VALUES('Python', 2.7, 'Beginner')")
    c.execute("INSERT INTO example VALUES('Python', 3.3, 'Intermediate')")
    c.execute("INSERT INTO example VALUES('Python', 3.4, 'Advanced')")
    conn.commit()

#enter_data()

def enter_dynamic_data():
    lang = input("What language? ")
    ver = float(input("What version? "))
    skill = input("What skill? ")
    c.execute("INSERT INTO example (Language, Version, Skill) VALUES (?, ?, ?)", (lang, ver, skill))
    conn.commit()
#enter_dynamic_data()

def read_from_db():
    sql = "SELECT * FROM example"
    for row in c.execute(sql):
        print(row)
        print(row[0], row[1], row[2])

read_from_db()

def read_dynamically_from_db():
    what_skill = input("What skill? ")
    sql = "SELECT * FROM example WHERE Skill == ?"
    for row in c.execute(sql, [(what_skill)]):
        print(row)
        print(row[0], row[1], row[2])

read_dynamically_from_db()
read_dynamically_from_db()
read_dynamically_from_db()

conn.close()