from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Abre o navegador
navegador = webdriver.Chrome()

# Acesse um perfil do Twitter/X (exemplo: CNN Brasil)
navegador.get("https://x.com/CNNBrasil")
time.sleep(5)  # espera a página carregar

# Rola a página algumas vezes para carregar mais posts
for _ in range(3):
    navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

# Coletar posts (limitado a 30 para este trabalho)
posts = navegador.find_elements(By.TAG_NAME, "article")[:30]

dados = []
for i, post in enumerate(posts):
    try:
        comentario = post.text
        dados.append([i+1, "@CNNBrasil", "texto da postagem", comentario])
    except:
        continue

# Salvar em CSV
df = pd.DataFrame(dados, columns=["codigo_da_postagem", "nome_portal", "texto_da_postagem", "texto_do_comentario"])
df.to_csv("resultados.csv", index=False, encoding="utf-8")

print("✅ Dados salvos em resultados.csv")

navegador.quit()

