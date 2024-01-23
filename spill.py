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
        self.color = "Black"
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
    def __init__(self, start_x, start_y, start_vx, start_vy):
        super().__init__(start_x, start_y)
        self.x = start_x
        self.y = start_y
        self.a = 0.2
        

pygame.init() 

screen = pygame.display.set_mode((700, 500)) # Setter skjermen til 500x500 piksler. 
clock = pygame.time.Clock() 
running = True 
# Initialiserer objekter 

while running: 
 # Avslutter løkken 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 
# Fyller skjermen med hvit farge 
screen.fill("white") 

# Tegner og oppdaterer spiller 


# Tegne og oppdatere fiender 

# Kollisjon 

# Oppdaterer hele skjermen 

pygame.display.flip() 

# Forsikrer at spillet kjører i maksimalt 60 FPS. 

clock.tick(60) 

# Avslutter spillet 

pygame.quit() 