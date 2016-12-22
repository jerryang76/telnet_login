#Password ***
import getpass
import sys
import telnetlib
# pause
import os

HOST = raw_input("Telnet server IP address: ")
#HOST = "10.10.1.223"

user = raw_input("Enter your remote account: ")
#user = "oc"

password = getpass.getpass()
#password = "128"

times = input("Retry times: ")
#times = 3
if times > 100:
	print "Number",times,"too big, max is 100."
	times = 100

print "Attacking :", HOST, "port 23"

while times > 0:
	i = 3
	tn = telnetlib.Telnet(HOST, 23, 10)	
	while i > 0:
		tn.read_until("r: ")		
		print "<< Command Line Interface V 3.6.3.0 >>"
		print ""
		tn.write(user + "\r\n")		
		print "User: "+ user
		if password:
			tn.read_until("d: ")
			tn.write(password + "\r\n")	
			print "Password: "+password
			print "****"
			print "Incorrect User/Password, Please Retry."
			print ""
		i -= 1
	print tn.read_all()
	tn.close()
	print "						Tries left: ",times-1
	times -= 1
os.system("pause")
