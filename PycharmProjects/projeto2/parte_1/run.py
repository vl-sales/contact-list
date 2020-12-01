import csv
from parceia_arquivos_csv.parceamento_csv import parceia_csv
from parte_1.interface import Interface

arquivo = open('../parceia_arquivos_csv/contatos.csv', 'r', encoding='utf8')

planilha = list(csv.reader(arquivo, delimiter=';', lineterminator='\n'))

arquivos_estruturados = parceia_csv(planilha)
arquivo.close()

interface = Interface(arquivos_estruturados)
interface.run()