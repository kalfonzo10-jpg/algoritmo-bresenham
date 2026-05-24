import pygame
import sys

pygame.init()

# tamaño de la ventana
ancho = 600
alto = 600

pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Circulo Bresenham")

# colores
blanco = (255, 255, 255)
gris = (180, 180, 180)
rojo = (255, 0, 0)

# tamaño de cada cuadro
tam = 20

# funcion para hacer la cuadricula
def cuadricula():

    for x in range(0, ancho, tam):
        pygame.draw.line(pantalla, gris, (x, 0), (x, alto))

    for y in range(0, alto, tam):
        pygame.draw.line(pantalla, gris, (0, y), (ancho, y))

# funcion para dibujar un pixel
def pixel(x, y):

    pygame.draw.rect(
        pantalla,
        rojo,
        (x * tam, y * tam, tam, tam)
    )

# algoritmo de bresenham
def circulo(xc, yc, r):

    x = 0
    y = r

    d = 3 - 2 * r

    while x <= y:

        # puntos del circulo
        pixel(xc + x, yc + y)
        pixel(xc - x, yc + y)
        pixel(xc + x, yc - y)
        pixel(xc - x, yc - y)

        pixel(xc + y, yc + x)
        pixel(xc - y, yc + x)
        pixel(xc + y, yc - x)
        pixel(xc - y, yc - x)

        # decision
        if d < 0:
            d = d + 4 * x + 6
        else:
            d = d + 4 * (x - y) + 10
            y -= 1

        x += 1

# bucle principal
ejecutando = True

while ejecutando:

    pantalla.fill(blanco)

    cuadricula()

    # centro y radio
    circulo(15, 15, 10)

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            ejecutando = False

    pygame.display.update()

pygame.quit()
sys.exit()