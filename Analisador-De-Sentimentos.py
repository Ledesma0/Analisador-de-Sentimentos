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
""" 
A Função Limpadora Serve para remover pontuações e converter tudo para minúsculas.
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
"""
A Função Analisadora de Sentimentos compara o texto do usuário com as listas de palavras postivas e negativas.
Ela utiliza dois contadores para reconhecer a quantidade de palavras negativas e/ou positivas e assim definir se o texto é positivo ou negtivo.
"""

# Parte 2 - Função Analisadora de Sentimentos

def analisar_sentimentos(frase):
    
    # Chama função anterior para realizar o tratamento:
    frase_limpa = limpar_texto(frase)

    # Separando o texto em palavras para comparação:
    palavras = frase_limpa.split()

    # Contadores de palavras:
    contador_negativo = 0
    contador_positivo = 0

    # Listas para Guardar as palavras que foram encontradas:
    palavras_positivas_encontradas = []
    palavras_negativas_encontradas = []

    # Verificando cada palavra no texto:

    # Verificando palavras Positivas:
    for palavra in palavras: # Estrutura de repetição para verificar todas as palavras do texto inserido pelo usuário.
        if palavra in palavras_positivas: # Procura palavras positivas no texto separado.
            contador_positivo += 1 # Adiciona 1 ao contador das palavras positivas
            palavras_positivas_encontradas.append(palavra) # Adiiona a palavra positiva encontrada na lista de palavras positivas encontradas.
        
        # Verificando palavras Negativas:
        elif palavra in palavras_negativas: # Procura palavras negativas no texto separado.
            contador_negativo += 1 # Adiciona 1 ao contador ded palavras negativas
            palavras_negativas_encontradas.append(palavra) # Adiciona a palavra negativa encontrada na lista de palavras negativas encontradas.

    return contador_negativo, contador_positivo, palavras_negativas_encontradas, palavras_positivas_encontradas

###############################################################################################################################################################################################################
"""
A Função adicionar serve para o usuário adicione novas palavras nas listas.
"""
# Parte 3 - Função para adicionar novas palavras.

def adicionar_palavras():
    print("\n" + "=" * LINHAS_FORMATACAO)
    print("ADICIONAR NOVA PALAVRA")

    # Mensagem para usuário digitar a nova palavra:
    nova_palavra = input("Digite a nova palavra: ").strip().lower()

    # Verifica e informa se a nova palavra já não está na lista de palavras positivas:
    if nova_palavra in palavras_positivas:
        print(f"👍  A palavra '{nova_palavra}' já está na Lista de POSITIVAS!")
        return
    
    # Verifica e informa se a nova palavra já não está na lista de palavras negativas:
    elif nova_palavra in palavras_negativas:
        print(f"👎  A palavra '{nova_palavra}' já está na Lista de NEGATIVAS!")
        return
    
    # Informar se a nova palavra é Negativa ou Positiva:
    print("\nEsta palavra é: ")
    print("1️⃣ Positiva")
    print("2️⃣ Negativa")

    escolha = input("Digite sua escolha: ")

    match escolha:
        case "1":
            palavras_positivas.append(nova_palavra) # Adiciona a palavra na lista de palavras positivas.
            print(f"A palavra {nova_palavra} foi adicionada a lista de palavras positivas.")
        case "2":
            palavras_negativas.append(nova_palavra) # Adicona a palavra na lista de palavras negativas.
            print(f"A palavra {nova_palavra} foi adicionada a lista dee palavras negativas")

        case _:
            print(f"Opção inválida. A palavra {nova_palavra} não foi adicionada á nenhuma das listas.") # Tratamento de escolha errada.

###############################################################################################################################################################################################################















