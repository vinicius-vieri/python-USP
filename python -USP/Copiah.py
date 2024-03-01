import re
import math

def le_assinatura():
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho médio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    return textos

def separa_sentencas(texto):
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    return frase.split()

def n_palavras_unicas(lista_palavras):
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1
    return unicas

def n_palavras_diferentes(lista_palavras):
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1
    return len(freq)

def calcula_assinatura(texto):
    sentencas = separa_sentencas(texto)
    frases = [frase for sentenca in sentencas for frase in separa_frases(sentenca)]
    palavras = [palavra for frase in frases for palavra in separa_palavras(frase)]

    num_palavras = len(palavras)
    num_sentencas = len(sentencas)
    num_frases = len(frases)

    tam_palavras = sum(len(palavra) for palavra in palavras) / num_palavras
    type_token = n_palavras_diferentes(palavras) / num_palavras
    hapax_legomana = n_palavras_unicas(palavras) / num_palavras
    tam_sentencas = sum(len(sentenca) for sentenca in sentencas) / num_sentencas
    complexidade_sentencas = num_frases / num_sentencas
    tam_frases = sum(len(frase) for frase in frases) / num_frases

    return [tam_palavras, type_token, hapax_legomana, tam_sentencas, complexidade_sentencas, tam_frases]

def compara_assinatura(as_a, as_b):
    similaridade = 0
    for i in range(len(as_a)):
        similaridade += abs(as_a[i] - as_b[i])
    return similaridade / 6

def avalia_textos(textos, ass_cp):
    assinatura_cp = ass_cp
    similaridades = []
    for texto in textos:
        ass_texto = calcula_assinatura(texto)
        similaridade = compara_assinatura(ass_texto, assinatura_cp)
        similaridades.append(similaridade)
    return similaridades.index(min(similaridades)) + 1

if __name__ == "__main__":
    ass_cp = le_assinatura()
    textos = le_textos()
    texto_infectado = avalia_textos(textos, ass_cp)
    print(f'O autor do texto {texto_infectado} está infectado com COH-PIAH')
