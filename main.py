import pygame
import random
import pygame_textinput
from pygame.mixer import Sound

pygame.init()

# defining window size
win = pygame.display.set_mode((1000, 550))

# setting program caption
pygame.display.set_caption("Light Speed")

# importing all images
rocketRaw = pygame.image.load('Images/Rocket.png')  # imports image
rocket = pygame.transform.scale(rocketRaw, (150, 90))  # re-sizes image
meteorRaw = pygame.image.load('Images/astroid.png')
meteorPic = pygame.transform.scale(meteorRaw, (120, 120))
longmeteorPic = pygame.transform.scale(meteorRaw, (170, 120))
heart0 = pygame.transform.scale(pygame.image.load('Images/Heart0.png'), (90, 40))
heart1 = pygame.transform.scale(pygame.image.load('Images/Heart1.png'), (130, 50))
heart2 = pygame.transform.scale(pygame.image.load('Images/Heart2.png'), (130, 50))
heart3 = pygame.transform.scale(pygame.image.load('Images/Heart3.png'), (130, 50))
heartpics = [heart1, heart2, heart3, heart0]  # creates list of heart images
bgmenuraw = pygame.image.load('Images/bgmenu.png')
bgmenu = pygame.transform.scale(bgmenuraw, (1000, 550))
bg1raw = pygame.image.load('Images/bg1.png')
bg1 = pygame.transform.scale(bg1raw, (1000, 550))
bg2raw = pygame.image.load('Images/bg2.png')
bg2 = pygame.transform.scale(bg2raw, (1000, 550))
bg3raw = pygame.image.load('Images/bg3.png')
bg3 = pygame.transform.scale(bg3raw, (1000, 550))
bg4raw = pygame.image.load('Images/bg4.png')
bg4 = pygame.transform.scale(bg4raw, (1000, 550))
earthbuttonraw = pygame.image.load('Images/earthbutton.png')
earthbutton = pygame.transform.scale(earthbuttonraw, (150, 150))
marsbuttonraw = pygame.image.load('Images/marsbutton.png')
marsbutton = pygame.transform.scale(marsbuttonraw, (150, 150))
saturnbuttonraw = pygame.image.load('Images/saturnbutton.png')
saturnbutton = pygame.transform.scale(saturnbuttonraw, (150, 150))
neptunebuttonraw = pygame.image.load('Images/neptunebutton.png')
neptunebutton = pygame.transform.scale(neptunebuttonraw, (150, 150))

# importing all sounds
collisionsound = [pygame.mixer.Sound('Audio/1.wav'), pygame.mixer.Sound('Audio/2.wav'), pygame.mixer.Sound('Audio/3.wav'),
                  pygame.mixer.Sound('Audio/4.wav'), pygame.mixer.Sound('Audio/5.wav'), pygame.mixer.Sound('Audio/6.wav'),
                  pygame.mixer.Sound('Audio/7.wav'), pygame.mixer.Sound('Audio/8.wav'), pygame.mixer.Sound('Audio/9.wav')]
bulletsound = pygame.mixer.Sound('Audio/Gunshot.wav')
selectsound = pygame.mixer.Sound('Audio/selectsound.wav')
explosion = pygame.mixer.Sound('Audio/explosion.wav')
music = pygame.mixer.music.load('Audio/BgMusic.mp3')
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()
textinput = pygame_textinput.TextInput()

# main menu function
def menu():
    def redrawGameWindow():  # displays background and text on screen
        win.blit(bgmenu, (0, 0))
        screenText()
        pygame.display.update()

    def screenText():
        # adding title text
        font = pygame.font.Font('ARCADECLASSIC.TTF', 150)  # setting font
        text = font.render('Lightspeed', 1, (255, 255, 255))  # setting text attributes
        win.blit(text, (500 - ((text.get_width() / 2) - 20), 40))  # displaying text on screen

        # pygame.draw.rect(win, (0, 100, 200), [(500 - (140 / 2)), 280, 140, 40])

        # adding play text
        font2 = pygame.font.Font('ARCADECLASSIC.TTF', 50)
        text2 = font2.render('Play', 1, (255, 255, 255))
        win.blit(text2, (500 - ((text2.get_width() / 2) - 8), 262))

        # adding credits text
        font3 = pygame.font.Font('ARCADECLASSIC.TTF', 20)
        text3 = font3.render((
                'Created' + '   ' + 'by' + '   ' + 'Alex' + '   ' + 'Manning' + '   ' + 'George' + '   ' + 'Hart' + '   ' + 'and' + '   ' + 'Isaac' + '   ' + 'Milley' + '   ' + '2021'),
            1, (255, 255, 255))
        win.blit(text3, (500 - (text3.get_width() / 2), 490))

    run = True
    while run:
        clock.tick(27)

        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # checks if exit button is clicked and exits program
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:  # checks if mouse is clicked and if it is in button area
                if mouse[0] >= 430 and mouse[0] <= 570 and mouse[1] >= 280 and mouse[1] <= 320:
                    selectsound.play()  # plays click sound
                    instructions()  # calls next screen

        mouse = pygame.mouse.get_pos()

        redrawGameWindow()

