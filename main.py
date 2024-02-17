# IMPORTING MODULES
import pygame

# INITIALIZE THE IMPORTED MODULES
pygame.init()

# VARIABLES
WIDTH, HEIGHT = 700, 500
fps = 500
timer = pygame.time.Clock()
running = True
active_size = 0
active_color = 'white'
painting = []

#SETTING THE SCREEN
screen = pygame.display.set_mode((WIDTH, HEIGHT))


# TITLE
pygame.display.set_caption('Draw!')


# SET UP THE MENU FUNCTION
def draw_menu(size, color):
    # ADDING A MENU FOR THE TOOLS
    pygame.draw.rect(screen, 'gray', [0, 0, WIDTH, 70])
    # MAKING A LINE THAT IS BETWEEN
    # THE MENU AND CANVAS
    pygame.draw.line(screen, 'black', (0, 70), (WIDTH, 70), 1)
    
    # SIZES OF THE BRUSHES
    # EXTRA LARGE BRUSH
    xl_brush = pygame.draw.rect(screen, 'black', [10, 10, 50, 50])
    pygame.draw.circle(screen, 'white', (35, 35), 20)

    # LARGE BUSH
    l_brush = pygame.draw.rect(screen, 'black', [70, 10, 50, 50])
    pygame.draw.circle(screen, 'white', (95, 35), 15)

    # MEDIUM BRUSH
    m_brush = pygame.draw.rect(screen, 'black', [130, 10, 50, 50])
    pygame.draw.circle(screen, 'white', (155, 35), 10)

    # SMALL BRUSH
    s_brush = pygame.draw.rect(screen, 'black', [190, 10, 50, 50])
