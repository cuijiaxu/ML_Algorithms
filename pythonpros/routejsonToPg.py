from __future__ import print_function

import cx_Oracle
import sampleenv
import urllib
import urllib.request
import json
import uuid
import psycopg2
import requests

def requestgeojson(luid):
    print(luid)
    url = 'http://localhost:8022/json/jsonFile/' +luid.strip()+'.json'
    try:
        #requestinfo = urllib.request.urlopen(url,data=None,timeout=10)
        #rst = requestinfo.read()
        #rst_dict = json.loads(rst)
        requestinfo = requests.get(url)
        rst_dict = requestinfo.json()
        #print(rst_dict)
        return rst_dict['geometry']
    except:
        print("not find:"+luid)
    finally:
        return None
    

def insertgeom(rowid,luid):
    try:
        rgeojson = requestgeojson(luid)
        connection = psycopg2.connect(database="qgis_postgreSQL", user="postgres", password="admin", host="10.1.30.32", port="5432")
        cursor = connection.cursor()
        #print(rgeojson)
        if rgeojson != None:
            cursor.execute("update np_busline set geom = ST_GeomFromGeoJSON(%s) where id = %s;", (json.dumps(rgeojson),rowid,))
            connection.commit()       
    except psycopg2.DatabaseError as exc:
        print(exc.args.message)
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    connection = psycopg2.connect(database="qgis_postgreSQL", user="postgres", password="admin", host="10.1.30.32", port="5432")
    cursor = connection.cursor()
    cursor.arraysize = 50
    cursor.execute("select id,luid from np_busline where luid is not null and luid <> ''")
    allroutes = cursor.fetchall()
    for result in allroutes:
        insertgeom(result[0],result[1])
        #print(result[1])

    cursor.close()
    connection.close()