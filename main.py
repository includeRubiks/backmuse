import pygame, os

pygame.init()
screen = pygame.display.set_mode((720,720))
clock = pygame.time.Clock()

playbutton = pygame.image.load('icons/playbutton.png')
pausebutton = pygame.image.load('icons/pausebutton.png')
playing = False
songfiles = os.listdir('mp3s')
selection = 0
sanserif = pygame.font.SysFont('Sans Serif',27)
pygame.display.set_caption('Gyatify')
pygame.mixer.music.set_endevent(pygame.USEREVENT+0)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			x,y = pygame.mouse.get_pos()
			for i in range(len(songfiles)):
				if x >= 20 and x <= 640 and y >= i*20+20 and y <= i*20+40:
					selection = i
			if x >= 660 and x <= 710 and y >= 20 and y <= 70:
				if playing == False:
					playing = True
					pygame.mixer.music.stop()
					pygame.mixer.music.load(f'mp3s/{songfiles[selection]}')
					pygame.mixer.music.play()
				elif playing == True:
					playing = False
					pygame.mixer.music.stop()
		if event.type == pygame.USEREVENT+0:
			if playing != False:
				if (selection + 1) > (len(songfiles)-1):
					selection = 0
				else:
					selection += 1
				pygame.mixer.music.load(f'mp3s/{songfiles[selection]}')
				pygame.mixer.music.play()
	
	screen.fill('black')
	
	pygame.draw.rect(screen,(200,200,255),pygame.Rect(0,selection*20+20,640,20))
	
	for i,j in enumerate(songfiles):
		screen.blit(sanserif.render(j.replace('.mp3',''),False,'white'),(20,i*20+20))
		
	if playing == False:	
		screen.blit(playbutton,(660,20))
	else:
		screen.blit(pausebutton,(660,20))
	
	pygame.draw.line(screen,'white',(640,0),(640,720))
	
	pygame.display.flip()
	
	clock.tick(60)
	
	
