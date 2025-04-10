# Sumarizador-Sumy

 Instalando Sumy (com pip):
No terminal (ou no Prompt de Comando do Windows / Anaconda Prompt), execute:

    pip install sumy
 Se quiser garantir que o idioma português funcione bem, também recomendo instalar o pacote nltk e baixar os recursos de tokenização do idioma:

    pip install nltk

Depois, dentro de um terminal Python ou script, execute:

          import nltk
          nltk.download('punkt')  # Necessário para dividir o texto em frases

Execução:

Deve escolher qual das técnicas de sumarizaçao vai usar. Para isso deve descomentar qual deseja.

        import os
        from sumy.parsers.plaintext import PlaintextParser
        from sumy.nlp.tokenizers import Tokenizer
        # # TextRank (baseado em grafos, tipo PageRank)
        from sumy.summarizers.text_rank import TextRankSummarizer as Summarizer
        # # LexRank (também baseado em grafos, usa TF-IDF)
        # from sumy.summarizers.lex_rank import LexRankSummarizer as Summarizer
        #from sumy.summarizers.lsa import LsaSummarizer as Summarizer
        # # Luhn (baseado em frequência de palavras e posição)
        # from sumy.summarizers.luhn import LuhnSummarizer as Summarizer
        # # Edmundson (requer configuração de palavras chave boas e ruins)
        # from sumy.summarizers.edmundson import EdmundsonSummarizer as Summarizer
        # # KL-Sum (minimiza divergência de informação - KL Divergence)
        # from sumy.summarizers.kl import KLSummarizer as Summarizer

O sumarizador Edmundson não está disponivel nesse codigo


Para executar o codigo voce deve ajustar os terminais de imput e output:
                    
    # Caminhos para as pastas de entrada e saída
   
