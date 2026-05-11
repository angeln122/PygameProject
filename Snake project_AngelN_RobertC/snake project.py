from gamelib import *
from random import *

game = Game(800,600,"Snake")

# Background
bg = Image("images/Snake Bg.jpg", game)
bg.resizeTo(800,600)
#play button
play = Image("images/Play.png",game)
play.resizeBy(2)
play.y = 250
#story button
story = Image("images/Story.png",game)
story.resizeBy(2)
story.y = 380

Story = Image("images/Story.True.png",game)
Story.resizeTo(800,700)
Story.y = 280
Story.visible = False

#how to play button
how = Image("images/How.png",game)
how.resizeBy(2)
how.y = 500

#how to play button hover
how_on = Image("images/How2.png",game)
how_off = Image("images/How.png",game)
how_on.resizeBy(2)
how_on.y = 500

#play button hover
play_on = Image("images/Play2.png",game)
play_off = Image("images/Play.png",game)
play_on.resizeBy(2)
play_on.y = 500

#story button hover
story_on = Image("images/Story2.png",game)
story_off = Image("images/Story.png",game)
story_on.resizeBy(2)
story_on.y = 500

#how to play image
How = Image("images/How.True.png",game)
How.resizeTo(800,700)
How.y = 280
How.visible = False

eat = Sound ("Sounds/music_food.wav",0)
over = Sound ("Sounds/music_gameover.mp3",1)
move = Sound ("Sounds/music_move.mp3",2)
explode = Sound ("Sounds/explosion.wav",3)

you_win = Image("images/You Win!.png",game)
you_win.resizeTo(800,600)
you_lose = Image("images/You Lose!.png",game)
you_lose.resizeTo(800,600)

# Logo
logo = Image("images/snake logo.png",game)
logo.resizeBy(-60)
logo.y = 100

bomb = Image("images/bomb.png", game)
bomb.resizeBy(-85)
bomb.moveTo(randint(100,700), randint(100,500))

bomb2 = Image("images/bomb.png", game)
bomb2.resizeBy(-85)
bomb2.moveTo(randint(100,700), randint(100,500))

explosion = Animation("images/explosion.png",14,game,512/4,512/4)
explosion.visible = False

bomb.y = -randint(10, 200)
bomb.x = randint(100, 700)
bomb.setSpeed(18,180)

bomb2.y = -randint(10, 200)
bomb2.x = randint(100, 700)
bomb2.setSpeed(18,180)

# Snake
snake = Image("images/snake model.png",game)
snake.resizeBy(-60)
snake.moveTo(400,300)

#snake opp 1
snakeE1 = Animation("images/snakeE1.png",10,game,320/10,22/1,3)
snakeE1.resizeBy(250)

#snakeE1.setSpeed(10,60)
snakeE1.y =0
snakeE1.x =400
snakeE1.setSpeed(18,180)
snakeE1.visible=False

#snake opp 2
snakeE2 = Animation("images/snakeE2.png",10,game,320/10,22/1,3)
snakeE2.resizeBy(250)
snakeE2.setSpeed(10,40)
snakeE2.visible=False

#snakeE2.setSpeed(10,60)
snakeE2.y =0
snakeE2.x =300
snakeE2.setSpeed(18,80)
snakeE2.visible=False

#snake opp 3
snakeE3 = Animation("images/snakeE3.png",10,game,320/10,22/1,3)
snakeE3.resizeBy(250)
snakeE3.setSpeed(10,120)
snakeE3.visible=False

snakeE3.y =0
snakeE3.x =500
snakeE3.setSpeed(18,20)
snakeE3.visible=False
snakeSpeed = 5

# Apple
apple = Image("images/apple.png",game)
apple.resizeBy(-90)
apple.moveTo(randint(100,700), randint(100,500))
apple.visible = False

apple2 = Image("images/apple2.png",game)
apple2.visible = True
apple2.resizeBy(-90)

healthbar = Shape("bar",game, snake.health, 10, green)
progressbar = Shape("bar" , game, 200, 10, magenta)
progressbar.moveTo(10,30)
progressbar2 = Shape("bar" , game, 200, 10, magenta)
progressbar2.moveTo(10,30)


# Score
game.score = 0

snake.health = 100

mouse.visible = False

# Start screen
while not game.over:
    game.processInput()
    bg.draw()
    logo.draw()
    play.draw()
    story.draw()
    how.draw()

    How.draw()
    Story.draw()

    apple2.moveTo(mouse.x, mouse.y)
    #texts turn white upon hover
    if apple2.collidedWith(how,"rectangle"):
        how.setImage(how_on.image)
    else:
        how.setImage(how_off.image)
    apple2.moveTo(mouse.x, mouse.y)
    
    #texts turn white upon hover
    if apple2.collidedWith(story,"rectangle"):
        story.setImage(story_on.image)
    else:
        story.setImage(story_off.image)
        
    #texts turn white upon hover
    if apple2.collidedWith(play,"rectangle"):
        play.setImage(play_on.image)
    else:
        play.setImage(play_off.image)
    #when clicked on play
    if apple2.collidedWith(play,"rectangle") and mouse.LeftClick:
        game.over = True
    #when clicked on how to play
    if apple2.collidedWith(how,"rectangle") and mouse.LeftClick:
        How.visible = True
        How.draw()
    #when clicked on story
    if apple2.collidedWith(story,"rectangle") and mouse.LeftClick:
        Story.visible = True
        Story.draw()
    #exits story + htp
    if keys.Pressed[K_SPACE]:
        How.visible = False
        Story.visible = False        

    game.update(60)

