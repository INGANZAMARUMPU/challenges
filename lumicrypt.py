import subprocess
import unsync

@unsync.unsync
def crypt(a):
	crypted = subprocess.check_output(["java", "-jar", "lumicrypt.jar", "1000"])
	print(crypted)

crypt(a)
