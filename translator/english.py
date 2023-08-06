with open("english/articles.txt") as f:
	articles = f.readlines()

def fr(text):
	tokens = []
	for word in text:
		if word in articles:
			pass