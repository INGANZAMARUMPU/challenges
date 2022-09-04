from sized_dict import SizedDict

def cached(size):
	memory = SizedDict(size)
	def decorator(fun_tocall):
		def wrapper(*args):
			arg = fun_tocall.__name__ + "".join([str(x) for x in args])
			if arg in memory:
				return memory[arg]
			else:
				values = fun_tocall(*args)
				memory[arg] = values
				return values
		return wrapper
	return decorator