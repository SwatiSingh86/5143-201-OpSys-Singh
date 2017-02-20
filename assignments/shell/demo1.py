import threading
import os
import sys
import shutil


def cp(cmd):
	#Built-in function to copy souce to destination. Imported "shutil" library to use its built-in functions. 
	shutil.copyfile(cmd[1],cmd[2])
	#print('Copy Successful.')
	return
def pwd(cmd):
	print(os.getcwd())
	return
def cat(file):
	f = open(file[1],'r')
	print(f.read())
	f.close()
def who(cmd):
	print(os.popen('who').read())
	return
	  
if __name__ == '__main__':
	cmd = input('% ')
	# cmd=stdin()
	cmd=cmd.split(' ')
	if(cmd[0]=="cp"):
		t = threading.Thread(target=cp,args=(cmd,))
		t.start()
		t.join()
	elif (cmd[0]=="pwd"):
		t = threading.Thread(target=pwd,args=(cmd,))
		t.start()
		t.join()
	elif (cmd[0]=="cat"):
		t = threading.Thread(target=cat,args=(cmd,))
		t.start()
		t.join()
	elif (cmd[0]=="who"):
		t = threading.Thread(target=who,args=(cmd,))
		t.start()
		t.join()
	
	else :
		print("invalid command")