# Start game
game.over = False

while not game.over:
    game.processInput()

    bg.draw()

    apple.visible = True
    apple.draw()
    snake.draw()
    bomb.move()
    bomb2.move()
    explosion .draw(False)
    progressbar.draw()
    progressbar.width = 100 - game.score *10

    healthbar.moveTo(snake.x-45,snake.y--30)
    healthbar.width = snake.health
    healthbar.x = snake.x - healthbar.width / 2

    # Apple collision
    if snake.collidedWith(apple):
        apple.moveTo(randint(100,700), randint(100,500))
        game.score += 1
        snakeSpeed += 0.5
        eat.play()
        
    if snake.collidedWith(bomb):
        snake.health-=20
        bomb.visible = False
        explosion.visible = True
        explosion.moveTo(snake.x, snake.y)

    if snake.collidedWith(bomb2):
        snake.health-=20
        bomb2.visible = False
        explosion.visible = True
        explosion.moveTo(snake.x, snake.y)
        explode.play()


    if snake.health <= 19:
        game.over=True
        over.play() 

    if bomb.y > game.height + 100:
        bomb.y = randint(-500, -100)
        bomb.x = randint(100, 700)
        bomb.visible = True

    if bomb2.y > game.height + 100:
        bomb2.y = randint(-500, -100)
        bomb2.x = randint(100, 700)
        bomb2.visible = True

    # Movement
    if keys.Pressed[K_UP]:
        snake.rotateTo(-90)
        snake.y -= snakeSpeed

    if keys.Pressed[K_DOWN]:
        snake.rotateTo(90)
        snake.y += snakeSpeed

    if keys.Pressed[K_RIGHT]:
        snake.rotateTo(180)
        snake.x += snakeSpeed

    if keys.Pressed[K_LEFT]:
        snake.rotateTo(0)
        snake.x -= snakeSpeed

    # Border check
    if snake.x > 800 or snake.x < 0 or snake.y > 600 or snake.y < 0:
        snake.Health =0
        game.over = True
        over.play()

    if game.score==10:
        game.over = True

    game.update(30)

game.over = False

#Second Level
while not game.over and snake.health >= 20:
    
    game.processInput()
    bomb.visible = False
    
    bg.draw()
    snake.draw()
    apple.draw()

    # second progress bar
    progressbar2.draw()
    progressbar2.width = 300 - game.score *10

    
    snakeE1.move()
    snakeE1.visible= True

    healthbar.moveTo(snake.x-45,snake.y--30)
    healthbar.width = snake.health
    healthbar.x = snake.x - healthbar.width / 2

    if game.score >=15:
        snakeE2.visible= True
        snakeE2.move()

    if snakeE1.y > 500:
        snakeE1.setSpeed(10,60)
        snakeE1.move(True)
     
    if game.score >=20:
        snakeE3.visible= True
        snakeE3.move()

    # Apple collision
    if snake.collidedWith(apple):
        apple.moveTo(randint(100,700), randint(100,500))
        game.score += 1
        snakeSpeed += 0.5
        snake.health += 5
        eat.play()

    if snake.collidedWith(snakeE1):
        snake.health-=5
    if snake.collidedWith(snakeE2):
        snake.health-=5        
    if snake.collidedWith(snakeE3):
        snake.health-=6

    if snake.health <=19:
        game.over = True
        over.play()
    # Movement
    if keys.Pressed[K_UP]:
        snake.rotateTo(-90)
        snake.y -= snakeSpeed

    if keys.Pressed[K_DOWN]:
        snake.rotateTo(90)
        snake.y += snakeSpeed

    if keys.Pressed[K_RIGHT]:
         snake.rotateTo(180)
         snake.x += snakeSpeed

    if keys.Pressed[K_LEFT]:
        snake.rotateTo(0)
        snake.x -= snakeSpeed

    if game.score == 30:
        game.over = True

    # Border check
    if snake.x > 800 or snake.x < 0 or snake.y > 600 or snake.y < 0:
        game.over = True
        snake.health =0
        over.play()

    # SnakeE1 check
    if snakeE1.x > 700 or snakeE1.x < 0 or snakeE1.y > 500 or snakeE1.y < 0 and snakeE1.y < 800:
        snakeE1.move(True)
        move.play()
    # SnakeE2 check
    if snakeE2.x > 700 or snakeE2.x < 0 or snakeE2.y > 500 or snakeE2.y < 0 and snakeE2.y < 800:
        snakeE2.move(True)
        move.play()
    # SnakeE3 check
    if snakeE3.x > 700 or snakeE3.x < 0 or snakeE3.y > 500 or snakeE3.y < 0 and snakeE3.y < 800:
        snakeE3.move(True)
        move.play()

    game.update(30)

#Game Over Screen
game.over = False
while not game.over:
    game.processInput()
    bg.draw()

    if game.score == 30:
        you_win.draw()

    if snake.health <= 19:
        you_lose.draw()

    if keys.Pressed [K_SPACE]:
        game.over = True

    game.update(30)
game.quit()
