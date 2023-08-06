def run(v, code=0):
	v["exit"] = code
	return f"Quitting with exit code {code}"