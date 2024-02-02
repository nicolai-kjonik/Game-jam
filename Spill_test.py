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
        self.size = 15
        self.fart = 10
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
    def __init__(self, start_x, start_y, start_vx, start_vy, image):
        super().__init__(start_x, start_y)
        self.x = start_x
        self.y = start_y
        self.r = 10
        self.v = 5
#ISAK
        self.image = pygame.image.load("xxx.png")
        self.image = pygame.transform.scale(self.image, (self.size*7, self.size*10))
        self.rect = self.image.get_rect(center=(self.x, self.y))

        self.sheet = image
        self.vx = start_vx
        self.vy = start_vy
        self.rect = pygame.Rect((self.x -(math.sqrt(2)/2)*self.r, self.y-(math.sqrt(2)/2)*self.r), (math.sqrt(2)*self.r, math.sqrt(2)*self.r))

#ISAK
    def tegn(self):
        screen.blit(self.image, self.rect.topleft)

    def oppdater(self):
        self.rect = pygame.Rect((self.x -(math.sqrt(2)/2)*self.r, self.y-(math.sqrt(2)/2)*self.r), (math.sqrt(2)*self.r, math.sqrt(2)*self.r))
    
    def oppdater(self):
        self.rect = pygame.Rect((self.x -(math.sqrt(2)/2)*self.r, self.y-(math.sqrt(2)/2)*self.r), (math.sqrt(2)*self.r, math.sqrt(2)*self.r))
        self.x += self.vx * self.v
        self.y += self.vy * self.v

        if self.x > screen.get_width() or self.x < 0:
            self.vx *= -1
        
        if self.y > screen.get_height() or self.y < 0:
            self.vy *= -1    

"""
    def get_image(self, frame, width, height, scale, colour):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(colour)

        return image
"""



pygame.init() 

screen = pygame.display.set_mode((700, 500)) # Setter skjermen til 700x500 piksler. 
clock = pygame.time.Clock() 


font = pygame.font.SysFont("Arial", int(screen.get_height()/30))
font2 = pygame.font.SysFont("Arial", 32)

sprite_sheet_image = pygame.image.load('Mort.png').convert_alpha()
spiller = Trampoline(screen.get_width()/2, screen.get_height()/1.2)
ball = Isak(screen.get_width()/2, screen.get_height()/2, random.choice([1, -1]), 1, sprite_sheet_image)

counter = 0
poeng = 0
poeng_font = pygame.font.SysFont("Arial", int(screen.get_height()/30))
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

        # Kollisjon 
    
        if pygame.Rect.colliderect(spiller.rect, ball.rect):
            if ball.vy > 0:
                ball.vy *= -1
                poeng += 1
                counter += 1
                  


        if counter == 5:
            ball.v = ball.v * 1.5
            spiller.size = spiller.size * 0.8
            counter = 0
            
        # Poeng
        tekst = poeng_font.render(str(poeng), True, "white")
        tekst_rect = tekst.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
        screen.blit(tekst, tekst_rect)

        

    
    # Oppdaterer hele skjermen 

    pygame.display.flip() 

    # Forsikrer at spillet kjører i maksimalt 60 FPS. 

    clock.tick(60) 

# Avslutter spillet 

pygame.quit() 