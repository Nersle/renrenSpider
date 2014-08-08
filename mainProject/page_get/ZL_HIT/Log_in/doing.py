import urllib
import urllib2
import cookielib

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
  
  
if __name__=="__main__":
 userR=raw_input("username:")
 pswdR=raw_input("Password:")
 userR='XXXXXXXXXX@163.com'
 pswdR='XXXXXXX'
 renRenLogIn(userR,pswdR)
 raw_input("---Game Over----")
  
