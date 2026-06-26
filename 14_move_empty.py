# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""_summary_
Vytvořte jednoduchou terminálovou aplikaci, která umožní hráči ovládat pohybující se 
kostičku (O) po hrací ploše. Cílem je sebrat co nejvíce hvězdiček (*) umístěných 
na hrací ploše.

Zadání úlohy
Vaším úkolem je vytvořit program, který:
Zobrazí hrací plochu (mřížka) o rozměrech 20x10 (šířka x výška) v terminálu.

Na této ploše bude:
Hráč reprezentovaný symbolem O, který se pohybuje pomocí kláves:
W pro pohyb nahoru.
S pro pohyb dolů.
A pro pohyb doleva.
D pro pohyb doprava.
Hvězdička (*), která se náhodně umístí na volné políčko hrací plochy.
Hráč začne na výchozí pozici (5, 5). Pohyb je omezen hranicemi plochy. 
Hráč se nemůže dostat mimo hrací plochu.

Pokud hráč dojde k hvězdičce (*), jeho skóre se zvýší o 1 
a hvězdička se přemístí na nové náhodné volné políčko.
Hrací plocha se bude v reálném čase aktualizovat, 
aby bylo vidět aktuální pozici hráče i hvězdičky.

Hra bude pokračovat neomezeně dlouho, dokud ji hráč 
manuálně neukončí (např. stiskem Ctrl+C).

* doplňte okraje herní plochy
* doplňte počítadlo pohybu hráče
* barevné kreace


"""

import os
import random
import time
import keyboard
import tkinter as tk

##############################################################
# Globální proměnné

BOARD_WIDTH = 20  # Šířka hrací plochy
BOARD_HEIGHT = 10  # Výška hrací plochy
PLAYER_SYMBOL = "O"
FOOD_SYMBOL = "X"
EMPTY_SYMBOL = "."
PLAYER_POS = (5, 5)  # Výchozí pozice hráče
FOOD_POS = (7, 7)  # Výchozí pozice hvězdičky
SCORE = 0
DELAY = 0.1
GAME_OVER = False


##############################################################
def render_board(width: int, height: int, snake_pos: tuple[int, int], food_pos: tuple[int, int]) -> None:
    """Vykresli herni desku pro hada."""
    for y in range(height):
        radek = ""

        for x in range(width):
            # 1) Okraje: první/poslední sloupec (x) nebo první/poslední řádek (y)
            if x == 0 or x == width - 1 or y == 0 or y == height - 1:
                radek += "#"
            
            # 2) Jídlo (O) na své specifické pozici
            elif (x, y) == food_pos:
                radek += "O"
            
            # 3) Had (X) na své specifické pozici
            elif (x, y) == snake_pos:
                radek += "X"
            
            # 4) Všechna ostatní políčka uvnitř budou tečky
            else:
                radek += "."

        print(radek)

##############################################################
import os
import random

# Globální nastavení hry
width = 20
height = 10
game_over = False

# Počáteční pozice (had začíná uprostřed, jídlo na náhodném místě)
snake_pos = (10, 5)
direction = "d"  # Výchozí směr doprava

def place_food() -> tuple[int, int]:
    """Vygeneruje náhodnou pozici jídla mimo okraje."""
    food_x = random.randint(1, width - 2)
    food_y = random.randint(1, height - 2)
    return (food_x, food_y)

food_pos = place_food()

def pohni_hadem(current_pos: tuple[int, int], current_direction: str) -> tuple[int, int]:
    """Vrátí novou pozici hada podle zadaného směru (o 1 políčko v mřížce)."""
    x, y = current_pos

    if current_direction == "w":
        return (x, y - 1)  # Nahoru
    elif current_direction == "s":
        return (x, y + 1)  # Dolů
    elif current_direction == "a":
        return (x - 1, y)  # Doleva
    elif current_direction == "d":
        return (x + 1, y)  # Doprava
    else:
        return current_pos

def kontrola_kolize(x: int, y: int, max_width: int, max_height: int) -> bool:
    """Zkontroluje, zda hlava hada nenarazila do zdi okraje."""
    if x <= 0 or x >= max_width - 1 or y <= 0 or y >= max_height - 1:
        print("Konec hry - náraz do zdi!")
        return True
    return False

def render_board(max_width: int, max_height: int, s_pos: tuple[int, int], f_pos: tuple[int, int]) -> None:
    """Vykreslí herní desku s okraji (#), hadem (X), jídlem (O) a prázdnem (.)."""
    if not game_over:
        root.after(200, game_step)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    for y in range(max_height):
        radek = ""
        for x in range(max_width):
            if x == 0 or x == max_width - 1 or y == 0 or y == max_height - 1:
                radek += "#"
            elif (x, y) == f_pos:
                radek += "O"
            elif (x, y) == s_pos:
                radek += "X"
            else:
                radek += "."
        print(radek)

def game_step():
    global game_over, snake_pos, food_pos

    if game_over:
        return

    nova_pozice = pohni_hadem(snake_pos, direction)
    x, y = nova_pozice

    if kontrola_kolize(x, y, width, height):
        game_over = True
        return

    snake_pos = nova_pozice

    if snake_pos == food_pos:
        food_pos = place_food()

    render_board(width, height, snake_pos, food_pos)


##############################################################
### Spuštění programu - MAIN
def on_key(event):
    global direction

    if event.keysym == "Up":
        direction = "w"
    elif event.keysym == "Down":
        direction = "s"
    elif event.keysym == "Left":
        direction = "a"
    elif event.keysym == "Right":
        direction = "d"
root = tk.Tk()
root.bind("<KeyPress>", on_key)
root.after(200, game_step)
root.mainloop()
if __name__ == "__main__":
    print("Použijte klávesy w, a, s, d pro pohyb. Stiskněte Ctrl+C pro ukončení.")

    width = 20
    height = 10
    direction = "d"
    snake_pos = (5, 5)
    game_over = False
    food_pos = place_food()

    try:
        render_board(width, height, snake_pos, food_pos)

        if not game_over:
            root.after(200, game_step)
        print("\nHra skončila!")

    except KeyboardInterrupt:
        print("\nHra ukončena uživatelem.")