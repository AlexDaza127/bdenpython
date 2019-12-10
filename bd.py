#importamos el conector de mysql
import mysql.connector

#creacion de la conexion con la base de datos en mysql
dbConnector = {
    'host': 'localhost',
    'user': 'root',
    'password':'',
    'database':'pruebapython'
}


conexion = mysql.connector.connect(**dbConnect)
cursor = conexion.cursor()
sql = "select * from usuarios"
cursor.execute(sql)
resultado = cursor.fetchall()