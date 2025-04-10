import os
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
# # TextRank (baseado em grafos, tipo PageRank)
# from sumy.summarizers.text_rank import TextRankSummarizer as Summarizer
# # LexRank (também baseado em grafos, usa TF-IDF)
# from sumy.summarizers.lex_rank import LexRankSummarizer as Summarizer
# from sumy.summarizers.lsa import LsaSummarizer as Summarizer
# # Luhn (baseado em frequência de palavras e posição)
# from sumy.summarizers.luhn import LuhnSummarizer as Summarizer
# # Edmundson (requer configuração de palavras chave boas e ruins)
# from sumy.summarizers.edmundson import EdmundsonSummarizer as Summarizer
# # KL-Sum (minimiza divergência de informação - KL Divergence)
# from sumy.summarizers.kl import KLSummarizer as Summarizer


# Caminhos para as pastas de entrada e saída
input_folder = 'Diretório com os textos'
output_folder = 'Diretório para salvar'
os.makedirs(output_folder, exist_ok=True)

# Inicializa o resumidor
summarizer = Summarizer()

for index, filename in enumerate(os.listdir(input_folder), start=1):
    if filename.endswith('.txt'):
        # Lê o arquivo
        try:
            with open(os.path.join(input_folder, filename), 'r', encoding='utf-8') as file:
                text = file.read().strip()
        except UnicodeDecodeError:
            with open(os.path.join(input_folder, filename), 'r', encoding='latin-1') as file:
                text = file.read().strip()
        
        # Verifica se o texto não está vazio
        if not text:
            print(f"Arquivo vazio: {filename}")
            continue
            
        # Cria o parser
        try:
            parser = PlaintextParser.from_string(text, Tokenizer("portuguese"))
        except:
            print(f"Erro ao processar: {filename}")
            continue

        # Calcula o número de palavras desejado no resumo (50%)
        total_words = len(text.split())
        target_words = max(1, round(total_words * 0.1))  # Pelo menos 1 palavra
        
        # Gera o resumo com todas as sentenças primeiro
        summary_sentences = summarizer(parser.document, len(parser.document.sentences))
        
        # Constrói o resumo até atingir o número de palavras desejado
        summary_words = []
        current_count = 0
        
        for sentence in summary_sentences:
            sentence_words = str(sentence).split()
            if current_count + len(sentence_words) > target_words:
                summary_words.extend(sentence_words) 
                break
                
            summary_words.extend(sentence_words)
            current_count += len(sentence_words)
        
        summary_text = ' '.join(summary_words)
        
        # Verifica o resultado
        summary_word_count = len(summary_words)
        
        print(f"Arquivo: {filename}")
        print(f"Total de palavras: {total_words} | Palavras no resumo: {summary_word_count}")
        print(f"Taxa de compressão: {summary_word_count/total_words:.1%}\n")
        
        # Salva o resumo
        output_filename = f"sumy_50_0{index}.txt"
        with open(os.path.join(output_folder, output_filename), 'w', encoding='utf-8') as f:
            f.write(summary_text.strip())

print("Processo concluído!")