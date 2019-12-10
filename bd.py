import mysql.connector
dbConnect = {
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

for datos in resultado:
    print(datos)