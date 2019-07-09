class User(pygame.sprite.Sprite):
    """ Esta clase representa la barra de la parte inferior que controla el protagonista. """
     
    def __init__(self):
        """ Constructor para Protagonista. """
        # Llama al constructor padre
        super().__init__()
         
        self.largo = 75
        self.alto = 15
        self.image = pygame.Surface([self.largo, self.alto])
        self.image.fill((BLANCO))
         
        # Hacemos que la esquina superior izquierda se la ubicación a pasar.
        self.rect = self.image.get_rect()
        self.alto_pantalla = pygame.display.get_surface().get_height()
        self.largo_pantalla = pygame.display.get_surface().get_width()
 
        self.rect.x = 0
        self.rect.y = self.alto_pantalla-self.alto
     
    def update(self):
        """ Actualiza la posición del protagonista. """
        # Obtenemos la posición del ratón
        pos = pygame.mouse.get_pos()
        # Sitúa la barra del lado izquierdo del jugador en la posición del ratón
        self.rect.x = pos[0]
        # Asegúrate de que no empujamos la pala del protagonista 
        # por fuera del borde derecho de la pantalla 
        if self.rect.x > self.largo_pantalla - self.largo:
            self.rect.x = self.largo_pantalla - self.largo
