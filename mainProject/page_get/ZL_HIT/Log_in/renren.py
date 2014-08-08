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
  rcont=rfile.read()
  copener.close()
  print"successful Get to page!"
  return rcont
  
  
if __name__=="__main__":
 userR=raw_input("username:")
 pswdR=raw_input("Password:")
 renRenLogIn(userR,pswdR)
  
