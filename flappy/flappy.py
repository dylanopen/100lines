def main():
	import os, random
	os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
	import pygame as p
	WIDTH = 1920
	HEIGHT = 1080
	SQUARE_SIZE = WIDTH // 32
	FPS = 60
	GRAVITY_CONST = 9.81 / FPS / 48 / 120 * SQUARE_SIZE
	JUMP_POWER = 60 / FPS / 12 / 120 * SQUARE_SIZE
	velocity = 0
	player_y = 9
	ofset = 0
	obstacles = []
	p.init()
	screen = p.display.set_mode((WIDTH, HEIGHT), p.FULLSCREEN)
	bg_img = p.transform.scale(p.image.load("background.png"), (WIDTH, HEIGHT))
	sprite_img = p.transform.scale(p.image.load("sprite.png"), (SQUARE_SIZE, SQUARE_SIZE))
	clock = p.time.Clock()
	def draw_obstacle(x, y):
		screen_x = int((x - ofset) * SQUARE_SIZE)
		screen_y = int(y * SQUARE_SIZE)
		p.draw.rect(screen, (96, 48, 0), p.Rect(screen_x, screen_y, SQUARE_SIZE, SQUARE_SIZE))
	def draw_player(y):
		screen_x = int(SQUARE_SIZE)
		screen_y = int(y * SQUARE_SIZE)
		screen.blit(sprite_img, (screen_x, screen_y))
	def generate_obstacle():
		ob = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
		is_top = True if random.randrange(0, 2) else False
		length = random.randrange(0, 10)
		for i in range(length):
			if is_top:
				ob[i] = True if length > i else False
			else:
				ob[17-i] = True if length > i else False
		return ob
	for i in range(32):
		if not i % 4 and i >= 8:
			obstacles.append(generate_obstacle())
		else:
			obstacles.append([False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False])
	screen.blit(bg_img, (0, 0))
	p.display.flip()
	p.display.update()
	font = p.font.SysFont(None, 32)
	running = True
	alive = True
	while running:
		clock.tick(FPS)
		velocity -= GRAVITY_CONST * (1 + (ofset / 1000))
		screen.blit(bg_img, (0, 0))
		if not alive:
			img = font.render(f"Score: {int(ofset // 4)}", True, (255, 255, 255))
			screen.blit(img, (20, 20))
			p.display.flip()
			p.display.update()
			for event in p.event.get():
				if event.type == p.QUIT:
					running = False
				if event.type == p.KEYDOWN and p.key.get_pressed()[p.K_SPACE]:
					main()
					running = False
			continue
		for event in p.event.get():
			if event.type == p.QUIT:
				alive = False
			if event.type == p.KEYDOWN and p.key.get_pressed()[p.K_SPACE]:
				velocity += JUMP_POWER * 1 + (ofset / 1000)
		player_y -= velocity
		if player_y > 17:
			alive = False
		if player_y < 0:
			velocity = - (velocity / 2)
			player_y = 0
		for col in range(len(obstacles)):
			for row in range(len(obstacles[0])):
				if obstacles[col][row]:
					draw_obstacle(col, row)
		if obstacles[int(ofset) + 2][int(player_y) + 1] or obstacles[int(ofset) + 1][int(player_y) + 1] or obstacles[int(ofset) + 2][int(player_y)] or obstacles[int(ofset) + 1][int(player_y)]:
			alive = False
		draw_player(player_y)
		img = font.render(f"Score: {int(ofset // 4)}", True, (255, 255, 255))
		screen.blit(img, (5, 5))
		if len(obstacles) < ofset + 32:
			for i in range(4):
				if not i % 4:
					obstacles.append(generate_obstacle())
				else:
					obstacles.append([False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False])
		p.display.flip()
		p.display.update()
		ofset += ofset / 1000 + 0.1
	p.quit()
if __name__ == "__main__":
	main()
