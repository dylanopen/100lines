import sys, os, importlib
v = {"cd": os.path.expanduser("~"), "exit": 255}
def run(code):
	c = code.split(" ")
	if os.path.exists(c[0] + ".py"):
		return importlib.import_module(c[0]).run(v, *c[1:])
		return f"\u001b[31;1m Error: the arguments '{', '.join(c[1:])}' are not valid for the module '{c[0]}'\u001b[0m"
	return f"\u001b[31;1m Error: '{c[0]}' is not a dscript extension, application or file\u001b[0m"
def shell():
	while True:
		line = input("\u001b[36;1m " + v["cd"] + "\u001b[30;1m$\u001b[0m ")
		print(run(line))
		if v["exit"] != 255:
			exit(v["exit"])
def interpreter(file):
	with open(file) as f:
		lines = f.read().splitlines()
	for line in lines:
		run(line)
if len(sys.argv) <= 1: shell()
else: interpreter(sys.argv[1])