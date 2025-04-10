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
summarizer = Summarizer()

text = ("life long learning sempre aprendendo com esses irmaos animada com a aprendizado uma sequencia de palavras que nem parecem ser no meu idioma "
        "ceus kkkkkk. essa imersao vai ser dificil. excelente descricao do que sao os notebooks. formalizacao do codigo jogado. gosto tambem da possibilidade "
        "de documentar e comunicar a solucao usando markdown. alura e legal mas e muito caro. a mensalidade fica dificil fazer. python parece ser o inicio de "
        "alguma coisa ate porque to estudando isso no primeiro semestre. dai a gente entra num video que so fala palavras dificeis. deus me ajudaaaa. quero essa camiseta. "
        "um video meio assustador pra quem nao entende de programacao. eles comecam a jogar monte de informacao que meros mortais nao entende sabe. poderia ser mais "
        "simplificado para quem quer entender o que e python. em relacao aos games e natural que o python sejam bem mais familiar a jogos de rpg e pluzzes. "
        "nao entendi porra nenhuma kkkkkk. man vcs estao no mesmo local pq a voz do guilherme esta tao ruim kssjsk. guilherme silveira e o professor mais brabo do alura. "
        "voces tem curso de python. saio sem entender o que e python a partir desse video. ja criei meu primeiro hello worldpy. valeu alura continuem assim ensinando e aprendendo. "
        "bom dia. feliz ano novo pra voces. entao eu queria muito entrar na area de programacao. poderia me ajudar por onde comecar cursos. vi esse anuncio de python e sera que "
        "eu poderia comecar por ele ou voces me indicam outro ponto inicial. anos e tentando uma transicao de carreira. sempre fui pessima em matematica e raciocinio logico "
        "mas estou tentando. tomara que eu consiga e tenha uma carreira a frente. deus abencoe a todos. ass monica. consigo invadir a nada com python. oi mi que legal saber que "
        "esta comecando a estudar phyton. temos um artigo que pode te ajudar. da uma olhada historia sintaxe e um guia para iniciar na linguagem. oi denise tudo bem. chama a gente "
        "na dm de alguma de nossas redes sociais que podemos verificar se podemos mandar algum mimo para."
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
