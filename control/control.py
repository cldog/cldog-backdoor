#!coding=utf8

import help
import proxy
import shell
import sql
import set
import sqlset

#整体控制

def control():
    func=raw_input('[cldog] ^_^ ')
    type(func)
    if func == ':proxy':
        proxy.netSet()
    if func == ':set':
        set.set()
    if func ==':help':
        help.help()
    if func == ':shell':
        shell.shell()
    if func == ':sql-set':
        sqlset.sqlSet()
    if func == ':sql':
        sql.sql()
    if func == ':exit':
        exit(0)
