import subprocess

class SizedDict(dict):
	def __init__(self, size = 10):
		self.store = dict()
		self.KEYS = []
		self.MAX_LENGTH = size

	def __getitem__(self, key):
		return self.store[key]

	def __setitem__(self, key, value):
		if(key not in self.store):
			if(len(self.KEYS) == self.MAX_LENGTH):
				del self[self.KEYS[0]]
		self.store[key] = value
		self.KEYS.append(key)

	def __delitem__(self, key):
		del self.store[key]
		self.KEYS.remove(key)

	def __iter__(self):
		return iter(self.store)
	
	def __len__(self):
		return len(self.KEYS)

	def __str__(self):
		return str(self.store)

a = SizedDict(5)
a["un"] = "kimwe"
a["deux"] = "kimwe"
a["trois"] = "kimwe"
a["quatre"] = "kimwe"
a["cinq"] = "kimwe"
a["un"] = "kimwe"
print(a)

# def crypt(a):
# 	crypted = subprocess.check_output(["java", "-jar", "lumicrypt.jar", "1000"])
# 	return crypted.decode()

# import time

# start = time.time()
# for a in range(10):
# 	print(crypt(a), end=" ")
# end = time.time()
# print("\n", start - end)
