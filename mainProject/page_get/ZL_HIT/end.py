import urllib
import urllib2
import cookielib

#�ܽ᣺
#!!!!!!DoingGet������Ҫ���ԣ�ԭ�����ڲ���ֱ�ӻ�ȡ״̬ҳ�����ݣ������ǵ�½֮����ȥ������ϢҲ������ҳ����
#������
#��ĿĿǰ�������⣺Ŀǰ������ȥ״̬ҳ�����ݣ����Һܶ�ҳ��ġ���һҳ�������޷�ģ�⡣��������
#������ȡ��־��״̬���������Ŀǰ��չ���ã���Ȼ����html��ǩ�Ĳ��ֻ�ûд���������ʵ������Ӧ�ò��鷳��
#���ݿ�������δ��ʼ�����ݵ���Ӧ����ʲôһ�ַ�ʽд�벢����Ƽ��ű�
#�����������������ע����Ĳ������ƣ�ȷ�����ŷ��ʲ��ԣ������������
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



#��½������������cookie
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
  
#��ȡ��ҳ���������ݣ�����������״̬����־��Ϣ

  rcont=rfile.read()
  copener.close()
  print"successful LOg in to page!"
  return rcont
 
#����pagenameҳ���״̬��������õĸ�ʽΪ������---״̬ 
def analysis_doing(pagename):
   pagehdl=open(pagename,'r')
   pgList=pagehdl.read()
   pagehdl.close()

   #��ȡ����
   regstr=re.compile(r'(?<=<h3>).+?(?=</h3)',re.I|re.S|re.U)

   #��ȡ����
   rName=re.compile(r'(?<=\">).+?(?=</a)',re.I|re.S|re.U)

   #��ȡ״̬����
   rStatue=re.compile(r'(?<=/a>..).+?(?=<a)',re.I|re.S|re.U)
   reglist=regstr.findall(pgList)
   
   #���浽�ļ���Ϊ����doing.txt�����ļ���
   #�洢��ʽ�� "״̬������"----��״̬���ݡ�
   ztfile=open('Doing.txt','w')
   
   for h3 in reglist:     
    y=rName.findall(h3)
    x=re.split(':',h3)
    xx=y[0]+"-----"+x[2]
    xx+=os.linesep
    ztfile.write(xx)
   ztfile.close() 
   
   
#�˺���������ȡ����ҳ���еľ�����־��Ϣ��������־���ߡ���־���⡢�Լ���־��������
def analysis_log(pagename):
   pagehdl=open(pagename,'r')
   pgList=pagehdl.read()
   pagehdl.close()
 


   #��ȡ����
   rTitle=re.compile(r'(?<=title\".value=\").+?(?=\".type)',re.I|re.S|re.U)

   #��ȡ����
   rName=re.compile(r'(?<=\d{9}\"><span>).+?(?=</span)',re.I|re.S|re.U)

   #��ȡ��־����
   rStatue=re.compile(r'(?<=text-article\">).+?(?=</div)',re.I|re.S|re.U)
    
   r_name=rName.findall(pgList)
   r_statue=rStatue.findall(pgList)
   r_title=rTitle.findall(pgList)
   
   #����־��Ϣ�浽��log.txt���ļ��У�
   #�洢��ʽΪ������  XX
   #            ����  YY
   #            ���� �ƣƣƣƣƣƣƣƣƣƣƣƣƣƣƣƣ�
   ztfile=open('log.txt','w')
    
   print"+++++++++++++++++++++++++++++����+++++++++++++++++++++++++++++++++++\n\n"
   print   r_name
   print"+++++++++++++++++++++++++++++����+++++++++++++++++++++++++++++++++++\n\n"
   print  r_title
   print"+++++++++++++++++++++++++++++����+++++++++++++++++++++++++++++++++++\n\n"
   print  r_statue

   xx=" "

   xx= os.linesep+"����    "+r_name[0]+os.linesep
   xx+=os.linesep+"����    "+r_title[0] +os.linesep
   xx+=os.linesep+"����   "+r_statue[0] +os.linesep 
   
   ztfile.write(xx)
   ztfile.close()   



   
  
if __name__=="__main__":
 userR=raw_input("username:")
 pswdR=raw_input("Password:")
 renRenLogIn(userR,pswdR)
  