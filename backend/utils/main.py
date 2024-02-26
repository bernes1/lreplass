import pysopg2 

conn = pysopg2.connect("dbname=test user=admini")
cur =  conn.cursor()
cur.execute("SELECT * FROM ???")

records = cur.fetchall()