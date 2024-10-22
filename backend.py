import sqlite3

class Database: #libros.db
    
    def __init__(self, db): #db=libros.db
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS libro (id INTEGER PRIMARY KEY, titulo text, autor text, year integer, isbn integer)")
        self.conn.commit()
        
        
    def insert(self,titulo,autor,year,isbn): 
        self.cur.execute("INSERT INTO libro VALUES (NULL,?,?,?,?)",(titulo,autor,year,isbn))
        self.conn.commit()
        
        
    def view(self): 
        self.cur.execute("SELECT * FROM libro")
        rows=self.cur.fetchall()
        return rows

    def search(self, titulo="",autor="",year="",isbn=""):
        self.cur.execute("SELECT * FROM libro WHERE titulo=? OR autor=? OR year=? OR isbn=?",(titulo,autor,year,isbn))
        rows=self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM libro WHERE id=?",(id,))
        self.conn.commit()
        
        

    def update(self,id,titulo,autor,year,isbn):
        self.cur.execute("UPDATE libro SET titulo=?, autor=?, year=?, isbn=? WHERE id=?",(titulo,autor,year,isbn,id))
        self.conn.commit()
        
    def __del__(self): #destructor the object
        self.conn.close()   #close the connection
        
    


