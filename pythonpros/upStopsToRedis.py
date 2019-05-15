from __future__ import print_function

import cx_Oracle
import redis
import sampleenv



if __name__ == "__main__":
    connection = cx_Oracle.connect(sampleenv.MAIN_CONNECT_STRING)
    cursor = connection.cursor()
    cursor.arraysize = 1000
    cursor.execute("select t.id,t.STOPNAME,t.LATITUDE,t.LONGITUDE from np_busstop t where t.flag = 1")
    stops = cursor.fetchall()

    redisPool = redis.ConnectionPool(host='10.1.100.105',password='123456') 
    r=redis.Redis(connection_pool=redisPool)
    p=r.pipeline()
    for stop in stops:
        p.set(stop[0],stop[1])
    
    p.execute()
    redisPool.disconnect()

    cursor.close()
    connection.close()