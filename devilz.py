import sys
import os
import time
import platform


print("""\033[1;32;40m
		  _____  ________      _______ _      ______
		 |  __ \|  ____\ \    / /_   _| |    |___  /
		 | |  | | |__   \ \  / /  | | | |       / / 
		 | |  | |  __|   \ \/ /   | | | |      / /  
		 | |__| | |____   \  /   _| |_| |____ / /__ 
		 |_____/|______|   \/   |_____|______/_____|
		                                            
		********************************************* 
		# Linux local privilege escalation helper   #
		#         Have a good CTF's :)              #
		#                                           #
		#                                           #
		*********************************************
\n""")
print("\033[0;0m")

time.sleep(3)
system = sys.version_info.major
if system == 3:
	print ("Please run the script for Python 2 version")
user = raw_input(""" 
		  1 ---> Print output in shell(**Recomended!**)
		  2 ---> Save at .txt

		  Please select number:  """)

if user == "1":	
	print("""\033[1;32;40m
		     -----------------------------
	     	     [+] Which services runned?\n	
		     -----------------------------
						""")
	print("\033[0;0m")
	services = os.system("cat /etc/services")
	print("------------------------------------------------------------------------\n")
	print("""\033[1;32;40m
		     -----------------------------
	     	     [+] Which services are running by root?\n	
		     -----------------------------
						""")
	print("\033[0;0m")
	root_serv = os.system("ps aux | grep root")
	print("------------------------------------------------------------------------\n")
	print("""\033[1;32;40m
		     ---------------------------------------
	     	     [+] Release and Kernel version\n	
		     ---------------------------------------
						""")
	print("\033[0;0m")
	uname = os.system("uname -a")
	print("------------------------------------------------------------------------\n")
	print("""\033[1;32;40m
		     ----------------------------------
	     	     [+] CRON Jobs(daily,weekly,mothly)\n	
		     ----------------------------------
						""")
	print("\033[0;0m")
	print("\033[1;32;40m 			DAILY CRON JOBS\n")
	print("\033[0;0m")
	cronjobs= os.system("ls /etc/cron.daily")
	print("\033[1;32;40m 			WEEKLY CRON JOBS\n")
	print("\033[0;0m")
	cronjobs2= os.system("ls /etc/cron.weekly")
	print("\033[1;32;40m 			MONTHLY CRON JOBS\n")
	print("\033[0;0m")
	cronjobs= os.system("ls /etc/cron.monthly")
	print("------------------------------------------------------------------------\n")
	print("""\033[1;32;40m
		     ----------------------------------
	     	     [+] ALL USERS\n	
		     ----------------------------------
						""")
	print("\033[0;0m")
	etc = os.system("cat /etc/passwd")
	print("------------------------------------------------------------------------\n")
	print("""\033[1;32;40m
		     ----------------------------------
	     	     [+] password.* file in \n	
		     ----------------------------------
						""")
	print("\033[0;0m")
	filename= os.system("grep 'password' */*")
	print("""\033[1;32;40m
		     ---------------------------------------------------
	     	     [+] We can sudo without supplying a password!\n	
		     ---------------------------------------------------
						""")
	print("\033[0;0m")
	sudol= os.system("sudo -l")

	print("""\033[1;32;40m
		     -----------------------------------------
	     	     [+] Installed programming languages\n	
		     -----------------------------------------
						""")
	print("\033[0;0m")
	lang = os.system("which gcc && which perl && which python 	&& which php && which gcc && which cc && which go && which 	g++ && which node && which c && which ruby")
	print("""\033[1;32;40m
		     ----------------------------------
	     	     [+] Check kernel version exploit's\n	
		     ----------------------------------
						""")
	print("\033[0;0m")

	
	platinfo= platform.release()
	platrelease= platinfo[0:6]

	exp = ["4.4.0","4.10.0","4.4.0","4.8.0","3.8.9","3.2.0","3.16.39","2.6.7","2.6.37","2.6.36","2.6.34","2.6.29","2.6.28","2.6.22","2.6.19","2.6.11","4.13.9","4.6.3","4.6.2","4.4.1","4.3.3","4.14.0","3.7.10","3.13.2","3.14.5","3.13.1","3.13.0","4.4.0","4.10.0","4.4.0","4.8.0","3.8.9","3.2.0","3.16.39","2.6.9","2.6.32","2.6.39","2.6.30","2.6.27","2.6.24","2.6.23","2.6.18","2.6.18","2.6.13","2.6.10","2.4.29","2.4.23","2.4.25","2.4.18","2.0.37","2.2.18"]
	if platrelease in exp:
		print(platrelease +"\n \033[1;31;40m 			[-] Kernel version is vulnerable!")
		print("\033[0;0m")

	else:
		print(" \033[1;31;40m  		  Maybe kernel version is not vulnerable")
		print("\033[0;0m")





elif user == "2":
	privesc1 = os.system("cat /etc/services > Services.txt")
	privesc2 = os.system("uname -mrs > Kernel.txt")
	privesc3 = os.system("ps aux | grep root > ServicesRunRoot.txt")
	privesc4 = os.system("ls /etc/cron.daily && ls /etc/cron.weekly && ls /etc/cron.monthly > CronJobs.txt")
	privesc5 = os.system("cat /etc/passwd > Users.txt")
	privesc6 = os.system("which gcc && which perl && which python && which php && which gcc && which cc && which go && which g++ && which node && which c && which ruby > InsLanguages.txt")
else:
	print("ERROR!")

	
