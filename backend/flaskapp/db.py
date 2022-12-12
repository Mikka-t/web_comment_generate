import pymysql.cursors
import markov

def createConnection():
    ret = pymysql.connect(host='database_container',
                          port=13306,
                          database='mydata',
                          user='Mikka',
                          password='apue928476',
                          cursorclass=pymysql.cursors.DictCursor)

    return ret

    
def insertURL(url):
    con = createConnection()

    cur = con.cursor()
    sql = "INSERT INTO URLs (url_str) VALUES (%s)"
    ret = cur.execute(sql, url)
    con.commit()

    con.close()
    return ret


def getMessages(url):
    con = createConnection()

    cur = con.cursor()

    markov

    messages = cur.fetchall()

    con.close()
    return messages
