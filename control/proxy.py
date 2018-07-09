#!coding=utf8


#将代理设置写入文件
def netSet():
    print '请配置proxy参数,暂时仅支持http代理'
    host = raw_input('host:')
    port = raw_input('port:')

    f = open('./net.db', 'w')
    if host=='':
        f.write('')
    else:
        f.write(host+':'+port)
    f.close()
    print '参数设置完成'

