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

#Criação do DataFrame
language_dict_path = resource_path("data/french_words.csv")
language_dictionary_df = pd.read_csv(language_dict_path)
language_dict = language_dictionary_df.to_dict(orient="records")





def show_backwards():
    random_goal_word = random.randint(0, 100)

    # Configuração da tela do flashcard - Tela de trás
    back_flashcard = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
    card_back = PhotoImage(file=resource_path("images/card_back.png"))
    back_flashcard.create_image(400, 263, image=card_back)


    back_flashcard.create_text(400, 150, text="English", font=(FONT_FAMILY, 40, "italic"))
    back_flashcard.create_text(400, 263, text=language_dict[random_goal_word]["English"], font=(FONT_FAMILY, 60, "bold"))
    back_flashcard.grid(row=0, column=0, columnspan=2)


def show_new_word():
    random_goal_word = random.randint(0, 100)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=language_dict[random_goal_word]["French"])






# Configuração a tela
window = Tk()
window.title("Mnemosyne")
window.minsize(width=900, height=600)
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)




# Configuração da tela do flashcard - Tela frontal
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file=resource_path("images/card_front.png"))
canvas.create_image(400, 263, image=card_front)

card_title = canvas.create_text(400, 150, text="", font=(FONT_FAMILY, 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=(FONT_FAMILY, 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)


#Buttons
right_icon = PhotoImage(file=resource_path("images/right.png"))
right_button = Button(image=right_icon, highlightthickness=0, bg=BACKGROUND_COLOR, command=show_new_word)
right_button.grid(row=1, column=1)

wrong_icon = PhotoImage(file=resource_path("images/wrong.png"))
wrong_button = Button(image=wrong_icon, highlightthickness=0, background=BACKGROUND_COLOR, command=show_new_word)
wrong_button.grid(row=1, column=0)



show_new_word()


window.mainloop()