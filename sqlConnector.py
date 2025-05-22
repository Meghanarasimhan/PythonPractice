from loguru import logger
import mysql.connector

connection= mysql.connector.connect(host="127.0.0.1",user="root",password="",database="pythonPractice")
logger.info(connection)

cursor=connection.cursor()
#cursor.execute("select * from labours_table")
insertQuery="insert into labours_table(name,role,wages) values(%s,%s,%s)"
cursor.execute(insertQuery,("Rahul","labour",700))
connection.commit()


cursor.execute("SELECT * FROM labours_table")
result = cursor.fetchall()
logger.info(result)

cursor.close()
connection.close()
