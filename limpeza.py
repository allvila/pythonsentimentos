import pandas as pd
import re

# Lê o arquivo que você coletou
df = pd.read_csv("resultados.csv")

def limpar_texto(texto):
    if not isinstance(texto, str):
        return ""
    texto = re.sub(r"http\S+", "", texto)         # remove links
    texto = re.sub(r"[@#]\w+", "", texto)         # remove hashtags e menções
    texto = re.sub(r"[^a-zA-ZÀ-ÿ\s]", "", texto)  # remove caracteres especiais/números
    return texto.strip()

# Aplica a limpeza em cada comentário
df["texto_do_comentario"] = df["texto_do_comentario"].apply(limpar_texto)

# Salva um novo arquivo limpo
df.to_csv("resultados_limpos.csv", index=False, encoding="utf-8")

print("✅ Textos limpos e salvos em resultados_limpos.csv")
