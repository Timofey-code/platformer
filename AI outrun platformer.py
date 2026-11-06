import pygame
import sys
import math
import random

# texts
pygame.init()
WIDTH, HEIGHT = 800,480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI Robot Escape")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 35)
small_font = pygame.font.Font(None, 20)  



#generate platfroma
floor = pygame.Rect(0, 440, 800, 40)

# Level 1 Layout 
level_1_platforms = [
    floor,
    pygame.Rect(120, 320, 180, 20),  
    pygame.Rect(500, 320, 180, 20),  
    pygame.Rect(310, 210, 180, 20)   
]

# Level 2 Layout 
level_2_platforms = [
    floor,
    pygame.Rect(60, 350, 140, 20),
    pygame.Rect(600, 350, 140, 20),
    pygame.Rect(220, 250, 160, 20),
    pygame.Rect(420, 250, 160, 20),
    pygame.Rect(310, 150, 180, 20)
]

# Level 3 Layout (Highly vertical complex grid)
level_3_platforms = [
    floor,
    pygame.Rect(40, 360, 130, 20),
    pygame.Rect(630, 360, 130, 20),
    pygame.Rect(220, 290, 360, 20),
    pygame.Rect(80, 190, 150, 20),
    pygame.Rect(570, 190, 150, 20),
    pygame.Rect(280, 110, 240, 20)
]

#game progression
current_level = 1
platforms = level_1_platforms
# splayer
player = pygame.Rect(100, 380, 24, 40)




#robot setup
level_1_robots = [
    [pygame.Rect(720, 400, 24, 30), 1.3, (255, 50, 50), "Runner", 0, "ChatGPT"],   
    [pygame.Rect(650, 280, 24, 24), 1.8, (180, 50, 255), "Stalker", 0, "Gemini"],  
    [pygame.Rect(580, 390, 36, 45), 0.5, (255, 130, 0), "Shover", 0, "Grok"]       
]

level_2_robots = [
    [pygame.Rect(720, 400, 22, 28), 2.9, (50, 255, 255), "Runner", 0, "DeepSeek"],  
    [pygame.Rect(650, 200, 24, 24), 1.1, (255, 100, 100), "Stalker", 0, "Claude"],  
    [pygame.Rect(580, 395, 30, 40), 0.6, (50, 255, 50), "Shover", 0, "Qwen"]  
]

# Level 3 Boss 
level_3_robots = [
    [pygame.Rect(0, 190, 30, 10), 4.0, (0, 255, 220), "Sweeper", 1, "Copilot"], 
    [pygame.Rect(720, 400, 24, 24), 0.8, (255, 100, 0), "Boomer", 0, "Perplexity"], 
    [pygame.Rect(580, 380, 44, 58), 0.7, (255, 255, 255), "Shover", 0, "OpenAI"],
    [pygame.Rect(280, 80, 24, 24), 0.9, (255, 105, 180), "Boomer", 0, "Gemma"]
]

robots = level_1_robots

# collectible items setup
item_types = [
    ("RAM", (255, 255, 100)), 
    ("Mouse", (100, 255, 255)), 
    ("Keyboard", (255, 100, 255)), 
    ("CPU", (100, 255, 100)),
    ("GPU", (255, 150, 50)), 
    ("SSD", (150, 100, 255))
]

items = []
def spawn_items():
    global items_needed
    items.clear()
    platform_choices = platforms[1:] 
    for plat in platform_choices:
        name, color = random.choice(item_types)
        item_x = random.randint(plat.left + 10, plat.right - 30)
        item_y = plat.top - 20
        items.append([pygame.Rect(item_x, item_y, 20, 15), name, color])
    if current_level == 1:
        items_needed = 5
    elif current_level == 2:
        items_needed = 8
    elif current_level == 3:
        items_needed = 10
spawn_items()

# physics
player_vy = 0
player_grounded = False
score = 0
saved_score = 0  
items_collected = 0  
game_started = False
game_over = False  
game_won = False  # Track ultimate win state
walk_frame = 0.0

# Level-Aware Respawn Function
def respawn_player():
    global player, robots, platforms, items_collected, player_vy, player_grounded, game_over, score, saved_score
    
    items_collected = 0
    player.x = 100
    player.y = 300 if current_level >= 2 else 380
    player_vy = 0
    player_grounded = False
    game_over = False
    score = saved_score  
    
    robots[0][0].x = 720
    robots[0][0].y = 400
    
    robots[1][0].x = 650
    robots[1][0].y = 120 if current_level == 3 else (200 if current_level == 2 else 280)
    
    robots[2][0].x = 580
    robots[2][0].y = 380 if current_level == 3 else (395 if current_level == 2 else 390)
    
    if len(robots) > 3:
        robots[3][0].x = 280
        robots[3][0].y = 80
    spawn_items()

# collision
def handle_y_collision(rect, vy, platform_list):
    grounded = False
    for plat in platform_list:
        if rect.colliderect(plat):
            if vy > 0:  
                rect.bottom = plat.top
                vy = 0
                grounded = True
            elif vy < 0:  
                rect.top = plat.bottom
                vy = 0
    return vy, grounded

