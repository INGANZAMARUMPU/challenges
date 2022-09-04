from dicts import SizedDict

def cached(size):
	memory = SizedDict(size)
	def decorator(fun_tocall):
		def wrapper(*args, **kwargs):
			fun_name = fun_tocall.__name__
			str_arg = "".join([str(x) for x in args])
			list_kwargs = sorted(kwargs.keys())
			str_kwarg = "".join(a + str(kwargs[a]) for a in list_kwargs)
			arg = fun_name + str_arg + str_kwarg
			print(arg)
			if arg in memory:
				return memory[arg]
			else:
				values = fun_tocall(*args)
				memory[arg] = values
				return values
		return wrapper
	return decorator