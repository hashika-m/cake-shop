#!C:\Python312\python.exe

import cgi
import mysql.connector

print("Content-Type:text/html\r\n")

print("<html>")
print("<body>")
print("<h1> Thank you. Your review has been recorded!!</h1>")

form=cgi.FieldStorage()
fname=form.getvalue("fname")
fmessage=form.getvalue("Message")

print("<h1>",fname,"</h1>")
print("<h1>",fmessage,"</h1>")

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="review"
)

mycursor=mydb.cursor()
sql="INSERT INTO user(Name,Message)VALUE(%s,%s)"
value=(fname,fmessage)

mycursor.execute(sql,value)
mydb.commit()

print("</body>")
print("</html>")