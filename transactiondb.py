from pysqlite3 import dbapi2 as sqlite3

class TransactionDB:
    '''Authentication & business sample database '''
    def __init__(self):
        self.conn = sqlite3.connect("./kabang.db")
    
    def authenticate ( self, userid: str, passwd: str): 
        cur = self.conn.cursor()
        cur.execute("select userid, display_name, role from AUTH_INFO where userid=? and password=?", (userid, passwd))
        result = cur.fetchone()
        print(result)
        return result
    
    def list_requests(self, userid: str):
        cur = self.conn.cursor()
        cur.execute("SELECT request_time as '요청일자', registration_nm as '등기번호', status as '처리상태' FROM USER_REQUEST WHERE userid=?", (userid,)) 
        result = []
        result.append( ('요청일자', '등기번호', '처리상태'))
        result.extend( cur.fetchall())
        return result
        

    
if __name__  == '__main__':
    db = TransactionDB()
    print( db.authenticate( "charles", "1234!"))
    print( db.list_requests('charles'))