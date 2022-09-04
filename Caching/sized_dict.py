
class SizedDict():
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
	
	def __len__(self):
		return len(self.KEYS)

	def __str__(self):
		return str(self.store)

	def __contains__(self, key):
		return key in self.store

if __name__ == '__main__':
	a = SizedDict(5)
	a["un"] = "kimwe"
	a["deux"] = "bibiri"
	a["trois"] = "bitatu"
	a["quatre"] = "bine"
	a["cinq"] = "bitanu"
	a["un"] = "kimwe"
	print(a)
	a["six"] = "bitandatu"
	print(a)
