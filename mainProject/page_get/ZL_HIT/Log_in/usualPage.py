import urllib2
def usualLogIn(page_url):
  req=urllib2.Request(page_url)
  fpage=urllib2.urlopen(req)
  fcont=fpage.read()
  print fcont
  print"successful Get to page!"
  print page_url
if __name__=="__main__":
 usualUrl=raw_input("URL:")
 
 usualLogIn(usualUrl)
 raw_input("-----END----")