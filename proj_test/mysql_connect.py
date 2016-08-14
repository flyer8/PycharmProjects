# Connect to MySQL and select data
# Should be installed "mysql-connector-python-2.1.3-py3.4-winx64.msi"
import mysql.connector
conn = mysql.connector.connect(host='localhost',database='shtat',user='root',password='Ss140179')
cursor = conn.cursor()
query = ("SELECT cod, zvan, fam, im FROM personal WHERE zvan = 'прапорщик' ORDER BY cod")
cursor.execute(query)
for i in cursor:
    print (i)