# game loop
while True:
    screen.fill((20, 22, 30))  
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if not game_started or game_won:
                    
                    current_level = 1
                    platforms = level_1_platforms
                    robots = level_1_robots
                    items_collected = 0
                    score = 0
                    player.x, player.y = 100, 380
                    respawn_player()
                    game_started = True
                    game_won = False
            if event.key == pygame.K_SPACE:
                if game_over:
                    respawn_player()

    if not game_started:
        # title text
        title_txt = font.render("AI ROBOT ESCAPE", True, (0, 255, 150))
        sub_txt = font.render("Collect all the items to build a PC and reach the exit!", True, (255, 255, 255))
        instr_txt = font.render("Press ENTER to Outrun the Machines", True, (255, 255, 255))
        screen.blit(title_txt, (WIDTH // 2 - title_txt.get_width() // 2, 180))
        screen.blit(sub_txt, (WIDTH // 2 - sub_txt.get_width() // 2, 240))
        screen.blit(instr_txt, (WIDTH // 2 - instr_txt.get_width() // 2, 300))

    elif game_won:
        # ULTIMATE VICTORY END SCREEN WINDOW OVERLAY
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((10, 35, 20, 230))  # Emerald digital tint matrix filter
        screen.blit(overlay, (0, 0))
        
        win_title = font.render("HUMANITY PRESERVED: ESCAPE SUCCESSFUL", True, (0, 255, 150))
        win_sub = font.render(f"Final Score: {score // 10} | Press ENTER to Replay", True, (255, 255, 255))
        
        screen.blit(win_title, (WIDTH // 2 - win_title.get_width() // 2, 180))
        screen.blit(win_sub, (WIDTH // 2 - win_sub.get_width() // 2, 240))

    elif game_over:
        # respawn overlay
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((10, 10, 15, 220))  
        screen.blit(overlay, (0, 0))
        
        lost_title = font.render("SYSTEM FAILURE: DATA CORRUPTED", True, (255, 50, 50))
        lost_sub = font.render(f"Items wiped! Press SPACEBAR to restart Level {current_level}", True, (255, 255, 255))
        
        screen.blit(lost_title, (WIDTH // 2 - lost_title.get_width() // 2, 180))
        screen.blit(lost_sub, (WIDTH // 2 - lost_sub.get_width() // 2, 240))

    else:

        score += 1
        keys = pygame.key.get_pressed()
        is_moving = False

        # Player move
        if keys[pygame.K_a]:
            player.x -= 5
            is_moving = True
        if keys[pygame.K_d]:
            player.x += 5
            is_moving = True

        # stop going out of screen
        if player.left < 0: player.left = 0
        if player.right > WIDTH: player.right = WIDTH

        # jump fir player
        if keys[pygame.K_w] and player_grounded:
            player_vy = -13.0
            player_grounded = False

        # gravity and up move
        player_vy += 0.65
        player.y += player_vy
        player_vy, player_grounded = handle_y_collision(player, player_vy, platforms)

        if is_moving and player_grounded:
            walk_frame += 0.25

        for plat in platforms:
            pygame.draw.rect(screen, (38, 44, 60), plat)
            pygame.draw.rect(screen, (0, 255, 150), plat, 1)  

        # draw items
        for item in items[:]:
            item_rect, item_name, item_color = item
            pygame.draw.rect(screen, item_color, item_rect)
            item_text = small_font.render(item_name, True, (255, 255, 255))
            screen.blit(item_text, (item_rect.centerx - item_text.get_width() // 2, item_rect.y - 14))
            
            # item check
            if player.colliderect(item_rect):
                items.remove(item)
                items_collected += 1
                
                # level transitions router logic
                if items_collected == items_needed:
                    if current_level == 1:
                        current_level = 2
                        saved_score = score
                        platforms = level_2_platforms
                        robots = level_2_robots
                        player.x, player.y = 100, 300
                        respawn_player()
                        break
                    elif current_level == 2:
                        current_level = 3
                        saved_score = score
                        platforms = level_3_platforms
                        robots = level_3_robots
                        player.x, player.y = 100, 300
                        respawn_player()
                        saved_score = score
                        break
                    elif current_level == 3:
                        saved_score = score
                        game_won = True
                        break
        
        # spawn items
        if not items and not game_won:
            spawn_items()

        # human
        pygame.draw.rect(screen, (0, 230, 255), (player.x + 4, player.y, 16, 12))
        pygame.draw.rect(screen, (0, 255, 150), (player.x, player.y + 12, player.width, 16))
        leg_offset = math.sin(walk_frame) * 6
        if is_moving and player_grounded:
            pygame.draw.line(screen, (0, 180, 255), (player.x + 6, player.y + 28), (player.x + 6 + leg_offset, player.bottom), 3)
            pygame.draw.line(screen, (0, 180, 255), (player.x + 18, player.y + 28), (player.x + 18 - leg_offset, player.bottom), 3)
        else:
            pygame.draw.rect(screen, (0, 180, 255), (player.x + 4, player.y + 28, 5, 12))
            pygame.draw.rect(screen, (0, 180, 255), (player.x + 15, player.y + 28, 5, 12))


        if 'boomer_directions' not in globals() and 'boomer_directions' not in locals():
            global boomer_directions
            boomer_directions = {}

        # ai Robot Logic
        for idx, robot_data in enumerate(robots):
            bot, speed, color, bot_type, bot_vy, bot_name = robot_data[:6]
            old_x = bot.x
            bot_grounded = False

            if bot_type == "Sweeper":
                bot.x += speed * bot_vy
                if bot.right > WIDTH or bot.left < 0:
                    bot_vy *= -1

            elif bot_type == "Boomer":
                bot_id = id(robot_data)
                if bot_id not in boomer_directions:
                    boomer_directions[bot_id] = 1
                roam_dir = boomer_directions[bot_id]
                
                #calculate distance to player
                dx = player.x - bot.x
                dy = player.y - bot.y
                distance = math.sqrt(dx**2 + dy**2)
                
                if distance < 160:
                    # Chase mode
                    current_speed = speed * 2.5
                    if bot.x < player.x:
                        bot.x += current_speed
                        boomer_directions[bot_id] = 1
                    else:
                        bot.x -= current_speed
                        boomer_directions[bot_id] = -1
                else:
                    # patrol
                    bot.x += speed * roam_dir
                    
                    # boundaries
                    if bot.right > WIDTH:
                        bot.right = WIDTH
                        boomer_directions[bot_id] = -1
                    elif bot.left < 0:
                        bot.left = 0
                        boomer_directions[bot_id] = 1
                        
                    if bot.x == old_x and bot_grounded:
                        boomer_directions[bot_id] *= -1

                
                bot_vy += 0.65
                bot.y += bot_vy
                bot_vy, bot_grounded = handle_y_collision(bot, bot_vy, platforms)

            elif bot_type == "Stalker":
                
                bot.x += speed if bot.x < player.x else -speed
                if bot.y < player.y - 40: bot.y += 2
                elif bot.y > player.y - 40: bot.y -= 2

            else:
                
                bot.x += speed if bot.x < player.x else -speed
                bot_vy += 0.65
                bot.y += bot_vy
                bot_vy, bot_grounded = handle_y_collision(bot, bot_vy, platforms)

            
            jump_threshold = 40 if current_level == 3 else 30
            if bot_grounded and (bot.x == old_x or player.y < bot.y - jump_threshold):
                bot_vy = -12.5 if current_level == 3 else -11.0
                bot_grounded = False

            
            robots[idx][4] = bot_vy






            
            jump_threshold = 40 if current_level == 3 else 30
            if bot_grounded and (bot.x == old_x or player.y < bot.y - jump_threshold):
                bot_vy = -12.5 if current_level == 3 else -11.0  # Bosses jump significantly higher!
                bot_grounded = False
            robot_data[4] = bot_vy

            # ai shape
            if bot_type == "Runner":
                pygame.draw.rect(screen, color, bot, 0, 4)
                pygame.draw.circle(screen, (255, 255, 255), (bot.centerx, bot.y + 8), 4)
            elif bot_type == "Sweeper":
                pygame.draw.rect(screen, color, bot, 0, 2)
                pygame.draw.rect(screen, (255, 255, 255), (bot.x + 5, bot.y + 3, bot.width - 10, 4))
            elif bot_type == "Boomer":
                distance = math.sqrt((bot.x - player.x)**2 + (bot.y - player.y)**2)
                pulse_color = (255, 255, 255) if (distance < 120 and pygame.time.get_ticks() % 200 < 100) else color
                pygame.draw.ellipse(screen, pulse_color, bot)
                pygame.draw.circle(screen, (0, 0, 0), bot.center, 6)
            elif bot_type == "Stalker":
                pygame.draw.ellipse(screen, color, bot)
                pygame.draw.rect(screen, (0, 255, 255), (bot.x + 4, bot.y + 8, 16, 4))
            elif bot_type == "Shover":
                if bot_name == "Qwen" or bot_name == "OpenAI":
                    pygame.draw.rect(screen, color, bot, 0, 8)
                    pygame.draw.rect(screen, (10, 40, 10), (bot.x + 4, bot.y + 4, bot.width - 8, 8))
                else:
                    pygame.draw.rect(screen, color, bot, 0, 2)
                    pygame.draw.rect(screen, (20, 20, 20), (bot.x + 3, bot.y + 6, bot.width - 6, 12))
            else:
                pygame.draw.rect(screen, color, bot, 0, 2)



            # robot name
            name_tag = small_font.render(bot_name, True, color)
            screen.blit(name_tag, (bot.centerx - name_tag.get_width() // 2, bot.y - 18))

            # collide
            if player.colliderect(bot):
                game_over = True
                score += 1
    score_display = font.render(f"LVL: {current_level}  |  ITEMS: {items_collected}/{items_needed}  |  SCORE: {score // 10}", True, (255, 255, 255))
    screen.blit(score_display, (20, 20))
    pygame.display.flip()
