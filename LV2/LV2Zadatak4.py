import numpy as np
import matplotlib.pyplot as plt

def generate_checkerboard(square_size, num_squares_height, num_squares_width):
    # Kreiranje crnog i bijelog kvadrata
    black_square = np.zeros((square_size, square_size))
    white_square = np.ones((square_size, square_size)) * 255  # 255 predstavlja maksimalnu vrijednost za grayscale sliku

    # Složiti crno-bijele kvadrate u redove
    rows = []
    for i in range(num_squares_width):
        if i % 2 == 0:  # Ako je paran red, počni s crnim kvadratom
            rows.append(black_square)
        else:  # Inače počni s bijelim kvadratom
            rows.append(white_square)
    
    # Složiti redove u sliku
    img_rows = []
    for i in range(num_squares_height):
        if i % 2 == 0:  # Ako je paran red, počni s prvom vrstom (crnim kvadratom)
            img_rows.append(np.hstack(rows))
        else:  # Inače počni s drugom vrstom (bijelim kvadratom)
            img_rows.append(np.hstack([white_square] + rows[:-1]))  # Dodajemo bijeli kvadrat na početak drugog retka

    # Složiti sve retke u sliku
    checkerboard = np.vstack(img_rows)

    return checkerboard

# Testiranje funkcije
square_size = 50
num_squares_height = 5
num_squares_width = 5

checkerboard_img = generate_checkerboard(square_size, num_squares_height, num_squares_width)

# Prikaz rezultata
plt.imshow(checkerboard_img, cmap='gray', vmin=0, vmax=255)
plt.axis([0, 250, 190, 0])  # Isključivanje oznaka osi
plt.show()
