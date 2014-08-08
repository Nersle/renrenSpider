import urllib
import urllib2
import cookielib

#总结：
#!!!!!!DoingGet函数需要调试，原因在于不能直接获取状态页的内容，就算是登陆之后，爬去所得信息也还是首页内容
#！！！
#项目目前存在问题：目前不能爬去状态页的内容，并且很多页面的“下一页”动作无法模拟。。。。。
#分析提取日志、状态方面的内容目前进展良好，虽然过滤html标签的部分还没写，但是这个实现起来应该不麻烦，
#数据库的设计尚未开始，数据到底应该以什么一种方式写入并且设计几张表？
#另外必须获得人人网，注册码的产生机制，确定最优访问策略，这个尚需解决！
#                         2011.5.28.Nersle

def DoingGet(username,pswd):
  jar=cookielib.LWPCookieJar()
  rcookie=urllib2.HTTPCookieProcessor(jar)
  copener=urllib2.build_opener(rcookie)
  urllib2.install_opener(copener)
  postdata = urllib.urlencode({
	'email':username, 
	'password': pswd,
	'origURL':'http://www.renren.com/Home.do',
	'domain':'renren.com'
  })
  reqst=urllib2.Request('http://www.renren.com/PLogin.do', postdata)
  rfile=copener.open(reqst)
  jar.save("cookieLib/renren.cookie")
  #rcont=rfile.read()
  
  print"successful Get to page!"
  
  rqt=urllib2.Request('http://blog.renren.com/blog/0/friendsNews?from=homeleft')
  fl=copener.open(rqt)
  xx=fl.read()
  
  
  ztfile=open('Doing.html','w')
  ztfile.write(xx)
  ztfile.close()
  copener.close()
  
  return xx



#登陆人人网，保存cookie
def renRenLogIn(username,pswd):
  jar=cookielib.LWPCookieJar()
  rcookie=urllib2.HTTPCookieProcessor(jar)
  copener=urllib2.build_opener(rcookie)
  urllib2.install_opener(copener)
  postdata = urllib.urlencode({
	'email':username, 
	'password': pswd,
	'origURL':'http://www.renren.com/Home.do',
	'domain':'renren.com'
  })
  reqst=urllib2.Request('http://www.renren.com/PLogin.do', postdata)
  rfile=copener.open(reqst)
  jar.save("cookieLib/renren.cookie")
  
#获取首页新鲜事内容，包括：最终状态、日志信息

  rcont=rfile.read()
  copener.close()
  print"successful LOg in to page!"
  return rcont
 
#分析pagename页面的状态，分析获得的格式为：姓名---状态 
def analysis_doing(pagename):
   pagehdl=open(pagename,'r')
   pgList=pagehdl.read()
   pagehdl.close()

   #提取段落
   regstr=re.compile(r'(?<=<h3>).+?(?=</h3)',re.I|re.S|re.U)

   #提取姓名
   rName=re.compile(r'(?<=\">).+?(?=</a)',re.I|re.S|re.U)

   #提取状态内容
   rStatue=re.compile(r'(?<=/a>..).+?(?=<a)',re.I|re.S|re.U)
   reglist=regstr.findall(pgList)
   
   #保存到文件名为：“doing.txt”的文件中
   #存储格式： "状态发起人"----“状态内容”
   ztfile=open('Doing.txt','w')
   
   for h3 in reglist:     
    y=rName.findall(h3)
    x=re.split(':',h3)
    xx=y[0]+"-----"+x[2]
    xx+=os.linesep
    ztfile.write(xx)
   ztfile.close() 
   
   
#此函数用于提取链接页面中的具体日志信息，包括日志作者、日志标题、以及日志具体内容
def analysis_log(pagename):
   pagehdl=open(pagename,'r')
   pgList=pagehdl.read()
   pagehdl.close()
 


   #提取标题
   rTitle=re.compile(r'(?<=title\".value=\").+?(?=\".type)',re.I|re.S|re.U)

   #提取作者
   rName=re.compile(r'(?<=\d{9}\"><span>).+?(?=</span)',re.I|re.S|re.U)

   #提取日志内容
   rStatue=re.compile(r'(?<=text-article\">).+?(?=</div)',re.I|re.S|re.U)
    
   r_name=rName.findall(pgList)
   r_statue=rStatue.findall(pgList)
   r_title=rTitle.findall(pgList)
   
   #将日志信息存到“log.txt”文件中，
   #存储格式为：作者  XX
   #            标题  YY
   #            内容 ＦＦＦＦＦＦＦＦＦＦＦＦＦＦＦＦＦ
   ztfile=open('log.txt','w')
    
   print"+++++++++++++++++++++++++++++作者+++++++++++++++++++++++++++++++++++\n\n"
   print   r_name
   print"+++++++++++++++++++++++++++++标题+++++++++++++++++++++++++++++++++++\n\n"
   print  r_title
   print"+++++++++++++++++++++++++++++内容+++++++++++++++++++++++++++++++++++\n\n"
   print  r_statue

   xx=" "

   xx= os.linesep+"作者    "+r_name[0]+os.linesep
   xx+=os.linesep+"标题    "+r_title[0] +os.linesep
   xx+=os.linesep+"内容   "+r_statue[0] +os.linesep 
   
   ztfile.write(xx)
   ztfile.close()   



   
  
if __name__=="__main__":
 userR=raw_input("username:")
 pswdR=raw_input("Password:")
 renRenLogIn(userR,pswdR)
  