# instructions screen function
def instructions():
    def redrawGameWindow():  # displays background and text on screen
        win.blit(bg1, (0, 0))
        screenText()
        pygame.display.update()

    def screenText():

        #  adding title text
        font = pygame.font.Font('ARCADECLASSIC.TTF', 150)
        text = font.render('Lightspeed', 1, (255, 255, 255))
        win.blit(text, (500 - ((text.get_width() / 2) - 20), 40))

        # adding instructions text
        font2 = pygame.font.Font('ARCADECLASSIC.TTF', 60)
        text2 = font2.render('Instructions', 1, (255, 255, 255))
        win.blit(text2, (500 - (text2.get_width() / 2), 150))

        # adding paragraph text
        font3 = pygame.font.Font('ARCADECLASSIC.TTF', 30)
        text3 = font3.render((
                'Welcome' + '   ' + 'to' + '   ' + 'Lightspeed' + '   ' + 'Your' + '   ' + 'mission' + '   ' + 'is' + '   ' + 'to' + '   ' + 'survive'),
            1, (255, 255, 255))
        text4 = font3.render((
                'the' + '   ' + 'astroid' + '   ' + 'strike' + '   ' + 'by' + '   ' + 'answering' + '   ' + 'math' + '   ' + 'questions'),
            1, (255, 255, 255))
        text5 = font3.render((
                'To' + '   ' + 'move' + '   ' + 'your' + '   ' + 'ship' + '   ' + 'use' + '   ' + 'the' + '   ' + 'up' + '   ' + 'and' + '   ' + 'down' + '   ' + 'arrow' + '   ' + 'keys'),
            1, (255, 255, 255))
        text6 = font3.render((
                'To' + '   ' + 'shoot' + '   ' + 'hit' + '   ' + 'the' + '   ' + 'space' + '   ' + 'bar' + '   ' + 'Good' + '   ' + 'luck' + '   ' + 'comrad'),
            1, (255, 255, 255))
        win.blit(text3, (500 - (text3.get_width() / 2), 220))
        win.blit(text4, (500 - (text4.get_width() / 2), 240))
        win.blit(text5, (500 - (text5.get_width() / 2), 260))
        win.blit(text6, (500 - (text6.get_width() / 2), 280))

        pygame.draw.rect(win, (0, 100, 200), [(500 - (140 / 2)), 440, 130, 40])  # adding button rectangle

        # adding next text
        font4 = pygame.font.Font('ARCADECLASSIC.TTF', 50)
        text4 = font4.render('Next', 1, (255, 255, 255))
        win.blit(text4, (500 - (text4.get_width() / 2), 435))

    run = True
    while run:
        clock.tick(27)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:  # checks where and if mouse is clicked on button
                if mouse[0] >= 430 and mouse[0] <= 570 and mouse[1] >= 440 and mouse[1] <= 480:
                    selectsound.play()
                    ageinputscreen()

        mouse = pygame.mouse.get_pos()

        redrawGameWindow()

