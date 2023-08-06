import os

def run(v, folder="."):
	if os.path.exists(v["cd"] + "/" + folder):
		v["cd"] = os.path.abspath(v["cd"] + "/" + folder)
		return v["cd"]
	return f"\u001b[31;1m Error: the directory '{folder}' does not exist\u001b[0m"