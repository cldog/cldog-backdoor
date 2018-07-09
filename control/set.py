#!coding=utf8


#读取文件数据显示设置信息
def set():
    f = open('./sql.db', 'r')
    tmp=f.read()
    f.close()

    if tmp=='':
        host=''
        user=''
        sqlpass=''
        database=''
    else:
        host=tmp.split('\n')[0]
        user=tmp.split('\n')[1]
        sqlpass=tmp.split('\n')[2]
        database=tmp.split('\n')[3]

    f=open('./net.db','r')
    tmp=f.read()
    f.close()

    print 'http代理:',tmp
    print 'host:',host
    print 'user:',user
    print 'pass',sqlpass
    print 'database:',database





