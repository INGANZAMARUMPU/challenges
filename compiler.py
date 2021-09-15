import compileall, sys
from pathlib import Path

py_version = "".join(sys.version.split()[0].split(".")[:2])
CPYTHON_EXT = f".cpython-{py_version}"

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
	new_name = old_name.replace(CPYTHON_EXT, "")
	
	try:
		py = parent_dir / f"{new_name}.py"
		py.unlink()
		py = parent_dir / f"{new_name}.pyc"
		py.unlink()

	except FileNotFoundError as e:
		continue

	pyc.rename((parent_dir / f"{new_name}.pyc"))

input("C'est fait !!!")
