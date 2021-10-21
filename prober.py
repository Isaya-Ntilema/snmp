#!/usr/bin/env python	
import sys,time,easysnmp
from easysnmp import Session
from_cmd = sys.argv
every_time = 1/float(from_cmd[2])
ip , port ,commu = from_cmd[1].split(':')

current = []
past =[]
all_oids = []
for i in range(4,len(from_cmd)):
	all_oids.append(from_cmd[i])
all_oids.insert(0,'1.3.6.1.2.1.1.3.0')
#Printing all_oids
def probing():
	global current,next
	if each!=0:
		print (int(t1)),"|",
	session = Session(hostname=ip,remote_port = port, community='public', version=2,timeout = 1,retries = 1)
	ans = session.get(all_oids)
	past  = []
	for select in range(1,len(ans)):
		if ans[select].value!= 'OBJECT-NOT-PRESENT' and ans[select].value!='INSTANCE-NOT-PRESENT':
			past.append(int(ans[select].value))
		        
			if each!= 0 and len(current)>0:
			
				num=  int(past[select-1])-int(current[select-1])
				den = round(t1-next,1)
				rate = int(num/den)
				if rate<0:
					if ans[select].snmp_type =='past':
						num = num+ 2**32
						print (int(num/den)),"|",
					elif ans[select].snmp_type =='COUNTER64':
						num = num+ 2**64
						print (int(num/den)),"|",
				else:

					print (int(rate)),"|",
	if each!=0:	
		print ("")
	current = past
	next = t1

if int(from_cmd[3])== -1:
	each = 0
	current=[]
	while True:
		
		t1 = (time.time())
		probing()
		second = time.time()
		each = each+1
		time.sleep(abs(every_time-second+t1))

		
else:
	current=[]
	for each in range(0,int(from_cmd[3])+1):
		t1 = (time.time())
		probing()
		second = time.time()
		time.sleep(abs(every_time-second+t1))
