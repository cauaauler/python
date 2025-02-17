import os
import time
import random
import nltk
import urllib.parse  # Import para converter espaços em %20

# Baixa o corpus Floresta do NLTK
nltk.download("floresta")

from nltk.corpus import floresta

# Obtém palavras únicas do corpus (removendo duplicatas)
palavras_portugues = list(set([word.lower() for word in floresta.words() if word.isalpha()]))

# Número de pesquisas
num_pesquisas = 30

for i in range(num_pesquisas):
    # Escolhe 3 palavras aleatórias
    palavra1 = random.choice(palavras_portugues)
    palavra2 = random.choice(palavras_portugues)
    palavra3 = random.choice(palavras_portugues)

    # Junta as palavras e codifica para URL (troca espaços por %20)
    termo_pesquisa = f"{palavra1} {palavra2} {palavra3}"
    termo_pesquisa_codificado = urllib.parse.quote(termo_pesquisa)

    # Comando ADB para abrir o navegador padrão com a pesquisa
    comando = f'adb shell am start -a android.intent.action.VIEW -d "https://www.bing.com/search?q={termo_pesquisa_codificado}"'

    # Executa o comando
    os.system(comando)
    
    print(f"[{i+1}/{num_pesquisas}] Pesquisa realizada no navegador padrão: {termo_pesquisa}")

    # Aguarda um tempo antes da próxima pesquisa (entre 3 e 5 segundos)
    time.sleep(random.randint(10))

print("✅ Todas as pesquisas foram concluídas com sucesso no navegador padrão!")
