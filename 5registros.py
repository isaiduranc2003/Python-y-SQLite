import sqlite3
conexion = sqlite3.connect('Ejemplo.db')

c = conexion.cursor()
c.execute('''CREATE TABLE acciones (fecha text, operacion text, simbolo text, cantidad real, precio real)''')


c.execute("INSERT INTO acciones VALUES('24/nov/2016','compra','INV',100,15.43)")
c.execute("INSERT INTO acciones VALUES('28/dic/2018','compra','ESV',30,28.43)")
c.execute("INSERT INTO acciones VALUES('02/ene/2022','compra','INV',88,80.20)")
c.execute("INSERT INTO acciones VALUES('14/abr/2017','compra','LS',2,18.00)")
c.execute("INSERT INTO acciones VALUES('17/jun/2019','compra','QWS',7,24.00)")
conexion.commit()
conexion.close()

