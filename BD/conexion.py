import mysql.connector
from mysql.connector import Error

class Conectar():
	def __init__(self):
		try:
			self.conexion = mysql.connector.connect(

				host = 'localhost',
				port = 3306,
				user = 'root',
				password = 'Mateo31357058',
				db = 'disqueria'

			)

		except mysql.connector.Error as descripcionError:	
			print("no se conecto", descripcionError)


	#lista de albumes por Añbum en orden alfabetico
		
	def ListarAlbumes(self):
		if self.conexion.is_connected():
			try:
				cursor = self.conexion.cursor()
				cursor.execute("SELECT * FROM album ORDER BY nombre ASC") #sentencia SQL
				resultados = cursor.fetchall() # guardamos en una variable lo traido en la sentencia sql
				self.conexion.close #cerramos la coneccion a la bd
				return resultados


			except Error as descripcionError:	#otra forma del error
			    print("Error al intentar la conexion: {0}".format(descripcionError))

#creamos el objeto

con = Conectar()

for album in con.ListarAlbumes():
	print(album) # asi traemos toda la lista

	print("codigo: ", album[1], "nombre album", album[2])

			