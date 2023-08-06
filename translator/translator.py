import english
langs = {"en", english}
il = input("Input language = ")
rl = input("Result language = ")
while True:
	inp = input(f"{il} = ")
	res = ""
	if il in langs:
		res = langs[il].fr(inp)
	else:
		continue
	if rl == "tokens":
		print(res)