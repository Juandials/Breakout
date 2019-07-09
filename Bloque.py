# -*- coding: cp1252 -*-
import math
import pygame
 
# Definimos algunos colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
 
# Tama�o de los bloques break-out
largo_bloque = 23
alto_bloque = 15
 
class Bloque(pygame.sprite.Sprite):
    """Esta clase representa a cada bloque que ser� golpeado por la pelota.
    Deriva de la clase "Sprite" en Pygame """
 
    def __init__(self, color, x, y):
        """ Constructor. Pasa el color del bloque y su 
            posici�n x, y. """
         
        # Llama al constructor de la clase padre (Sprite)
        super().__init__()
         
        # Crea una imagen del bloque de tama�o apropiado
        # El largo y alto son enviados como una lista al primer par�metro.
        self.image = pygame.Surface([largo_bloque, alto_bloque])
         
        # Rellenamos la imagen con el color apropiado
        self.image.fill(color)
         
        # Extraemos el objeto rect�ngulo que posee las dimensiones de la imagen
        self.rect = self.image.get_rect()
         
        # Movemos la esquina superior izquierda del rect�ngulo a las coordenadas x,y.
        # Aqu� es donde aparecer� nuestro bloque.
        self.rect.x = x
        self.rect.y = y
