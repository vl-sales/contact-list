import csv
from parceia_arquivos_csv.parceamento_csv import parceia_csv
from parte_2.sistema import SistemaCadastros

arquivo = open('../parceia_arquivos_csv/contatos.csv', 'r', encoding='utf8')

planilha = list(csv.reader(arquivo, delimiter=';', lineterminator='\n'))

arquivos_estruturados = parceia_csv(planilha)
arquivo.close()

sistema = SistemaCadastros(arquivos_estruturados)
sistema.run()
