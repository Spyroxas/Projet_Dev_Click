import pygame


def DrawText(screen, text, text_color, x, y, fsize):
    font = pygame.font.Font('freesansbold.ttf', fsize)
    text = font.render(text, True, text_color)
    text_rect = text.get_rect()
    text_rect.center = (x, y)
    screen.blit(text, text_rect)

def display_base(dis_w, dis_h, image_path):
    pygame.display.set_mode((dis_w, dis_h))
    pygame.display.set_caption("Dev Clicker")
    screen = pygame.display.set_mode((dis_w, dis_h))
    background = pygame.image.load(image_path)
    background = pygame.transform.scale(background, (dis_w, dis_h))
    screen.blit(background, (0, 0))
    return screen

def display_button(screen, rect, image, width, height):
    background = pygame.image.load(image).convert_alpha()
    background = pygame.transform.scale(background, (width, height))
    screen.blit(background, rect)

def display_info_code(screen, code):
    DrawText(screen, str(f'{code:.1f}') + "%", "black", 100, 50, 20)

def display_info_stock_code(screen, stock_code):
    DrawText(screen, str(stock_code), "black", 100, 100, 20)

def display_info_money(screen, money):
    DrawText(screen, str(f'{money}') + "€", "white", 100, 150, 20)

def coord(coordonnee, max_coord):
    return (coordonnee / 100) * max_coord

def coord_button(coord_x, coord_y, size_x, size_y, largeur, hauteur):
    coord_x = (coord_x / 100) * largeur
    coord_y = (coord_y / 100) * hauteur
    size_x = (size_x / 100) * largeur
    size_y = (size_y / 100) * hauteur
    return coord_x, coord_y, size_x, size_y

def coord_size(size_x, size_y, largeur, hauteur):
    size_x = (size_x / 100) * largeur
    size_y = (size_y / 100) * hauteur
    return size_x, size_y

def rect_with_alpha(sc, rect, image, sx, sy, w, h):
    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    new_rect = pygame.draw.rect(shape_surf, (0, 0, 0, 255), rect)
    new_rect.update(rect)
    sc.blit(shape_surf, new_rect)
    coord = coord_size(sx, sy, w, h)
    display_button(sc, new_rect, image, coord[0], coord[1])
    return new_rect

