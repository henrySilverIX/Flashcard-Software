from tkinter import *

import pandas as pd
import random
import sys
import os




BACKGROUND_COLOR = "#B1DDC6"
FONT_FAMILY = "Ariel"

# Função para encontrar arquivos corretamente
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    if getattr(sys, 'frozen', False):
        # Executável
        return os.path.join(sys._MEIPASS, relative_path)
    else:
        # Script normal
        return os.path.join(os.path.abspath("."), relative_path)

current_card = {}
language_dict = {}

#Criação do DataFrame
try:
    language_dict_path = resource_path("data/words_to_learn.csv")
    language_dictionary_df = pd.read_csv(language_dict_path)
except FileNotFoundError:
    language_dict_path = resource_path("data/french_words.csv")
    original_data = pd.read_csv(language_dict_path)
    language_dict = original_data.to_dict(orient="records")
else:
    language_dict = language_dictionary_df.to_dict(orient="records")



def show_backwards():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)



def show_new_word():
    global flip_timer, current_card
    current_card = random.choice(language_dict)
    window.after_cancel(flip_timer)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer= window.after(3000, func=show_backwards)


def known_words():
    language_dict.remove(current_card)
    updated_dictionary = pd.DataFrame(language_dict)
    updated_dictionary.to_csv("data/words_to_learn.csv", index=False)
    show_new_word()


# Configuração a tela
window = Tk()
window.title("Mnemosyne")
window.minsize(width=900, height=600)
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=show_backwards)

# Configuração da tela do flashcard - Tela frontal
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file=resource_path("images/card_front.png"))
card_back_img = PhotoImage(file=resource_path("images/card_back.png"))
card_background = canvas.create_image(400, 263, image=card_front_img)

card_title = canvas.create_text(400, 150, text="", font=(FONT_FAMILY, 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=(FONT_FAMILY, 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)


#Buttons
right_icon = PhotoImage(file=resource_path("images/right.png"))
right_button = Button(image=right_icon, highlightthickness=0, bg=BACKGROUND_COLOR, command=known_words)
right_button.grid(row=1, column=1)

wrong_icon = PhotoImage(file=resource_path("images/wrong.png"))
wrong_button = Button(image=wrong_icon, highlightthickness=0, background=BACKGROUND_COLOR, command=show_new_word)
wrong_button.grid(row=1, column=0)



show_new_word()


window.mainloop()