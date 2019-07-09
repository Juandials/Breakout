class Pelota(pygame.sprite.Sprite):
    """ Esta clase representa la pelota       
        Deriva de la clase "Sprite" en Pygame """
     
    # Velocidad en píxeles por ciclo
    velocidad = 10.0
     
    # Representación en coma flotante de la ubicación de la pelota
    x = 0.0
    y = 180.0
     
    # Rumbo de la pelota (en grados)
    rumbo = 200
 
    largo = 10
    alto = 10
     
    # Constructor. Pasa el color del bloque así como su posición x e y
    def __init__(self):
        # Llama al constructor de la clase padre (Sprite)
        super().__init__()
         
        # Crea la imagen de la pelota
        self.image = pygame.Surface([self.largo, self.alto])
         
        # Color de la pelota
        self.image.fill(BLANCO)
         
        # Obtiene un objeto rectángulo que muestra dónde se encuentra nuestra imagen
        self.rect = self.image.get_rect()
         
        # Obtiene los atributos para alto/largo de la pantalla
        self.alto_pantalla = pygame.display.get_surface().get_height()
        self.largo_pantalla = pygame.display.get_surface().get_width()
     
    def botar(self, diff):
        """ Está función hará botar la pelota 
            desde una superficie horizontal (no de una vertical) """
         
        self.rumbo = (180 - self.rumbo) % 360
        self.rumbo -= diff
     
    def update(self):
        """ Actualiza la posición de la pelota. """
        # Seno y Coseno trabajan con grados, por eso debemos convertirlos a radianes
        rumbo_radianes = math.radians(self.rumbo)
         
        # Cambia la posición (x e y) según la velocidad y el rumbo
        self.x += self.velocidad * math.sin(rumbo_radianes)
        self.y -= self.velocidad * math.cos(rumbo_radianes)
         
        # Mueve la imagen hacia las coordenadas x e y
        self.rect.x = self.x
        self.rect.y = self.y
         
        # ¿Hemos botado por fuera del borde superior de la pantalla?
        if self.y <= 0:
            self.botar(0)
            self.y = 1
             
        # ¿Hemos botado por fuera de la izquierda de la pantalla?
        if self.x <= 0:
            self.rumbo = (360 - self.rumbo) % 360
            self.x = 1
             
        # ¿Hemos botado por fuera de la derecha de la pantalla?
        if self.x > self.largo_pantalla - self.largo:
            self.rumbo = (360 - self.rumbo) % 360
            self.x = self.largo_pantalla - self.largo - 1
         
        # ¿Hemos botado por fuera del borde inferior de la pantalla?
        if self.y > 600:
            return True
        else:
            return False
