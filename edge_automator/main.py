import pyautogui
import os
import time
import random
import nltk

# Baixa o corpus Floresta
nltk.download("floresta")

from nltk.corpus import floresta

# Obtém palavras únicas do corpus (remoção de duplicatas)
palavras_portugues = list(set([word.lower() for word in floresta.words() if word.isalpha()]))

# Abre o Microsoft Edge no Bing
os.system("start msedge https://www.bing.com/")
time.sleep(5)

for _ in range(30):
    time.sleep(3)

    palavra = random.choice(palavras_portugues)
    palavra2 = random.choice(palavras_portugues)
    palavra3 = random.choice(palavras_portugues)

    pyautogui.hotkey('ctrl', 'l')  
    time.sleep(1)

    pyautogui.write(palavra + " " + palavra2 + " " + palavra3, interval=0.1)
    pyautogui.press("enter")
