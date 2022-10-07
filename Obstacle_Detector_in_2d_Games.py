import pygame
pygame.init()
screen=pygame.display.set_mode((800,600))
font=pygame.font.SysFont("myfont",40)
player_width=100
player_height=100
obstacle_width=200
obstacle_height=200
player_x1=100
player_y1=600
player_x2=player_x1+player_width
player_y2=player_y1
player_x3=player_x1+player_width
player_y3=player_y1+player_height
player_x4=player_x1
player_y4=player_y1+player_height
obstacle_x1=300
obstacle_y1=300
obstacle_x2=obstacle_x1+obstacle_width
obstacle_y2=obstacle_y1
obstacle_x3=obstacle_x1+obstacle_width
obstacle_y3=obstacle_y1+obstacle_height
obstacle_x4=obstacle_x1
obstacle_y4=obstacle_y1+obstacle_height
player_xchange=0
player_ychange=0
speed=3 #player's speed
coll_message="touched..!!"
hor_right_coll_chk,hor_left_coll_chk=False,False
ver_top_coll_chk,ver_bottom_coll_chk=False,False
clock=pygame.time.Clock()
def player():
	pygame.draw.rect(screen,(128,0,128),(player_x1,player_y1,player_width,player_height))
def obstacle():
	pygame.draw.rect(screen,(255,0,0),(obstacle_x1,obstacle_y1,obstacle_width,obstacle_height))
def player_coordinates():
	text4=font.render('('+str(player_x4)+','+str(player_y4)+')',False,(0,0,0))
	text3=font.render('('+str(player_x3)+','+str(player_y3)+')',False,(0,0,0))
	text2=font.render('('+str(player_x2)+','+str(player_y2)+')',False,(0,0,0))
	text1=font.render('('+str(player_x1)+','+str(player_y1)+')',False,(0,0,0))
	obs_txt=font.render("OBSTACLE",False,(60,50,60))
	controls_info1=font.render("use w,a,s,d keys to contol the player",False,(60,50,60))
	controls_info2=font.render("use space key to stop the player",False,(60,50,60))
	screen.blit(text4,(player_x4-100,player_y4))
	screen.blit(text3,(player_x3,player_y3))
	screen.blit(text2,(player_x2,player_y2))
	screen.blit(text1,(player_x1-100,player_y1))
	screen.blit(obs_txt,(obstacle_x1, obstacle_y1+10))
	screen.blit(controls_info1,(150,0))
	screen.blit(controls_info2,(150,30))
def player_corners():
	global player_x2,player_y2,player_x3,player_y3,player_x4,player_y4
	player_x2=player_x1+player_width
	player_y2=player_y1
	player_x3=player_x1+player_width
	player_y3=player_y1+player_height
	player_x4=player_x1
	player_y4=player_y1+player_height
#function which check for collisions---
def collision():
	collision_gap=5
#right collision-------------
	if player_x2<obstacle_x1+collision_gap:
		if player_y1 in range(obstacle_y1, obstacle_y4) or player_y4 in range(obstacle_y1, obstacle_y4):
			if player_x2>obstacle_x1:
				return "horizontal right"
#left collision--------------
	if player_x1>obstacle_x2-collision_gap:
		if player_y1 in range(obstacle_y1, obstacle_y4) or player_y4 in range(obstacle_y1, obstacle_y4):
			if player_x1<obstacle_x2:
				return "horizontal left"
#top collision---------------
	if player_y4<obstacle_y1+collision_gap:
		if player_x1 in range(obstacle_x1, obstacle_x2) or player_x2 in range(obstacle_x1, obstacle_x2):
			if player_y4>obstacle_y1:
				return "vertical top"
#bottom collision-------------
	if player_y1>obstacle_y4-collision_gap:
		if player_x1 in range(obstacle_x4, obstacle_x3) or player_x2 in range(obstacle_x4, obstacle_x3):
			if player_y1<obstacle_y4:
				return "vertical bottom"
#main game loop-----------------	
root=True
while root:
	screen.fill((115,215,255))
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			root=False
		if event.type==pygame.KEYDOWN:
			
			if event.key==pygame.K_a:
				player_ychange=0
				hor_right_coll_chk=False
				ver_bottom_coll_chk=False
				ver_top_coll_chk=False
				if hor_left_coll_chk==False:
					player_xchange=-speed
					
			if event.key==pygame.K_d:
				player_ychange=0
				hor_left_coll_chk=False
				ver_bottom_coll_chk=False
				ver_top_coll_chk=False
				if hor_right_coll_chk==False:
					player_xchange=speed
					
			if event.key==pygame.K_w:
				player_xchange=0
				hor_right_coll_chk=False
				hor_left_coll_chk=False
				ver_top_coll_chk=False
				if ver_bottom_coll_chk==False:
					player_ychange=-speed
					
			if event.key==pygame.K_s:
				player_xchange=0
				hor_left_coll_chk=False
				hor_right_coll_chk=False
				ver_bottom_coll_chk=False
				if ver_top_coll_chk==False:
					player_ychange=speed
					
			if event.key==pygame.K_SPACE:
				player_xchange=0
				player_ychange=0
				
	player_x1+=player_xchange
	player_y1+=player_ychange
	if player_x1<0:
		player_x1=0
	if player_x1>625:
		player_x1=625
	player()
	obstacle()
	player_corners()
	coll=collision()
	
	if coll=="horizontal right":
		coll_txt=font.render(coll_message,False,(60,50,60))
		screen.blit(coll_txt,(obstacle_x1+20,obstacle_y1+100))
		player_x1=obstacle_x1-player_width
		hor_right_coll_chk=True
		
	if coll=="horizontal left":
		coll_txt=font.render(coll_message,False,(60,50,60))
		screen.blit(coll_txt,(obstacle_x1+20,obstacle_y1+100))
		player_x1=obstacle_x2
		hor_left_coll_chk=True
	
	if coll=="vertical top":
		coll_txt=font.render(coll_message,False,(60,50,60))
		screen.blit(coll_txt,(obstacle_x1+20,obstacle_y1+100))
		player_y1=obstacle_y1-player_height
		ver_top_coll_chk=True
		
	if coll=="vertical bottom":
		coll_txt=font.render(coll_message,False,(60,50,60))
		screen.blit(coll_txt,(obstacle_x1+20,obstacle_y1+100))
		player_y1=obstacle_y4
		ver_bottom_coll_chk=True
	
	player_coordinates()
	clock.tick(60)
	pygame.display.flip()
pygame.quit()