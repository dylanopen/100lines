import tkinter as tk, tkinter.font as font
class Editor:
	def __init__(self, file):
		self.file = file
		self.window = tk.Tk()
		self.window.configure(bg="#222426")
		self.window.title(f"Add Flashcards")
		tk.Label(self.window, text="Front side of flashcard:", bg="#222426", fg="#a7a7a7").pack()
		self.front = tk.Text(self.window, fg="#ffffff", bg="#333639", width=30, height=3, font=font.Font(family="Arial", size=16, weight=font.BOLD))
		self.front.pack()
		tk.Label(self.window, text="Back side of flashcard:", bg="#222426", fg="#a7a7a7").pack()
		self.back = tk.Text(self.window, fg="#ffffff", bg="#333639", width=30, height=3, font=font.Font(family="Arial", size=16, weight=font.BOLD))
		self.back.pack()
		tk.Button(self.window, fg="#ffffff", bg="#6633bb", text="Add flashcard", width=30, command=self.new).pack()
		tk.Label(self.window, text="Flashcard CSV (paste spreadsheet data here):", bg="#222426", fg="#a7a7a7").pack()
		self.csv = tk.Text(self.window, fg="#ffffff", bg="#333639", width=40, height=7, font=font.Font(family="Arial", size=12))
		self.csv.pack()
		with open(file) as f:
			self.csv.insert("1.0", f.read())
		self.window.protocol("WM_DELETE_WINDOW", self.save)
		self.window.mainloop()
	def new(self):
		self.csv.insert("1.0", self.front.get("1.0", "end-1c") + "," + self.back.get("1.0", "end-1c") + "\n")
	def save(self):
		with open(self.file, "w") as f:
			f.write(self.csv.get(1.0, "end-1c"))
		self.window.destroy()