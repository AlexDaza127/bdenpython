#importamos el conector de mysql
import mysql.connector

#creación de la conexion con la base de datos en mysql
dbConnect = {
    'host': 'localhost',
    'user': 'root',
    'password':'',
    'database':'pruebapython'
}

#creación de la variable que establece la conexion
conexion = mysql.connector.connect(**dbConnect)
#creación del cursor que permite enviar comandos al servidor y recibir los registros
cursor = conexion.cursor()
#creacion de la variable que permite realizar la consulta
sql = "select * from usuarios"
#se ejecuta la consulta
cursor.execute(sql)
#creacion de la variable que recibe los registros de la consulta
resultado = cursor.fetchall()


#se crea un for para imprimir por linea cada fila de la consulta
for datos in resultado:
    print(datos)