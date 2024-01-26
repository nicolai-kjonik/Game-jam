import pygame
import math
import random
import numpy as np

class Spillerobjekt():
    def __init__(self, start_x, start_y):
        self.x = start_x
        self.y = start_y
        self.color = "grey"
        self.size = 5
        self.rect = pygame.Rect((self.x, self.y),(self.size*2, self.size*2))

    def tegn(self):
        pygame.draw.rect(screen, self.color, self.rect)
        self.rect = pygame.Rect((self.x, self.y), (self.size*2, self.size*2))

class Trampoline(Spillerobjekt):
    def __init__(self, start_x, start_y):
        super().__init__(start_x, start_y)
        self.x = start_x
        self.y = start_y
        self.color = "white"
        self.size = 8
        self.fart = 5
        self.rect = pygame.Rect((self.x, self.y),(self.size*10, self.size*2))

    def oppdater(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.x -= self.fart
        if keys[pygame.K_d]:
            self.x += self.fart

    def tegn(self):
        pygame.draw.rect(screen, self.color, self.rect)
        self.rect = pygame.Rect((self.x, self.y), (self.size*10, self.size*2))

class Isak(Spillerobjekt):
    def __init__(self, start_x, start_y):
        super().__init__(start_x, start_y)
        self.x = start_x
        self.y = start_y
        self.r = 10
        self.a = 0.02
        self.v = 0
        self.rect = pygame.Rect((self.x -(math.sqrt(2)/2)*self.r, self.y-(math.sqrt(2)/2)*self.r), (math.sqrt(2)*self.r, math.sqrt(2)*self.r))

    def oppdater(self):
        self.rect = pygame.Rect((self.x -(math.sqrt(2)/2)*self.r, self.y-(math.sqrt(2)/2)*self.r), (math.sqrt(2)*self.r, math.sqrt(2)*self.r))



pygame.init() 

screen = pygame.display.set_mode((700, 500)) # Setter skjermen til 700x500 piksler. 
clock = pygame.time.Clock() 


font = pygame.font.SysFont("Arial", int(screen.get_height()/30))
font2 = pygame.font.SysFont("Arial", 32)


spiller = Trampoline(screen.get_width()/2, screen.get_height()/1.2)
ball = Isak(screen.get_width()/2, screen.get_height()/2)
# Initialiserer objekter 

STARTING = True
INGAME = False
ENDING = False
RUNNING = True 

while RUNNING: 
 # Avslutter løkken 
    for event in pygame.event.get():

        if event.type == pygame.QUIT: 
            RUNNING = False 

        if pygame.key.get_pressed()[pygame.K_RETURN] and STARTING:
            print("Ching")
            STARTING = False
            INGAME = True
            inputword = ""
            break


    screen.fill("black") 

    if STARTING:
        # Tegn tittel tekst osv
        tekst1 = font2.render("Bouncing Isak", True, "white")
        tekst_rect1 = tekst1.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
        screen.blit(tekst1, tekst_rect1)

        # Tegn press return for å starte start
        tekst2 = font.render("Press enter to start", True, "white")
        tekst_rect2 = tekst2.get_rect(center=(screen.get_width()/2, screen.get_height()/1.5))
        screen.blit(tekst2, tekst_rect2)


    if INGAME:
        # Tegner og oppdaterer spiller 
        spiller.tegn()
        spiller.oppdater()
        # Tegne og oppdatere ball
        pygame.draw.circle(screen, "white", [ball.x, ball.y], ball.r)
        ball.oppdater()
        pygame.draw.rect(screen, "white", ball.rect)

        # Fartegenskaper til ball
        ball.y += ball.v
        ball.v += ball.a

        # Kollisjon 

        if pygame.Rect.colliderect(spiller.rect, ball.rect):
            ball.a -= 0.2
            while ball.v < 2:
                ball.v = 0
                ball.a = 0.02
                ball.y += ball.v
                ball.v += ball.a
            
    
    
    # Oppdaterer hele skjermen 

    pygame.display.flip() 

    # Forsikrer at spillet kjører i maksimalt 60 FPS. 

    clock.tick(60) 

# Avslutter spillet 

pygame.quit() 