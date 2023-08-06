def run(v, file, *cont):
		with open(v["cd"] + "/" + file, "w") as f:
			return f.write(" ".join(cont))
		return f"\u001b[31;1m Error: cannot write to file '{file}'\u001b[0m"
