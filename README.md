# Sumarizador-Sumy

✅ Instalando Sumy (com pip):
No terminal (ou no Prompt de Comando do Windows / Anaconda Prompt), execute:

    pip install sumy
🔄 Se quiser garantir que o idioma português funcione bem, também recomendo instalar o pacote nltk e baixar os recursos de tokenização do idioma:

    pip install nltk

Depois, dentro de um terminal Python ou script, execute:

          import nltk
          nltk.download('punkt')  # Necessário para dividir o texto em frases