def ageinputscreen():
    def redrawGameWindow():
        win.blit(bg1, (0, 0))
        screenText()
        win.blit(textinput.get_surface(), (450, 293))
        ageChecker()
        pygame.display.update()

    def screenText():

        # adding title text
        font = pygame.font.Font('ARCADECLASSIC.TTF', 150)
        text = font.render('Lightspeed', 1, (255, 255, 255))
        win.blit(text, (500 - ((text.get_width() / 2) - 20), 40))

        # adding more text
        font2 = pygame.font.Font('ARCADECLASSIC.TTF', 80)
        text2 = font2.render('Enter your age', 1, (255, 255, 255))
        win.blit(text2, (500 - (text2.get_width() / 2), 180))

        pygame.draw.rect(win, (0, 100, 200), [(500 - (140 / 2)), 440, 130, 40])  # adding button rectangle
        pygame.draw.rect(win, (255, 255, 255), [(500 - (200 / 2)), 300, 200, 80])

        # adding next text
        font4 = pygame.font.Font('ARCADECLASSIC.TTF', 50)
        text4 = font4.render('Next', 1, (255, 255, 255))
        win.blit(text4, (500 - (text4.get_width() / 2), 435))

    def ageChecker():
        if ageVar == 1:  # checks if user is too young
            font4 = pygame.font.Font('ARCADECLASSIC.TTF', 50)
            text4 = font4.render('You are too young!', 1, (255, 255, 255))
            win.blit(text4, (500 - (text4.get_width() / 2), 380))

        if ageVar == 2:  # checks if user is too old
            font4 = pygame.font.Font('ARCADECLASSIC.TTF', 50)
            text4 = font4.render('You are too old!', 1, (255, 255, 255))
            win.blit(text4, (500 - (text4.get_width() / 2), 380))

        if ageVar == 3:  # checks if user input was not valid number
            font4 = pygame.font.Font('ARCADECLASSIC.TTF', 50)
            text4 = font4.render('Please   enter   a   valid   number!', 1, (255, 255, 255))
            win.blit(text4, (500 - (text4.get_width() / 2), 380))

    ageVar = 0
    run = True
    while run:
        clock.tick(27)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:  # checks where and if mouse is clicked on button
                if mouse[0] >= 430 and mouse[0] <= 570 and mouse[1] >= 440 and mouse[1] <= 480:
                    selectsound.play()
                    try:  # trys to convert input to int
                        userAge = int(textinput.get_text())

                        if userAge >= 5 and userAge <= 13:  # if user age is within range calls next screen
                            levelscreen(userAge)
                        else:
                            if userAge < 5:  # if user to young change age variable
                                ageVar = 1
                            if userAge > 13:  # if user to old change age variable
                                ageVar = 2

                    except ValueError:  # if ValueError occurs change age variable
                        ageVar = 3

        textinput.update(events)

        mouse = pygame.mouse.get_pos()

        redrawGameWindow()

def levelscreen(userAge):
    def redrawGameWindow(userAge):  # displays background, images and text on screen
        win.blit(bg1, (0, 0))
        win.blit(earthbutton, (105, 323))
        win.blit(marsbutton, (315, 323))
        win.blit(saturnbutton, (530, 323))
        win.blit(neptunebutton, (740, 323))
        screenText(userAge)
        pygame.display.update()

    def screenText(userAge):

        # adding title text
        font = pygame.font.Font('ARCADECLASSIC.TTF', 150)
        text = font.render('Lightspeed', 1, (255, 255, 255))
        win.blit(text, (500 - ((text.get_width() / 2) - 20), 40))

        # adding select level text
        font2 = pygame.font.Font('ARCADECLASSIC.TTF', 80)
        text2 = font2.render('Select Level', 1, (255, 255, 255))
        win.blit(text2, (500 - (text2.get_width() / 2), 180))

        # adding level number text
        font3 = pygame.font.Font('ARCADECLASSIC.TTF', 80)
        text3 = font3.render('1', 1, (255, 255, 255))
        text3a = font3.render('2', 1, (255, 255, 255))
        text3b = font3.render('3', 1, (255, 255, 255))
        text3c = font3.render('4', 1, (255, 255, 255))
        win.blit(text3, (180 - (text3.get_width() / 2), 400 - (text3.get_height() / 2)))
        win.blit(text3a, (393.3 - (text3a.get_width() / 2), 400 - (text3.get_height() / 2)))
        win.blit(text3b, (606.6 - (text3b.get_width() / 2), 400 - (text3.get_height() / 2)))
        win.blit(text3c, (819.9 - (text3c.get_width() / 2), 400 - (text3.get_height() / 2)))

        if userAge >= 5 and userAge <= 7:
            z = 100
        if userAge >= 8 and userAge <= 10:
            z = 307
        if userAge >= 11 and userAge <= 12:
            z = 517
        if userAge == 13:
            z = 730

        font2 = pygame.font.Font('ARCADECLASSIC.TTF', 20)
        text2 = font2.render('Recommended level', 1, (255, 255, 255))
        win.blit(text2, (z, 300))

    run = True
    while run:
        clock.tick(27)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            # checks if mouse is click and checks which button it clicks on.
            # Then changes 'level' variable and calls mainGame function
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse[0] >= 137.5 and mouse[0] <= 222.5 and mouse[1] >= 357.5 and mouse[1] <= 442.5:
                    level = 1
                    selectsound.play()
                    mainGame(level)
                if mouse[0] >= 350.8 and mouse[0] <= 435.8 and mouse[1] >= 357.5 and mouse[1] <= 442.5:
                    level = 2
                    selectsound.play()
                    mainGame(level)
                if mouse[0] >= 564.1 and mouse[0] <= 649.1 and mouse[1] >= 357.5 and mouse[1] <= 442.5:
                    level = 3
                    selectsound.play()
                    mainGame(level)
                if mouse[0] >= 777.4 and mouse[0] <= 862.4 and mouse[1] >= 357.5 and mouse[1] <= 442.5:
                    level = 4
                    selectsound.play()
                    mainGame(level)

        mouse = pygame.mouse.get_pos()

        redrawGameWindow(userAge)

