from __future__ import print_function

import cx_Oracle
import sampleenv
import urllib
import urllib.request
import json
import uuid

def insertrows(insertlist):
    print('start insert-----')
    

if __name__ == "__main__":
    insertlist = [('59-22', '59', 'e4:c4:83:81:da:35', 16, '2019-01-07 12:51:23', '和兴路', 16, '2019-01-07 12:51:23', '和兴路'), ('59-22', '59', 'e4:c4:83:81:da:35', 16, '2019-01-07 12:51:23', '和兴路', 20, '2019-01-07 12:55:25', '林业大学'), ('59-22', '59', 'e4:c4:83:81:da:35', 16, '2019-01-07 12:51:23', '和兴路', 21, '2019-01-07 12:59:15', '三大动力路')]
    connection = cx_Oracle.connect(sampleenv.INSERT_MAIN_STRING) 
    cursor = connection.cursor()
    cursor.executemany("insert into WIFIOD values(:1,:2,:3,:4,:5,:6,:7,:8,:9)",insertlist)
    connection.commit()
    cursor.close()
    connection.close()