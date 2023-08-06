def run(v, code=0):
	v["exit"] = code
	return f"Exiting with exit code {code}"