# game function
def mainGame(level):
    class player(object):
        def __init__(self, x, y, width, height):  # initializing player (rocket) object
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.vel = 10  # speed of rocket
            self.hitbox = (self.x + 10, self.y, 100, 90)  # hit box dimensions
            self.heartCounter = 3

        def draw(self, win):  # displays player (rocket)
            win.blit(rocket, (self.x, self.y))
            self.hitbox = (self.x + 10, self.y, 100, 90)
            # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

        def hit(self):  # this function is called if the rocket collides with an asteroid
            (random.choice(collisionsound)).play()  # plays random collsion sound
            pygame.display.update()
            spaceship.heartCounter -= 1  # takes away one from heartCounter variable

            # displays heart image according to value of heartCounter
            if spaceship.heartCounter == 2:
                heartInGame.heartpicsCurrent = heartpics[1]
            if spaceship.heartCounter == 1:
                heartInGame.heartpicsCurrent = heartpics[0]
            if spaceship.heartCounter == 0:
                heartInGame.heartpicsCurrent = heartpics[3]
                print("game over")

            # delay in program to allow for code above to run properly
            i = 0
            while i < 3:
                pygame.time.delay(10)
                i += 1
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        i = 301
                        pygame.quit()

    class projectile(object):
        def __init__(self, x, y, radius, colour):  # initializing projectile (bullet) object
            self.x = x
            self.y = y
            self.radius = radius
            self.colour = colour
            self.vel = 70  # speed

        def draw(self, win):  # displays grey circle
            pygame.draw.circle(win, self.colour, (self.x, self.y), self.radius)

    class rock(object):
        def __init__(self, x, y, width, height, end):  # initializing rock (asteroid) object
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.path = [x, end]
            self.vel = 8  # speed
            self.hitbox = (self.x, self.y + 10, 120, 100)  # hit box dimensions
            self.visible = True
            self.number = 0

        def draw(self, win):  # displays asteroid
            if self.visible:  # checks if the asteroid should be visible
                if level == 1:
                    win.blit(meteorPic, (self.x, self.y))
                if level == 2 or level == 3 or level ==4:
                    win.blit(longmeteorPic, (self.x, self.y))
                self.hitbox = (self.x, self.y + 10, 120, 100)

                font2 = pygame.font.Font('ARCADECLASSIC.TTF', 80)
                text = font2.render((str(self.number)), 1, (255, 255, 255))
                win.blit(text, (self.x + 30, self.y + 30))
                # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

        def hit(self):  # function is called if rocket shoots correct asteroid
            self.visible = False  # makes asteroid disappear

    class heart(object):
        def __init__(self, x, y, width, height):  # initializes heart object
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.visible = True
            self.heartpicsCurrent = heartpics[2]  # initial state is to display image of 3 hearts

        def draw(self, win):  # displays the appropriate heart image
            if self.visible:
                win.blit(self.heartpicsCurrent, (self.x, self.y))

    class question(object):  # question object
        def draw(self, a, b):  # displays question at bottom of screen
            self.a = a
            self.b = b
            font2 = pygame.font.Font('ARCADECLASSIC.TTF', 80)
            text = font2.render((str(self.a) + " x " + str(self.b)), 1, (255, 255, 255))
            win.blit(text, (500 - (text.get_width() / 2), 450))

    class score(object):  # score object
        def draw(self, score):  # displays current score in top right and exit button in top left
            self.score = score
            font2 = pygame.font.Font('ARCADECLASSIC.TTF', 40)
            text = font2.render(("Score " + str(score)), 1, (255, 255, 255))
            win.blit(text, (830, 5))
            text2 = font2.render(('Exit to menu'), 1, (255, 255, 255))
            win.blit(text2, (10, 5))

    class gameover(object):  # game over oject
        def draw(self, win, score):  # displays gameover text
            if spaceship.heartCounter == 0:
                font3 = pygame.font.Font('ARCADECLASSIC.TTF', 120)
                text = font3.render(('GAME OVER'), 1, (255, 255, 255))
                win.blit(text, ((500 - text.get_width() / 2), 50))
                font4 = pygame.font.Font('ARCADECLASSIC.TTF', 60)
                text2 = font4.render(('SCORE ' + str(score)), 1, (255, 255, 255))
                win.blit(text2, ((500 - text2.get_width() / 2), 150))
                text3 = font4.render(
                    ('Press' + '   ' + 'enter' + '   ' + 'to' + '   ' + 'go' + '   ' + 'to' + '   ' + 'menu'), 1,
                    (255, 255, 255))
                win.blit(text3, ((500 - text3.get_width() / 2), 300))



    def redrawGameWindow(a, b, score, scorequestionVisible, level):  # displays all objects on screen

        # checks what level and displys the correct background image
        if level == 1:
            win.blit(bg1, (0, 0))
        if level == 2:
            win.blit(bg2, (0, 0))
        if level == 3:
            win.blit(bg3, (0, 0))
        if level == 4:
            win.blit(bg4, (0, 0))

        spaceship.draw(win)
        meteorTop.draw(win)
        meteorMiddle.draw(win)
        meteorBottom.draw(win)
        heartInGame.draw(win)

        # checks if the score and question should be being displayed
        if scorequestionVisible == True:
            questionGame.draw(a, b)
            scoreGame.draw(score)

        gameoverGame.draw(win, score)

        for bullet in bullets:
            bullet.draw(win)

        pygame.display.update()

    # mainloop

    # defining all attributes to all objects when game starts
    spaceship = player(104, 235, 100, 100)
    meteorTop = rock(800, 40, 100, 100, 300)
    meteorMiddle = rock(800, 190, 100, 100, 300)
    meteorBottom = rock(800, 340, 100, 100, 300)
    heartInGame = heart(30, 490, 30, 30)
    questionGame = question()
    scoreGame = score()
    gameoverGame = gameover()
    bullets = []
    run = True

    # checks level and changes what the range of the random numbers in questions can be and defines the random numbers
    if level == 1:
        number1 = random.randint(1, 3)
        number2 = random.randint(1, 3)
    if level == 2:
        number1 = random.randint(1, 6)
        number2 = random.randint(1, 6)
    if level == 3:
        number1 = random.randint(1, 9)
        number2 = random.randint(1, 9)
    if level == 4:
        number1 = random.randint(1, 19)
        number2 = random.randint(1, 19)

    scorenumber = 0
    whichComet = random.randint(1, 3)  # randomly chooses what asteroid will have correct answer

    # displays possible answers on asteroids depending on whichComet variable
    if whichComet == 1:
        meteorTop.number = number1 * number2  # calculates correct answer value
        meteorMiddle.number = random.randint(1, 30)  # displays random number
        meteorBottom.number = random.randint(1, 30)  # "                     "
    if whichComet == 2:
        meteorTop.number = random.randint(1, 30)
        meteorMiddle.number = number1 * number2
        meteorBottom.number = random.randint(1, 30)
    if whichComet == 3:
        meteorTop.number = random.randint(1, 30)
        meteorMiddle.number = random.randint(1, 30)
        meteorBottom.number = number1 * number2
    w = 1
    scorequestionVisible = True  # tells draw function to draw the score, question and exit button

    while run:
        clock.tick(27)

        if spaceship.heartCounter == 0:  # if player has no hearts
            if meteorTop.x == 1200:  # waits till asteroids are off screen
                meteorTop.vel = 0  # sets asteroid speed to zero
                meteorMiddle.vel = 0
                meteorBottom.vel = 0
            spaceship.vel = 0  # stops rocket
            if keys[pygame.K_KP_ENTER] or keys[pygame.K_RETURN]:  # checks if enter has been pressed
                menu()  # calls menu
            scorequestionVisible = False  # tells draw function to not display the score, question and exit button

        meteorTop.x -= meteorTop.vel  # subtracts asteroid 'x' value by velocity
        meteorMiddle.x -= meteorMiddle.vel  # variable every loop to create illusion of backwards movement
        meteorBottom.x -= meteorBottom.vel

        if meteorTop.x == -176:  # when asteroid reaches end of screen
            meteorTop.x = 1200  # teleport asteroid to the other end of screen
            meteorTop.visible = True  # if an asteroid has been destroyed it is respawned here
            # generates random numbers again so the question changes
            # also the random number range is dependent on level
            if level == 1:
                number1 = random.randint(1, 3)
                number2 = random.randint(1, 3)
            if level == 2:
                number1 = random.randint(1, 6)
                number2 = random.randint(1, 6)
            if level == 3:
                number1 = random.randint(1, 9)
                number2 = random.randint(1, 9)
            if level == 4:
                number1 = random.randint(1, 19)
                number2 = random.randint(1, 19)

            whichComet = random.randint(1, 3)  # changes asteroid with correct answer

        # respawns and moves other asteroids to the other end of screen
        if meteorMiddle.x == -176:
            meteorMiddle.x = 1200
            meteorMiddle.visible = True
        if meteorBottom.x == -176:
            meteorBottom.x = 1200
            meteorBottom.visible = True

            if whichComet == 1:  # checks what asteroid to display correct answer on
                meteorTop.number = number1 * number2  # displays correct answer on top asteroid
                # checks level to see what the range of possible answers should be
                if level == 1:
                    meteorMiddle.number = random.randint(1, 9)  # displays random numbers on other two asteroids \/
                    meteorBottom.number = random.randint(1, 9)
                if level == 2:
                    meteorMiddle.number = random.randint(1, 40)
                    meteorBottom.number = random.randint(1, 40)
                if level == 3:
                    meteorMiddle.number = random.randint(1, 90)
                    meteorBottom.number = random.randint(1, 90)
                if level == 4:
                    meteorMiddle.number = random.randint(1, 400)
                    meteorBottom.number = random.randint(1, 400)

            if whichComet == 2:  # checks what asteroid to display correct answer on
                meteorMiddle.number = number1 * number2
                if level == 1:
                    meteorTop.number = random.randint(1, 9)
                    meteorBottom.number = random.randint(1, 9)
                if level == 2:
                    meteorTop.number = random.randint(1, 40)
                    meteorBottom.number = random.randint(1, 40)
                if level == 3:
                    meteorTop.number = random.randint(1, 90)
                    meteorBottom.number = random.randint(1, 90)
                if level == 4:
                    meteorTop.number = random.randint(1, 400)
                    meteorBottom.number = random.randint(1, 400)

            if whichComet == 3:  # checks what asteroid to display correct answer on
                meteorBottom.number = number1 * number2
                if level == 1:
                    meteorMiddle.number = random.randint(1, 9)
                    meteorTop.number = random.randint(1, 9)
                if level == 2:
                    meteorMiddle.number = random.randint(1, 40)
                    meteorTop.number = random.randint(1, 40)
                if level == 3:
                    meteorMiddle.number = random.randint(1, 90)
                    meteorTop.number = random.randint(1, 90)
                if level == 4:
                    meteorMiddle.number = random.randint(1, 400)
                    meteorTop.number = random.randint(1, 400)

        if meteorTop.visible == True:  # checks if top asteroid is showing
            if spaceship.hitbox[1] < meteorTop.hitbox[1] + meteorTop.hitbox[3] and spaceship.hitbox[1] + \
                    spaceship.hitbox[
                        3] > meteorTop.hitbox[1]:  # checks if the rocket at asteroid hit boxes have collided
                if spaceship.x == meteorTop.x:

                    spaceship.hit()  # class hit function

        if meteorMiddle.visible == True:  # checks if middle asteroid is showing
            if spaceship.hitbox[1] < meteorMiddle.hitbox[1] + meteorMiddle.hitbox[3] and spaceship.hitbox[1] + \
                    spaceship.hitbox[3] > meteorMiddle.hitbox[1]:
                if spaceship.x == meteorMiddle.x:  # checks if the rocket at asteroid hit boxes have collided

                    spaceship.hit()  # class hit function

        if meteorBottom.visible == True:   # checks if bottom asteroid is showing
            if spaceship.hitbox[1] < meteorBottom.hitbox[1] + meteorBottom.hitbox[3] and spaceship.hitbox[1] + \
                    spaceship.hitbox[3] > meteorBottom.hitbox[1]:
                if spaceship.x == meteorBottom.x:  # checks if the rocket at asteroid hit boxes have collided

                    spaceship.hit()   # class hit function

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # checks if exit button is pressed
                quit()  # quits game

            if event.type == pygame.MOUSEBUTTONDOWN:  # checks if mouse clicked
                if mouse[0] >= 10 and mouse[0] <= 240 and mouse[1] >= 10 and mouse[1] <= 50:  # checks if mosue is over exit button
                    selectsound.play()
                    menu()  # calls menu function
        mouse = pygame.mouse.get_pos()

        for bullet in bullets:

            if whichComet == 1:  # checks if top asteroid has correct answer
                if meteorTop.visible == True:
                    if bullet.y - bullet.radius < meteorTop.hitbox[1] + meteorTop.hitbox[
                        3] and bullet.y + bullet.radius > \
                            meteorTop.hitbox[1]:  # checks if bullet collided with asteroid
                        if bullet.x + bullet.radius > meteorTop.hitbox[0] and bullet.x - bullet.radius < \
                                meteorTop.hitbox[0] + \
                                meteorTop.hitbox[2]:  # checks if bullet collided with asteroid
                            bullets.pop(bullets.index(bullet))  # destroys bullet
                            scorenumber += 1  # adds point to score
                            explosion.play()
                            meteorTop.hit()  # calls the right meteor hit function

            if whichComet == 2:
                if meteorMiddle.visible == True:
                    if bullet.y - bullet.radius < meteorMiddle.hitbox[1] + meteorMiddle.hitbox[
                        3] and bullet.y + bullet.radius > \
                            meteorMiddle.hitbox[1]:
                        if bullet.x + bullet.radius > meteorMiddle.hitbox[0] and bullet.x - bullet.radius < \
                                meteorMiddle.hitbox[
                                    0] + meteorMiddle.hitbox[2]:
                            bullets.pop(bullets.index(bullet))
                            scorenumber += 1
                            explosion.play()
                            meteorMiddle.hit()

            if whichComet == 3:
                if meteorBottom.visible == True:
                    if bullet.y - bullet.radius < meteorBottom.hitbox[1] + meteorBottom.hitbox[
                        3] and bullet.y + bullet.radius > \
                            meteorBottom.hitbox[1]:
                        if bullet.x + bullet.radius > meteorBottom.hitbox[0] and bullet.x - bullet.radius < \
                                meteorBottom.hitbox[
                                    0] + meteorBottom.hitbox[2]:
                            bullets.pop(bullets.index(bullet))
                            scorenumber += 1
                            explosion.play()
                            meteorBottom.hit()

            if bullet.x < 1000 and bullet.x > 0:  # checks if bullet is off screen
                bullet.x += bullet.vel  # makes bullet move
            else:  # bullet must be off screen
                bullets.pop(bullets.index(bullet))  # destroys bullet


        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:  # checks if space bar is pressed
            if len(bullets) < 1:  # checks if there are less than one bullet
                bullets.append(
                    projectile(round(spaceship.x + spaceship.width + 10 // 2),
                               round(spaceship.y + spaceship.height // 2), 7, (117, 237, 255)))  # creates bullet
                bulletsound.play()  # plays bullet sound

        if keys[pygame.K_UP] and spaceship.y > 50:  # checks if up arrow is pressed
            spaceship.y -= spaceship.vel  # makes rocket go up
        elif keys[pygame.K_DOWN] and spaceship.y < 400:  # checks if down arrow is pressed
            spaceship.y += spaceship.vel  # makes rocket go down

        redrawGameWindow(number1, number2, scorenumber, scorequestionVisible, level)  # calls redraw function


menu()  # calls menu
pygame.quit()  # exits game
