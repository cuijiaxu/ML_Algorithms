from __future__ import print_function

import cx_Oracle
import sampleenv
import urllib
import urllib.request
import json

# 's340':'s40E0724B-8C86-11E8-B444-060400EF5315',
#'s370':'s40E07236-8C86-11E8-B444-060400EF5315',
#'s377':'s40E07233-8C86-11E8-B444-060400EF5315',

urldict = {'s59':'s40E07201-8C86-11E8-B444-060400EF5315',
's51':'s40E07202-8C86-11E8-B444-060400EF5315',
's379':'s40E07231-8C86-11E8-B444-060400EF5315',
's220':'s40E07259-8C86-11E8-B444-060400EF5315',
's213':'s40E0725C-8C86-11E8-B444-060400EF5315',
's65':'s40E07293-8C86-11E8-B444-060400EF5315',
's396':'s40E072C0-8C86-11E8-B444-060400EF5315',
's371':'s40E072C1-8C86-11E8-B444-060400EF5315',
's363':'s40E072C2-8C86-11E8-B444-060400EF5315',
's218':'s40E072C3-8C86-11E8-B444-060400EF5315',
's217':'s40E072C4-8C86-11E8-B444-060400EF5315',
's209':'s40E072C5-8C86-11E8-B444-060400EF5315',
's202':'s40E072C7-8C86-11E8-B444-060400EF5315',
's201':'s40E072C8-8C86-11E8-B444-060400EF5315',
's376':'s40E07234-8C86-11E8-B444-060400EF5315',
's92':'s40E072CD-8C86-11E8-B444-060400EF5315',
's225':'s40E07257-8C86-11E8-B444-060400EF5315',
's223':'s40E07258-8C86-11E8-B444-060400EF5315',
's212':'s40E0725D-8C86-11E8-B444-060400EF5315',
's66':'s40E072DD-8C86-11E8-B444-060400EF5315',
's63':'s40E072DF-8C86-11E8-B444-060400EF5315',
's378':'s40E07232-8C86-11E8-B444-060400EF5315',
's52':'s40E072E7-8C86-11E8-B444-060400EF5315',
's68':'s40E07292-8C86-11E8-B444-060400EF5315',
's211':'s40E0725E-8C86-11E8-B444-060400EF5315',
's郊5':'s40E07219-8C86-11E8-B444-060400EF5315',
's213区线':'s40E07210-8C86-11E8-B444-060400EF5315',
's80':'s40E0728D-8C86-11E8-B444-060400EF5315',
's81':'s40E0728C-8C86-11E8-B444-060400EF5315',
's94':'s40E0728B-8C86-11E8-B444-060400EF5315',
's98':'s40E0728A-8C86-11E8-B444-060400EF5315',
's213支':'s40E0720F-8C86-11E8-B444-060400EF5315',
's215':'s40E0720E-8C86-11E8-B444-060400EF5315',
's220支':'s40E0720D-8C86-11E8-B444-060400EF5315',
's359':'s40E0720C-8C86-11E8-B444-060400EF5315',
's388':'s40E0720B-8C86-11E8-B444-060400EF5315',
's83区间':'s40E0720A-8C86-11E8-B444-060400EF5315',
's68区间':'s40E07207-8C86-11E8-B444-060400EF5315',
's57区间':'s40E07204-8C86-11E8-B444-060400EF5315',
's58':'s40E072E2-8C86-11E8-B444-060400EF5315',
's361':'s40E0723D-8C86-11E8-B444-060400EF5315',
's364':'s40E0723C-8C86-11E8-B444-060400EF5315',
's365':'s40E0723B-8C86-11E8-B444-060400EF5315',
's366':'s40E0723A-8C86-11E8-B444-060400EF5315',
's353':'s40E07243-8C86-11E8-B444-060400EF5315',
's356':'s40E07241-8C86-11E8-B444-060400EF5315',
's55':'s40E072E5-8C86-11E8-B444-060400EF5315',
's90':'s40E072CF-8C86-11E8-B444-060400EF5315',
's89':'s40E072D0-8C86-11E8-B444-060400EF5315',
's206':'s40E072C6-8C86-11E8-B444-060400EF5315',
's83':'s40E072D5-8C86-11E8-B444-060400EF5315',
's82':'s40E072D6-8C86-11E8-B444-060400EF5315',
's71':'s40E072DA-8C86-11E8-B444-060400EF5315',
's64':'s40E072DE-8C86-11E8-B444-060400EF5315',
's61':'s40E072E0-8C86-11E8-B444-060400EF5315',
's85':'s40E072D3-8C86-11E8-B444-060400EF5315',
's84':'s40E072D4-8C86-11E8-B444-060400EF5315',
's203':'s40E07261-8C86-11E8-B444-060400EF5315',
's73':'s40E07290-8C86-11E8-B444-060400EF5315',
's381':'s40E0722F-8C86-11E8-B444-060400EF5315',
's387':'s40E0722A-8C86-11E8-B444-060400EF5315',
's390':'s40E07228-8C86-11E8-B444-060400EF5315',
's399':'s40E07226-8C86-11E8-B444-060400EF5315',
's97':'s40E072C9-8C86-11E8-B444-060400EF5315',
's382':'s40E0722E-8C86-11E8-B444-060400EF5315',
's346-2':'s40E0721C-8C86-11E8-B444-060400EF5315',
's67':'s40E07200-8C86-11E8-B444-060400EF5315',
's333':'s40E07252-8C86-11E8-B444-060400EF5315',
's226':'s40E07256-8C86-11E8-B444-060400EF5315',
's368':'s40E07238-8C86-11E8-B444-060400EF5315',
's369':'s40E07237-8C86-11E8-B444-060400EF5315',
's383':'s40E0722D-8C86-11E8-B444-060400EF5315',
's386':'s40E0722B-8C86-11E8-B444-060400EF5315',
's56':'s40E072E4-8C86-11E8-B444-060400EF5315',
's53':'s40E072E6-8C86-11E8-B444-060400EF5315',
's93':'s40E072CC-8C86-11E8-B444-060400EF5315',
's87':'s40E072D1-8C86-11E8-B444-060400EF5315',
's79':'s40E072D7-8C86-11E8-B444-060400EF5315',
's75':'s40E072D9-8C86-11E8-B444-060400EF5315',
's70':'s40E072DB-8C86-11E8-B444-060400EF5315',
's57':'s40E072E3-8C86-11E8-B444-060400EF5315',
's399区间':'s7ED955720F7F383CE0530816010A6EBE',
's216':'s40E0725B-8C86-11E8-B444-060400EF5315',
's219':'s40E0725A-8C86-11E8-B444-060400EF5315',
'x59':'x40E07201-8C86-11E8-B444-060400EF5315',
'x51':'x40E07202-8C86-11E8-B444-060400EF5315',
'x379':'x40E07231-8C86-11E8-B444-060400EF5315',
'x220':'x40E07259-8C86-11E8-B444-060400EF5315',
'x213':'x40E0725C-8C86-11E8-B444-060400EF5315',
'x65':'x40E07293-8C86-11E8-B444-060400EF5315',
'x396':'x40E072C0-8C86-11E8-B444-060400EF5315',
'x371':'x40E072C1-8C86-11E8-B444-060400EF5315',
'x363':'x40E072C2-8C86-11E8-B444-060400EF5315',
'x218':'x40E072C3-8C86-11E8-B444-060400EF5315',
'x217':'x40E072C4-8C86-11E8-B444-060400EF5315',
'x209':'x40E072C5-8C86-11E8-B444-060400EF5315',
'x202':'x40E072C7-8C86-11E8-B444-060400EF5315',
'x201':'x40E072C8-8C86-11E8-B444-060400EF5315',
'x376':'x40E07234-8C86-11E8-B444-060400EF5315',
'x92':'x40E072CD-8C86-11E8-B444-060400EF5315',
'x340':'x40E0724B-8C86-11E8-B444-060400EF5315',
'x225':'x40E07257-8C86-11E8-B444-060400EF5315',
'x223':'x40E07258-8C86-11E8-B444-060400EF5315',
'x212':'x40E0725D-8C86-11E8-B444-060400EF5315',
'x370':'x40E07236-8C86-11E8-B444-060400EF5315',
'x377':'x40E07233-8C86-11E8-B444-060400EF5315',
'x66':'x40E072DD-8C86-11E8-B444-060400EF5315',
'x63':'x40E072DF-8C86-11E8-B444-060400EF5315',
'x378':'x40E07232-8C86-11E8-B444-060400EF5315',
'x52':'x40E072E7-8C86-11E8-B444-060400EF5315',
'x68':'x40E07292-8C86-11E8-B444-060400EF5315',
'x211':'x40E0725E-8C86-11E8-B444-060400EF5315',
'x郊5':'x40E07219-8C86-11E8-B444-060400EF5315',
'x213区线':'x40E07210-8C86-11E8-B444-060400EF5315',
'x80':'x40E0728D-8C86-11E8-B444-060400EF5315',
'x81':'x40E0728C-8C86-11E8-B444-060400EF5315',
'x94':'x40E0728B-8C86-11E8-B444-060400EF5315',
'x98':'x40E0728A-8C86-11E8-B444-060400EF5315',
'x213支':'x40E0720F-8C86-11E8-B444-060400EF5315',
'x215':'x40E0720E-8C86-11E8-B444-060400EF5315',
'x220支':'x40E0720D-8C86-11E8-B444-060400EF5315',
'x359':'x40E0720C-8C86-11E8-B444-060400EF5315',
'x388':'x40E0720B-8C86-11E8-B444-060400EF5315',
'x83区间':'x40E0720A-8C86-11E8-B444-060400EF5315',
'x68区间':'x40E07207-8C86-11E8-B444-060400EF5315',
'x57区间':'x40E07204-8C86-11E8-B444-060400EF5315',
'x58':'x40E072E2-8C86-11E8-B444-060400EF5315',
'x361':'x40E0723D-8C86-11E8-B444-060400EF5315',
'x364':'x40E0723C-8C86-11E8-B444-060400EF5315',
'x365':'x40E0723B-8C86-11E8-B444-060400EF5315',
'x366':'x40E0723A-8C86-11E8-B444-060400EF5315',
'x353':'x40E07243-8C86-11E8-B444-060400EF5315',
'x356':'x40E07241-8C86-11E8-B444-060400EF5315',
'x55':'x40E072E5-8C86-11E8-B444-060400EF5315',
'x90':'x40E072CF-8C86-11E8-B444-060400EF5315',
'x89':'x40E072D0-8C86-11E8-B444-060400EF5315',
'x206':'x40E072C6-8C86-11E8-B444-060400EF5315',
'x83':'x40E072D5-8C86-11E8-B444-060400EF5315',
'x82':'x40E072D6-8C86-11E8-B444-060400EF5315',
'x71':'x40E072DA-8C86-11E8-B444-060400EF5315',
'x64':'x40E072DE-8C86-11E8-B444-060400EF5315',
'x61':'x40E072E0-8C86-11E8-B444-060400EF5315',
'x85':'x40E072D3-8C86-11E8-B444-060400EF5315',
'x84':'x40E072D4-8C86-11E8-B444-060400EF5315',
'x203':'x40E07261-8C86-11E8-B444-060400EF5315',
'x73':'x40E07290-8C86-11E8-B444-060400EF5315',
'x381':'x40E0722F-8C86-11E8-B444-060400EF5315',
'x387':'x40E0722A-8C86-11E8-B444-060400EF5315',
'x390':'x40E07228-8C86-11E8-B444-060400EF5315',
'x399':'x40E07226-8C86-11E8-B444-060400EF5315',
'x97':'x40E072C9-8C86-11E8-B444-060400EF5315',
'x382':'x40E0722E-8C86-11E8-B444-060400EF5315',
'x346-2':'x40E0721C-8C86-11E8-B444-060400EF5315',
'x67':'x40E07200-8C86-11E8-B444-060400EF5315',
'x333':'x40E07252-8C86-11E8-B444-060400EF5315',
'x226':'x40E07256-8C86-11E8-B444-060400EF5315',
'x368':'x40E07238-8C86-11E8-B444-060400EF5315',
'x369':'x40E07237-8C86-11E8-B444-060400EF5315',
'x383':'x40E0722D-8C86-11E8-B444-060400EF5315',
'x386':'x40E0722B-8C86-11E8-B444-060400EF5315',
'x56':'x40E072E4-8C86-11E8-B444-060400EF5315',
'x53':'x40E072E6-8C86-11E8-B444-060400EF5315',
'x93':'x40E072CC-8C86-11E8-B444-060400EF5315',
'x87':'x40E072D1-8C86-11E8-B444-060400EF5315',
'x79':'x40E072D7-8C86-11E8-B444-060400EF5315',
'x75':'x40E072D9-8C86-11E8-B444-060400EF5315',
'x70':'x40E072DB-8C86-11E8-B444-060400EF5315',
'x57':'x40E072E3-8C86-11E8-B444-060400EF5315',
'x399区间':'x7ED955720F7F383CE0530816010A6EBE',
'x216':'x40E0725B-8C86-11E8-B444-060400EF5315',
'x219':'x40E0725A-8C86-11E8-B444-060400EF5315'
}

for key,value in urldict.items():
    print(key)
    url = 'http://localhost/jsons/' +value+'.json'
    try:
        requestinfo = urllib.request.urlopen(url,data=None,timeout=10)
    except:
        print("not find:"+key)
    data = requestinfo.read().decode()

    connection = cx_Oracle.connect(sampleenv.MAIN_CONNECT_STRING) 
    cursor = connection.cursor()
    cursor.execute("insert into JC_XCFA_LH t values(:name,:id,:routs)",name=key,id=key,routs=data)
    connection.commit()
