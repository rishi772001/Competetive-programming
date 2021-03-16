'''
@Author: rishi
'''

from mysql.connector import connect

# get connection to db
db = connect(host="localhost", user="root", password="", port="33", database="rec")
# create cursor to execute sql
my_cursor = db.cursor()

# insert query
data = ("181001105", "Swathy", "B", "IT", "1234567890")
my_cursor.execute("insert into student (registerno, name, section, branch, phno) values (%s, %s, %s, %s, %s)", data)

# select query
my_cursor.execute("select * from student ORDER BY phno LIMIT 2")
for i in my_cursor:
    print(i)
