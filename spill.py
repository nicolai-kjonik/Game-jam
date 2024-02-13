import pygame
import math
import random
import numpy as np
from pygame import mixer

# Spiller objekt klasse
class Spillerobjekt():
    def __init__(self, start_x, start_y):
        self.x = start_x
        self.y = start_y
        self.color = "grey"
        self.size = 5
        self.rect = pygame.Rect((self.x, self.y),(self.size*2, self.size*2))

# Spiller klassen
class Trampoline(Spillerobjekt):
    def __init__(self, start_x, start_y):
        super().__init__(start_x, start_y)
        self.x = start_x
        self.y = start_y
        self.color = "white"
        self.size = 15
        self.fart = 10
        self.image = pygame.image.load("trampoline.png")
        self.image = pygame.transform.scale(self.image, (self.size*10, self.size*2))
        self.rect = self.image.get_rect(center=(self.x, self.y))
#bevegelses funksjonen
    def oppdater(self):
        keys = pygame.key.get_pressed()
        self.rect = self.image.get_rect(center=(self.x, self.y))
        if keys[pygame.K_a]:
            self.x -= self.fart
        if keys[pygame.K_d]:
            self.x += self.fart
#tegn funksjon
    def tegn(self):
        screen.blit(self.image, self.rect.topleft)



# BAll klassen
class Isak(Spillerobjekt):
    def __init__(self, start_x, start_y, start_vx, start_vy):
        super().__init__(start_x, start_y)
        self.x = start_x
        self.y = start_y
        self.r = 10
        self.v = 5
        self.image = pygame.image.load("stein1.png")
        self.image = pygame.transform.scale(self.image, (self.size*20, self.size*25))
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.vx = start_vx
        self.vy = start_vy

    def tegn(self):
        screen.blit(self.image, self.rect.topleft)

    def oppdater(self):
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.x += self.vx * self.v
        self.y += self.vy * self.v

        if self.x > screen.get_width() or self.x < 0:
            self.vx *= -1
        
        if self.y > screen.get_height() or self.y < 0:
            self.vy *= -1    

pygame.init() 

screen = pygame.display.set_mode((700, 600)) # Setter skjermen til 700x500 piksler. 
clock = pygame.time.Clock() 

# Bakgrunns musikk
mixer.music.load("Rihanna - Where Have You Been (Hardstyle Bootleg).wav")
mixer.music.play(-1)

# Funksjon for bakgrunn
image = pygame.image.load ('toilet.png')
def Background_dass(image):
    size = pygame.transform.scale(image,(700, 600))
    screen.blit(size, (0, 0))

# Forskjellige fonter
font = pygame.font.SysFont("Arial", int(screen.get_height()/30))
font2 = pygame.font.SysFont("Arial", 32)
poeng_font = pygame.font.SysFont("Arial", int(screen.get_height()/25))

# Spiller og ball objekter
spiller = Trampoline(screen.get_width()/2, screen.get_height()/1.2)
ball = Isak(screen.get_width()/2, screen.get_height()/2, random.choice([1, -1]), 1)

# Poeng
counter = 0
poeng = 0

STARTING = True
INGAME = False
ENDING = False
RUNNING = True 

while RUNNING: 
 # Avslutter løkken 
    for event in pygame.event.get():

        # Hvis boolen RUNNING er false så slutter spillet
        if event.type == pygame.QUIT:  
            RUNNING = False  


        # Hvis man er i starting og enter blir trykket så starter spillet
        if pygame.key.get_pressed()[pygame.K_RETURN] and STARTING: 
            print("Ching")
            STARTING = False
            INGAME = True
            inputword = ""
            break

        # Hvis du har dødd og er i ending screen så går den tilbake til starting screenen
        if pygame.key.get_pressed()[pygame.K_RETURN] and ENDING: 
            print("Ching")
            ENDING = False
            STARTING = True

            counter = 0
            poeng = 0

            inputword = ""
            break
        
        # HVis du har dødd og presser backspace lukker spillet seg
        if pygame.key.get_pressed()[pygame.K_BACKSPACE] and ENDING: 
            print("Ching")
            RUNNING = False
            inputword = ""
            break

    if STARTING:

        # Fyller skjermen svart
        screen.fill("black")

        # Tegn tittel tekst osv
        tekst1 = font2.render("Bouncing Stian", True, "white")
        tekst_rect1 = tekst1.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
        screen.blit(tekst1, tekst_rect1)

        # Tegn press return for å starte start
        tekst2 = font.render("Press enter to start", True, "white")
        tekst_rect2 = tekst2.get_rect(center=(screen.get_width()/2, screen.get_height()/1.5))
        screen.blit(tekst2, tekst_rect2)


    if INGAME:
        # Tegner bakgrunnen før objektene
        Background_dass(image)

        # Tegner og oppdaterer spiller 
        spiller.tegn()
        spiller.oppdater()

        # Tegne og oppdatere ball
        ball.tegn()
        ball.oppdater()

        # Kollisjon 
        if pygame.Rect.colliderect(spiller.rect, ball.rect):
            if ball.vy > 0:
                ball.vy *= -1
                poeng += 1
                counter += 1
                  

        # Poengsum teller og triggerer
                
        if counter == 5:
            ball.v = ball.v * 1.5
            spiller.size = spiller.size * 0.8
            spiller.image = pygame.transform.scale(spiller.image, (spiller.size*10, spiller.size*2))
            counter = 0
            
        # Tegne poengsum
        tekst = poeng_font.render(str(poeng), True, "cyan")
        tekst_rect = tekst.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
        screen.blit(tekst, tekst_rect)

        # Resetter posisjoner og verdier hvis du dør
        if ball.y > screen.get_height():    
            ball.v = 5
            ball.r = 10
            ball = Isak(screen.get_width()/2, screen.get_height()/2, random.choice([1, -1]), 1)
            spiller.size = 15
            spiller = Trampoline(screen.get_width()/2, screen.get_height()/1.2)
            spiller.image = pygame.transform.scale(spiller.image, (spiller.size*10, spiller.size*2))

            
            INGAME = False
            ENDING = True

    # Slutt fasen
    if ENDING: 

        # Fyller skjermen med svart
        screen.fill("black") 

        #Skriver game over
        tekst3 = font2.render("GAME OVER", True, "white")   
        tekst_rect3 = tekst3.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
        screen.blit(tekst3, tekst_rect3)

        # Tegn press return for å starte start
        tekst4 = font.render("Press enter to restart, or backspace to end", True, "white")
        tekst_rect4 = tekst4.get_rect(center=(screen.get_width()/2, screen.get_height()/1.5))
        screen.blit(tekst4, tekst_rect4)

        # Tegner poengsum
        tekst = poeng_font.render(f"Your score is {str(poeng)}", True, "white")
        tekst_rect = tekst.get_rect(center=(screen.get_width()/2, screen.get_height()/4))
        screen.blit(tekst, tekst_rect)

        

    
    # Oppdaterer hele skjermen 

    pygame.display.flip() 

    # Forsikrer at spillet kjører i maksimalt 60 FPS. 

    clock.tick(60) 

# Avslutter spillet 

pygame.quit() 