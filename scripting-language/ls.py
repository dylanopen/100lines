import os

def run(v, folder="."):
	files = folders = ""
	for file in os.listdir(v["cd"] + "/" + folder):
		if os.path.isdir(v["cd"] + "/" + file):
			folders += f"\u001b[33;1m  {file}\u001b[0m   "
		else:
			files += f"\u001b[39;1m  {file}\u001b[0m   "
	return folders + files