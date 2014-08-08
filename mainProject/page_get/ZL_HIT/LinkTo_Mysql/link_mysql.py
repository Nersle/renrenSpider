#-*- coding:utf-8 -*-
import re,os,MySQLdb
def link_to_mysql( ):
   conct=MySQLdb.connect(host="localhost",user="root",passwd="xxx", db='renren')
   cur=conct.cursor()
   pstr="INSERT INTO  renRenLog  VALUES ('2', \'妈妈必知的五件事\', \'宝宝\', \'抱宝宝\');"
   cur.execute(pstr)
   cur.close()
   conct.commit()
   print "---成功----"
   
    
   
 
 
if __name__=='__main__':
 filename=raw_input("---filename---:")
 filename="ee.htm"
 link_to_mysql()
 raw_input("--------Analysis the HTML end------------")  
