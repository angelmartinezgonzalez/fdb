import fdb

con = fdb.connect(dsn='localhost:C://dev//amg//fdb//database/EMPRESA.FDB', user='sysdba', password='a2210')

cur = con.cursor()

SELECT = "SELECT ID, COD, FIRST_NAME, LAST_NAME FROM CUSTOMERS"

cur.execute(SELECT)

for (ID, COD, FIRST_NAME, LAST_NAME ) in cur:
    print('Tabla Customers Fila %s %s %s %s' % (str(ID), COD, FIRST_NAME, LAST_NAME))

