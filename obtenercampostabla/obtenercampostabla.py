import fdb

con = fdb.connect(dsn='localhost:C://dev//amg//fdb//database/EMPRESA.FDB', user='sysdba', password='a2210')

cur = con.cursor()
 
SELECT = "SELECT ID, COD, FIRST_NAME, LAST_NAME FROM CUSTOMERS"

cur.execute(SELECT)

for row in cur.itermap():
    print(str(row['ID']).ljust(5),row['COD'], row['FIRST_NAME'])


