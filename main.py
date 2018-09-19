#ESP MICROPYTHON CUSTOM COMMANDS
import os
ls=os.listdir
cd=os.chdir
rm=os.remove
mkdir=os.mkdir
rmdir=os.rmdir

def del_all():
	for i in ls():
		rm(i)
