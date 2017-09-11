import cx_Oracle

class connectToOracle():

	def __init__(self,query):
		self.query=query

	def connect(self):
		try:
			con =  cx_Oracle.connect('DRUGO73/lokomotiv1970@127.0.0.1/xe')
			#print(con.version)
			cur = con.cursor()
			cur.execute(self.query)
			#for result in cur:
				#print(result)
			return cur
			cur.close()
			con.close()
		except cx_Oracle.DatabaseError:
			print("No has puesto ninguna query")
