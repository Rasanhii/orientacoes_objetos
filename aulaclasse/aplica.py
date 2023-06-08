from classes.GerenciarS3 import GerenciarS3

controla_s3 = GerenciarS3('aulanoitejonatas788')

diretorio_destino = 'orientacoes_objetos/aulaclasse/arquivos'
nome_arquivo = 'fotinho.jpg'
controla_s3.download_arquivo(nome_arquivo, diretorio_destino)