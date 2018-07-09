#!coding=utf8

#配置sql参数，写入文件
def sqlSet():
    print '请配置sql参数'
    host = raw_input('host:')
    user = raw_input('user:')
    sqlpass = raw_input('pass:')
    database= raw_input('database(若不指定，将显示全部已有数据库):')

    f = open('./sql.db', 'w')
    f.write(host+'\n')
    f.write(user+'\n')
    f.write(sqlpass+'\n')
    f.write(database)
    f.close()
    print '参数设置完成'
