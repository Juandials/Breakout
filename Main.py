import pygame

#Llamamos a esta función para que la biblioteca Pygame pueda inicializarse.
pygame.init()
 
#Creamos una pantalla de 800x600
pantalla = pygame.display.set_mode([800, 600])
 
# Establecemos el título de la ventana
pygame.display.set_caption('Breakout')
 
# Haz esto para que el ratón desaparezca cuando se encuentre sobre nuestra ventana
pygame.mouse.set_visible(0)
 
# Esta es la fuente que usaremos para dibujar texto sobre pantalla (tamaño 36)
fuente = pygame.font.Font(None, 36)
 
# Creamos una superficie sobre la que podamos dibujar
fondo_pantalla = pygame.Surface(pantalla.get_size())
 
# Listas de todos los sprites
bloques = pygame.sprite.Group()
pelotas = pygame.sprite.Group()
todos_los_sprites = pygame.sprite.Group()
 
# Creamos el objeto pala del protagonista
protagonista = Protagonista()
todos_los_sprites.add(protagonista)
 
# Creamos las pelotas
pelota = Pelota()
todos_los_sprites.add(pelota)
pelotas.add(pelota)
 
# La parte superior del bloque (posición y)
top = 80
 
# Número de bloques a crear
numero_de_bloques = 32
 
# --- Creamos los bloques
 
# Cinco filas de bloques
for fila in range(5):
    # 32 columnas de bloques
    for columna in range(0, numero_de_bloques):
        # Crea un bloque (color,x,y)
        bloque = Bloque(AZUL, columna * (largo_bloque + 2) + 1, top)
        bloques.add(bloque)
        todos_los_sprites.add(bloque)
    # Mueve  hacia abajo el borde superior de la siguiente fila
    top += alto_bloque + 2
 
# Reloj para limitar la velocidad
reloj = pygame.time.Clock()
 
# ¿Se acabó el juego?
game_over = False
 
# ¿Salir del programa?
salir_programa = False
 
# Bucle principal
while not salir_programa:
 
    # Limitamos a 30 fps
    reloj.tick(30)
 
    # Limpiamos la pantalla
    pantalla.fill(NEGRO)
     
    # Procesamos los eventos en el juego
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            salir_programa = True
     
    # Mientras que el juego no acabe, actualizamos las posiciones del protagonista 
    # y las pelotas.
    if not game_over:
        #actualizamos las posiciones del protagonista y las pelotas.
        protagonista.update()
        game_over = pelota.update()
     
    # Si terminamos, imprimir game over
    if game_over:
        texto = fuente.render("Game Over", True, BLANCO)
        textopos = texto.get_rect(centerx=fondo_pantalla.get_width()/2)
        textopos.top = 300
        pantalla.blit(texto, textopos)
     
    # Observamos si las pelotas chocan contra la pala del protagonista.
    if pygame.sprite.spritecollide(protagonista, pelotas, False):
        # El 'diff' te permite intentar botar las pelotas hacia la izquierda o derecha 
        # dependiendo por que parte de la pala las golpees
        diff = (protagonista.rect.x + protagonista.largo/2) - (pelota.rect.x+pelota.largo/2)
         
        # Establece la posición 'y' de la pelota en caso la golpees 
        # con el borde la pala
        pelota.rect.y = pantalla.get_height() - protagonista.rect.alto - pelota.rect.alto - 1
        pelota.botar(diff)
     
    # Comprueba las colisiones entre las pelotas y los bloques
    bloquesmuertos = pygame.sprite.spritecollide(pelota, bloques, True)
     
    # Si le damos a un bloque, botamos las pelotas
    if len(bloquesmuertos) > 0:
        pelota.botar(0)
         
        # El juego se termina si todos los bloques desaparecen.
        if len(bloques) == 0:
            game_over = True
     
    # Dibujamos Todo
    todos_los_sprites.draw(pantalla)
 
    # Actualizamos la pantalla para mostrar todo lo dibujado
    pygame.display.flip()
 
pygame.quit()
