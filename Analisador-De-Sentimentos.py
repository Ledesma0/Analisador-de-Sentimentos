""" 
Introdução a Engenharia de Software. Profº Drº Daniela Bagatini.
Analisador De Sentimentos realizado como projeto para o 1º semestre de Engenharia de Software.
O programa tem como objetivo analisar frases e textos e identificar se são NEGATIVAS, NEUTRAS ou POSITIVAS.

Autores: 
Erica Moraes Balinhas
Leonardo Ledesma dos Santos
Leonardo Silva Nobre dos Santos
Lúcio Eduardo Bueno Abreu Viana
Bernardo Machado Soares
"""

#_____ INFORMAÇÕES _____#

# Linhas Para formatação 
LINHAS_FORMATACAO = 100
LINHAS_FORMATACAO_DUPLA = 50

# Listas das Palavras

palavras_positivas = [
    "feliz", "alegre", "ótimo", "excelente", "maravilhoso", "bom", "amor",
    "adorar", "incrível", "fantástico", "perfeito", "legal", "bacana",
    "sucesso", "vitória", "paz", "amizade", "sorrir", "esperança", "lindo",
    "bonito", "agradável", "divertido", "animado", "satisfeito", "grato",
]

palavras_negativas = [
    "triste", "ruim", "péssimo", "horrível", "terrível", "ódio", "odiar",
    "chorar", "fracasso", "derrota", "medo", "raiva", "feio", "chato",
    "desagradável", "entediado", "frustrado", "decepcionado", "cansado",
    "preocupado", "ansioso", "difícil", "problema", "mal", "infeliz"
]

###############################################################################################################################################################################################################
""" A Função Limpadora Serve para remover pontuações e converter tudo para minúsculas.
EX: 
Entrada: Olá, MUNDOOOOO
A função retorna: olá mundooooo
"""
# Parte 1 - Função Limpadora

def limpar_texto(texto):

    # Listas de pontuações que serão removidas:
    pontuacoes = ".,!?;:()-\"'…"
    
    # Convertendo texto para minúsculas:
    texto_limpo = texto.lower()

    # Removendo as pontuações do texto:
    for pontuacao in pontuacoes:
        texto_limpo = texto_limpo.replace(pontuacao, "")

    return texto_limpo

###############################################################################################################################################################################################################