import compileall
from pathlib import Path

print("/!\\ CETTE CHOSE EST VRAIMENT SANS PITIER")
print("/!\\ IL SUPRIME TOUT LES FICHIER PY")

input("Si vous en foutez appuyer sur ENTER: ")

pys = Path.cwd().rglob("*.py")
for f in pys:
	print(f.name)

print("\n/!\\ Tout ces fichier seront remplacé par des .pycs")
input("\nencore une fois Si vous en foutez appuyer sur ENTER: ")

compileall.compile_dir(Path.cwd(), quiet=1, force=True)

pycs = Path.cwd().rglob("*.pyc")

for pyc in pycs:
	parent_dir = pyc.resolve().parent.parent

	old_name = pyc.stem
	new_name = old_name.replace(".cpython-39", "")
	
	try:
		py = parent_dir / f"{new_name}.py"
		py.unlink()
	except FileNotFoundError as e:
		continue

	pyc.rename((parent_dir / f"{new_name}.pyc"))

input("C'est fait !!!")