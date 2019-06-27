import csv
from cogroo_interface import Cogroo

cogroo = Cogroo.Instance()
classe = []
resposta = []
lema_list = []
analise = []
classes_pergs = []
i=0

with open('corpus.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    next(readCSV)
    for row in readCSV:
        classe.append(row[3])
        resposta.append(row[2])
        pergunta_lema = str(cogroo.lemmatize(row[1]))
        pergunta_lema = pergunta_lema.lower() #Passa todas as palavras para lowercase
        lema_list.append( str(pergunta_lema).split(' ') ) #adiciona as perguntas lematizadas em uma lista
        #analise_perg = cogroo.analyze(pergunta_lema)
        #analise.append(analise_perg.sentences[0].tokens) #guarda a analise morfologica das perguntas em uma lista
        
        y=0
        while(y<len(lema_list[i])):
            perg = str(lema_list[i][y])
            if(perg=='o' or perg=='de' or perg==',' or perg=='que' or perg=='qual' or perg=='a' or perg=='um' or perg=='.' or perg=='o('
                    or perg=='?' or perg=='' or perg=='ser' or perg=='quem' or perg=='em' or perg=='por' or perg=='algoritmo'
                    or perg=='ir' or perg=='se' or perg=='random_forest' or perg=='random' or perg=='forest') or perg=='para':
                lema_list[i].pop(y)
                y=y-1
            y=y+1
        i=i+1

for i in range(len(lema_list)):
    classes_pergs.append( (lema_list[i],classe[i]) )

first_row = ['PERGUNTAS','CLASSES']

with open('corpus_lema.csv','w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(first_row)
    writer.writerows(classes_pergs)
    