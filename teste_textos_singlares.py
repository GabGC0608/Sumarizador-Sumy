import os
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
# # TextRank (baseado em grafos, tipo PageRank)
# from sumy.summarizers.text_rank import TextRankSummarizer as Summarizer
# # LexRank (também baseado em grafos, usa TF-IDF)
# from sumy.summarizers.lex_rank import LexRankSummarizer as Summarizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
# # Luhn (baseado em frequência de palavras e posição)
# from sumy.summarizers.luhn import LuhnSummarizer as Summarizer
# # Edmundson (requer configuração de palavras chave boas e ruins)
# from sumy.summarizers.edmundson import EdmundsonSummarizer as Summarizer
# # KL-Sum (minimiza divergência de informação - KL Divergence)
# from sumy.summarizers.kl import KLSummarizer as Summarizer


# Inicializa o resumidor
summarizer = Summarizer(aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa)

text = (""
)
# Cria o parser
parser = PlaintextParser.from_string(text, Tokenizer("portuguese"))

    # Calcula o número de palavras desejado no resumo (50%) 
total_words = len(text.split())
target_words = max(1, round(total_words * 0.1))  # Pelo menos 1 palavra
        
        # Gera o resumo com todas as sentenças primeiro
summary_sentences = summarizer(parser.document, len(parser.document.sentences))
        
        # Constrói o resumo até atingir o número de palavras desejado
summary_words = []
current_count = 0

#Corta a sentença caso ela ultrapasse o limite de palavras 
for sentence in summary_sentences:
        sentence_words = str(sentence).split()
        if current_count + len(sentence_words) > target_words:
                remaining = target_words - current_count
                if remaining > 0:
                    summary_words.extend(sentence_words[:remaining])
                break
        summary_words.extend(sentence_words)
        current_count += len(sentence_words)
        
summary_text = ' '.join(summary_words)    
   
print(f"Resumo ({len(summary_words)} palavras):\n{summary_text}")
