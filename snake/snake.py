WIDTH, HEIGHT, SQUARE_SIZE = 16, 12, 32
import pygame as p
p.init()
p.display.set_mode((WIDTH * SQUARE_SIZE, HEIGHT * SQUARE_SIZE))
running = True
clock = p.time.Clock()
while running:
	clock.tick(30)
	for event in p.event.get():
		if event.type == p.QUIT:
			running = False
	p.display.flip()
	p.display.update()
p.quit()