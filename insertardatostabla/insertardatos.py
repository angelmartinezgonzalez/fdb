import fdb

con = fdb.connect(dsn='localhost:C://dev//amg//fdb//database/EMPRESA.FDB', user='sysdba', password='a2210')

cur = con.cursor()
 
SELECT = "SELECT ID, COD, FIRST_NAME, LAST_NAME FROM CUSTOMERS"

cur.execute(SELECT)

for (ID, COD, FIRST_NAME, LAST_NAME ) in cur:
    print('Tabla Customers Fila %s %s %s %s' % (str(ID), COD, FIRST_NAME, LAST_NAME))



# --- Inserta registros ---
# Insertion:
#varias filas

data = [
    ('cod9', 'Albania','fds'),
    ('cod10', 'Algeria','ff'),
    ('cod11', 'Andorra','gggds')
]
cur.executemany("insert into CUSTOMERS (COD, FIRST_NAME, LAST_NAME) values (?,?,?)",data)
con.commit()

# una fila filas
cur.execute("insert into CUSTOMERS (FIRST_NAME,LAST_NAME) values (?,?)",("lalala","Afghanistan"))
con.commit()

# una fila filas

cur.execute("insert into CUSTOMERS (COD, FIRST_NAME,LAST_NAME) values (?,?,?)",("code","Afghanistan","dasdas"))
con.commit()



# Obtener:
cur.execute("select * from CUSTOMERS")
print('Datos de la tabla Customer')
print(cur.fetchall())

