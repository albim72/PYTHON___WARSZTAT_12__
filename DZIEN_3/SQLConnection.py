import mysql.connector

db = mysql.connector.connect(user='root',password = 'abc123',host='127.0.0.1',port=3306,database='dbtestowa')

cursorObject = db.cursor()
"""
testTable = 
            CREATE TABLE test(
            ID INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
            NAME VARCHAR(25) NOT NULL,
            DESCR VARCHAR(400))


cursorObject.execute(testTable)

tableStudent = "create table student(name varchar(50), roll_no int);"
cursorObject.execute(tableStudent)

print("tabela została utworzona")


sql = "insert into student(name,roll_no) values(%s,%s)"
val = ("Henryk","99")

cursorObject.execute(sql,val)
db.commit()
print(cursorObject.rowcount, "dodano")


sql = "insert into student(name,roll_no) values(%s,%s)"
val = [("Anna","44"),
("Leon","33"),
("Ola","77"),
("Ala","23"),
("Piotr","67"),
("Tomasz","12")]

cursorObject.executemany(sql,val)
db.commit()
print(cursorObject.rowcount, "dodano")
"""

print("dane z tabeli student:")

query = "select name, roll_no from student"
cursorObject.execute(query)
myresult = cursorObject.fetchall()
for x in myresult:
    print(x)


print("filtrowane dane z tabeli student:")

query = "select name, roll_no from student where roll_no >= 44 order by name"
cursorObject.execute(query)
myresult = cursorObject.fetchall()
for x in myresult:
    print(x)


db.close()
