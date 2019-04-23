from __future__ import print_function

import cx_Oracle
import sampleenv
import urllib
import urllib.request
import json
import uuid

def insertrows(insertlist):
    #print('start insert-----')
    connection = cx_Oracle.connect(sampleenv.INSERT_MAIN_STRING) 
    cursor = connection.cursor()
    try:
        cursor.executemany("insert into WIFIOD values(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12)",insertlist)
        connection.commit()
    except cx_Oracle.DatabaseError as exc:
        print(exc.args.message)
    finally:
        cursor.close()
        connection.close()
    

def handledirbybus(busno,linename):
    print(busno)
    try:
        connection = cx_Oracle.connect(sampleenv.MAIN_CONNECT_STRING) 
        cursor = connection.cursor()
        cursor.arraysize = 1000
        cursor.execute("""select a.*,
        a.stopindex - LAG(a.stopindex, 1, a.stopindex) OVER(order by a.catchtime, a.macid) AS diff
            from 
            (select max(t.clzbh) as busno,
                    '59' as linename,
                    t.sbidh as macid,
                    t.zdxh as stopindex,
                    max(to_char(t.scrq,'yyyy-MM-dd HH:mi:ss')) as catchtime,
                    max(t.zdmc) as stopname
                from DD_JK_CLKLSCJL_20190106 t
            where t.xllpmc = :linename
                and t.clzbh = :busno
            group by t.sbidh, t.zdxh
            order by stopindex, macid) a""",[linename,busno])
        allrecords = cursor.fetchall()
        print("query close")
        dirguid = str(uuid.uuid1())
        for updirindex in range(len(allrecords)):
            if updirindex ==0:
                tup1 = (dirguid,)
                allrecords[updirindex]=allrecords[updirindex]+tup1
            else:
                if allrecords[updirindex][6] > 0:
                    tup1 = (dirguid,)
                    allrecords[updirindex]=allrecords[updirindex]+tup1
                else:
                    dirguid = str(uuid.uuid1())
                    tup1 = (dirguid,)
                    allrecords[updirindex]=allrecords[updirindex]+tup1
        print("add dir close--")
        #print(allrecords[1][2])
        insertlist = []
        for countindex in range(len(allrecords)):
            macid = allrecords[countindex][2]
            guid = str(uuid.uuid1())
            for index in range(countindex+1,len(allrecords)):
                if allrecords[index][2] == macid and allrecords[countindex][7] == allrecords[index][7]:
                    insertlist.append((allrecords[countindex][0],allrecords[countindex][1],macid,allrecords[countindex][3],allrecords[countindex][4],allrecords[countindex][5],allrecords[index][3],allrecords[index][4],allrecords[index][5],guid,allrecords[countindex][7],allrecords[index][7]))           
        print("loop close---")
        insertrows(insertlist)
        insertlist.clear()
        print("insert close ---")
    except cx_Oracle.DatabaseError as exc:
        print(exc.args.message)
    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    linename = '59'
    connection = cx_Oracle.connect(sampleenv.MAIN_CONNECT_STRING) 
    cursor = connection.cursor()
    cursor.arraysize = 50
    cursor.execute("select  t.clzbh from  DD_JK_CLKLSCJL_20190106 t where t.xllpmc = :linename group by t.clzbh",linename = linename)
    distinctbuses = cursor.fetchall()
    for result in distinctbuses:
        handledirbybus(result[0],linename)
    
    cursor.close()
    connection.close()