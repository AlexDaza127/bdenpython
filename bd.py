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
"""sql = "select * from usuarios"
#se ejecuta la consulta
cursor.execute(sql)
#creacion de la variable que recibe los registros de la consulta
resultado = cursor.fetchall()


#se crea un for para imprimir por linea cada fila de la consulta
for datos in resultado:
    print(datos)
#mostrar registros especificos de la bd por medio de cadenas de caracteres
for datos in resultado:
    print(str(datos[0]) + str(datos[1]))

sqlInsertar = "insert into usuarios(id,nombre,email,pass)values(%s,%s,%s,%s)"
cursor.execute(sqlInsertar,('11','hola','hola@mundo.com','123'))
conexion.commit()
#Creacion de las sentencias para cerrar la conexion (buenas practicas)
cursor.close()
conexion.close()"""

#sentencia que permiten imprimit un solo registro consultado
sql = "select * from usuarios where id = %s"
cursor.execute(sql,('1',))
resultados = cursor.fetchone()
print(resultados)
cursor.close()
conexion.close()