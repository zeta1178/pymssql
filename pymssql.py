import pymssql

def handler(event, context):

   # rds settings
   db_host = "adventureworksdw2012-3.c8rv2s5ixph5.us-gov-west-1.rds.amazonaws.com"
   db_username = "iss_admin"
   db_password = "Aw#%4IssQ"
   db_name = "AdventureWorks2012"
   db_port = "1433"

   conn = pymssql.connect(server=db_host, port=db_port, user=db_username, password=db_password, database=db_name)
   cursor = conn.cursor()
   cursor.execute('SELECT [FirstName] FROM Person.Person')

   rows = []

   for row in cursor:
      print('row = %r' % (row,))
      rows.append(row)

   conn.close()

   return rows
