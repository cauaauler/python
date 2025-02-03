import pyautogui
import os
import time
import random
import nltk

# Baixa a lista de palavras do dicionário (só precisa rodar uma vez)
nltk.download("words")

from nltk.corpus import words

# Filtra apenas palavras em português (ou próximas)
palavras_reais = [palavra.lower() for palavra in words.words() if palavra.isalpha() and len(palavra) > 2]

# Abre o Microsoft Edge no Bing
os.system("start msedge https://www.bing.com/")
time.sleep(5)  # Espera o navegador carregar

x = 0
while x < 30:  # Executa 30 buscas
    time.sleep(3)  # Pequeno delay entre buscas

    # Escolhe uma palavra real aleatória
    palavra = random.choice(palavras_reais)

    # Seleciona a barra de pesquisa (atalho universal para maioria dos navegadores)
    pyautogui.hotkey('ctrl', 'l')  
    time.sleep(1)

    # Digita a palavra real e pressiona Enter
    pyautogui.write(palavra, interval=0.1)
    pyautogui.press("enter")

    x += 1  # Incrementa o contador
