def run(v, file):
	try:
		with open(v["cd"] + "/" + file) as f:
			return f.read()
	except Exception(e):
		return f"\u001b[31;1m Error: cannot read file '{file}'\u001b[0m"