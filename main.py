import numpy as np
from PIL import Image
import pygame

def matrix_to_chars(matrix, chars):
   
    """
    Converte uma matriz de valores de brilho em uma matriz de caracteres, usando uma lista de caracteres.

    Parâmetros:
    - matrix (list): Matriz de valores de brilho (inteiros de 0 a 255).
    - chars (list): Lista de caracteres a serem usados para mapear os valores de brilho.

    Retorno:
    - char_matrix (list): Matriz de caracteres correspondentes aos valores de brilho da matriz de entrada.
    """
   
    # Calcula o intervalo de brilho de cada caractere
    interval = 256 // len(chars)

    # Mapeia a matriz de brilho para uma matriz de caracteres
    char_matrix = []
    for row in matrix:
        char_row = []
        for brightness in row:
            # Calcula o índice do caractere correspondente ao brilho
            char_index = brightness // interval
            if char_index > 9:
                char_index = 9
            if char_index < 0:
                char_index = 0
            # Adiciona o caractere correspondente à linha de caracteres
            char_row.append(chars[char_index])
        # Adiciona a linha de caracteres à matriz de caracteres
        char_matrix.append(char_row)

    return char_matrix


# Define a lista de caracteres a serem usados
chars = [' ', '.', '-', '_', '+', '*', '^', 's', 'X', '@']

# Carrega a imagem e converte para escala de cinza
image = Image.open('imagem.jpg').convert('L')

# Redimensiona a imagem para um tamanho menor
image = image.resize((80, 80))

# Converte a imagem para uma matriz NumPy
matrix = np.array(image)

# Converte a matriz de valores de brilho em uma matriz de caracteres
char_matrix = matrix_to_chars(matrix, chars)

# Imprime a matriz de caracteres
"""
for row in char_matrix:
    print(''.join(row))
"""

# Define as dimensões da tela
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 700

# Define o tamanho de cada caractere (pixel)
CHAR_WIDTH = 9
CHAR_HEIGHT = 9

# Inicializa o Pygame
pygame.init()

# Cria a janela principal
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Define a fonte a ser usada
font = pygame.font.SysFont('Arial', CHAR_HEIGHT)

# Loop principal
while True:
    # Processa os eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Define a posição inicial na tela
    x = 0
    y = 0

    # Percorre a matriz de caracteres e desenha cada caractere na tela
    for row in char_matrix:
        for char in row:
            # Renderiza o caractere com a fonte definida
            char_surf = font.render(char, True, (255, 255, 255))
            # Desenha o caractere na posição atual na tela
            screen.blit(char_surf, (x, y))
            # Atualiza a posição na tela para o próximo caractere
            x += CHAR_WIDTH
        # Atualiza a posição na tela para a próxima linha de caracteres
        x = 0
        y += CHAR_HEIGHT

    # Atualiza a tela
    pygame.display.update()
