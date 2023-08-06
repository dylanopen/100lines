def load_flashcards(flashcard_file):
	cards = []
	with open(flashcard_file) as f: cont = f.read().splitlines()
	for card in cont: cards.append( card.split(",") )
	return cards
def flip_flashcard(initial_side):
	return 0 if initial_side == 1 else 1
import editor, os, sys, pygame as p
def load():
	global screen, flashcards, large_font
	p.init()
	screen = p.display.set_mode( (600, 450) )
	p.display.set_caption("Flashcard App")
	flashcards = load_flashcards(f"fc/{sys.argv[1]}.fc")
	large_font = p.font.SysFont("Arial", 24)
running = True
current_flashcard = 0
flashcard_side = 0
load()
while running:
	screen.fill( (32, 34, 36) )
	for event in p.event.get():
		if event.type == p.QUIT: running = False
		if event.type == p.KEYDOWN:
			if p.key.get_pressed()[p.K_RIGHT]:
				if current_flashcard + 1 < len(flashcards): current_flashcard += 1
				else: current_flashcard = 0
			if p.key.get_pressed()[p.K_LEFT]:
				if current_flashcard > 0: current_flashcard -= 1
				else: current_flashcard = len(flashcards) - 1
			if p.key.get_pressed()[p.K_EQUALS]:
				p.quit()
				editor.Editor(f"fc/{sys.argv[1]}.fc")
				load()
			if p.key.get_pressed()[p.K_SPACE]: flashcard_side = flip_flashcard(flashcard_side)
		if event.type == p.MOUSEBUTTONDOWN: flashcard_side = flip_flashcard(flashcard_side)
	card_label = large_font.render(flashcards[current_flashcard][flashcard_side], 1, p.Color( (255, 255, 255) ))
	card = card_label.get_rect(center=(600 // 2, 450 // 2))
	screen.blit(card_label, card)
	p.display.flip()
	p.display.update()
p.quit()