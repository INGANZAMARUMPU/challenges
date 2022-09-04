from decorators import cached

import time
import random

@cached(size=20)
def crypt(b):
	time.sleep(0.5)
	a = random.randrange(0, 11)
	return f"{b}-{a}"


start = time.time()
for a in range(100):
	b = random.randrange(0, 11)
	print(crypt(b), end=" ")
end = time.time()
print("\n", start - end)
