import unicodedata

def cleaned(string):
	return unicodedata\
		.normalize('NFKD', string)\
		.encode('ASCII', 'ignore')\
		.decode().lower()