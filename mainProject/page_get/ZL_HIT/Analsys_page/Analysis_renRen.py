#-*- coding:utf-8 -*-
import re,os
def analysis_rren(pagename):
   pagehdl=open(pagename,'r')
   pgList=pagehdl.read()
   pagehdl.close()

   #提取段落
   regstr=re.compile(r'(?<=<h3>).+?(?=</h3)',re.I|re.S|re.U)


   #提取姓名
   rName=re.compile(r'(?<=\">).+?(?=</a)',re.I|re.S|re.U)


   #提取状态
   rStatue=re.compile(r'(?<=/a>..).+?(?=<a)',re.I|re.S|re.U)
   reglist=regstr.findall(pgList)
   
   #打开文件存储格式为：文件名：“状态详单.txt” -"状态发起人"----“状态内容”
   ztfile=open('11.html','w')
 
   for h3 in reglist:     
    print"+++++++++++++++++++++++++++++状态+++++++++++++++++++++++++++++++++++\n\n"
   # s=rStatue.findall(h3)
    y=rName.findall(h3)
    
    x=re.split(':',h3)
  
    xx=y[0]+"    "+x[2]
    xx+=os.linesep
    print xx
   # print s
    ztfile.write(xx)
   ztfile.close()  
 
if __name__=='__main__':
 filename=raw_input("---filename---:")
 filename="home.htm"
 analysis_rren(filename)
 raw_input("--------Analysis the HTML end------------")  
