from decorators import cached
from sized_dict import SizedDict

import time
import random

cache = SizedDict(10)

@cached(memory=cache)
def crypt(b):
	time.sleep(0.5)
	a = random.randrange(0, 11)
	return f"{b}-{a}"


start = time.time()
for a in range(10):
	b = random.randrange(0, 11)
	print(crypt(b), end=" ")
end = time.time()
print("\n", start - end)
