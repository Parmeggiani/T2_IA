import csv
from cogroo_interface import Cogroo

cogroo = Cogroo.Instance()

classe = []
resposta = []

lema_list = []
analise = []
relevante = []
class_relev = []
contagem_relev = []
bag_words = []
i=0

def conta_frequencia(palavra):
    frequencia=0
    for k in range(len(analise)):
        for j in range(len(analise[k])):
            if(palavra == str(analise[k][j])):
                frequencia = frequencia+1
    return frequencia

with open('perguntas.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    next(readCSV)
    for row in readCSV:
        classe.append(row[3])
        resposta.append(row[2])
        pergunta_lema = cogroo.lemmatize(row[1])
        lema_list.append(str(pergunta_lema)) #adiciona as perguntas lematizadas em uma lista
        analise_perg = cogroo.analyze(pergunta_lema)
        analise.append(analise_perg.sentences[0].tokens) #guarda a analise morfologica das perguntas em uma lista
        
        #print(row[1:4])
        #print("PERGUNTA: ", pergunta_lema)
        #print("RESPOSTA: ", resposta[i])
        #print(lema_list[i])
        #print(classe[i])
        #print("PERGUNTA: ",analise[i])
        #print(len(analise[i]))
        
        y=0
        while(y<len(analise[i])):
            perg = str(analise[i][y])
            if(perg.startswith('o#') or perg.startswith('de#') or perg.startswith(',#') or perg.startswith('que#') or perg.startswith('qual#')
                    or perg.startswith('um#') or perg.startswith('.#') or perg.startswith('?#') or perg.startswith('O#') or perg.startswith('o(')
                    or perg.startswith('ser#') or perg.startswith('quem#') or perg.startswith('em#') or perg.startswith('por#') or perg.startswith('algoritmo#') 
                    or perg.startswith('ir#') or perg.startswith('se#') or perg.startswith('Random_Forest#') or perg.startswith('Random#') or perg.startswith('Forest#')):
                analise[i].pop(y)
                y=y-1
                #print('TENTANDO: ', perg)
            y=y+1
        #print("FOI: ", analise[i])
        i=i+1

    for i in range(len(analise)):
        #pegar as k maiores quantias de termos repedidos devemos colocar sem repeticao em um vetor de cada classe
        # 1. conceito 2. comparacao 3. funcionamento 4. aplicacao 5. hiperparametro 6. desvantagem
        # 7. vantagem 8. metodo 9. historia 10. conceitoArvore 11. paradigma 12. overfitting 13. tarefa
        for y in range(len(analise[i])):
            if(relevante.count(str(analise[i][y])) == 0):
                class_relev.append(classe[i])
                relevante.append(str(analise[i][y]))
                contagem_relev.append(conta_frequencia(str(analise[i][y])))
        print("TERMO: ",relevante[i], "CLASSE: ", class_relev[i], "COUNT: ", contagem_relev[i])

    #k_mais_relevantes = 