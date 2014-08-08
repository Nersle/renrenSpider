from ZL_HIT.Information import Info
from ZL_HIT.Log_in.renren import renRenLogIn
from ZL_HIT.Analsys_page.Analysis_renRen import analysis_rren

#  Introduction to page
print"----Information----\n"
Info()



# Test for Log in the website

print"\n----Test Log In----\n"
userR=raw_input("username:")
pswdR=raw_input("Password:")
rrpage=renRenLogIn(userR,pswdR)



# Write the web page to 'html' file

print"\n----Test Save In----\n"
fl1=open("rRHome.html",'w+')
fl1.write(rrpage)
fl1.close()

# Get to any webSite


# Analysis the page 

print"\n----Test Analysis----\n"
filename=raw_input("---filename---:")
filename=rRHome.html
analysis_rren(filename)
analysis_rren
raw_input("=====END======")
