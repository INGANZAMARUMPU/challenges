with open("db.txt") as file:
	list_line = file.readline().split("}, {")
	f_founds = open("founds.csv", "w")
	indexes = []
	fake_indexes = []
	founds = []
	fake_founds = []
	for i, line in enumerate(list_line):
		line = line.replace("{","").replace("},","").replace(", ", "+")
		somme = eval(line)
		if somme == 170:
			indexes.append(i)
			founds.append(line)
			print(f"{i} {line} = {eval(line)}")
		else:
			fake_indexes.append(i)
			fake_founds.append(line)

	print("\n".join([f"{str(x)};{y};{eval(y)}" for x,y in zip(indexes, founds)]), file=f_founds)
	print("\n", file=f_founds)
	print("\n".join([f"{str(x)};{y};{eval(y)}" for x,y in zip(fake_indexes, fake_founds)]), file=f_founds)
	f_founds.close()