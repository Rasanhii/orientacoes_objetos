import os
import boto3
class Gerenciar53:
    def __init__(self, nome_bucket):
        self.nome_bucket = nome_bucket
        self.s3 = boto3.client('s3')
        
    def lista_arquivos(self):
        try:
            resposta = self.s3.list_objects_v2(Bucket=self.nome_bucket)
            
            if 'Contents' in resposta:
                files = [obj['Key'] for obj in resposta['Contents']]
                print('Arquivos s3: ')
                for file in files:
                    print (file)
            
            else:
                print('Nunhum arquivo encontrado no S3.')
                    
        except Exception as e:
            print(f'Erro ao listar os arquivos do S3: {e}')
    
    def upload_arquivo(self, caminho_arquivo, nome_arquivo=None):
        if nome_arquivo is None:
            nome_arquivo = caminho_arquivo
            
        try:
            self.s3.update_file(caminho_arquivo, self.nome_bucket, nome_arquivo)
            print(f'Arquivo {nome_arquivo} enviado para o S3 com sucesso.')
        except Exception as e:
            print(f'Erro ao enviar o arquivo para o S3: {e}')
      
    def download_arquivo(self, nome_arquivo, caminho_arquivo):
        if nome_arquivo is None:
            nome_arquivo = caminho_arquivo
        
        try:
            caminho_completo = os.path.join(caminho_arquivo, nome_arquivo)
            self.s3.download_file(self.nome_bucket, nome_arquivo, caminho_completo)
            print(f'arquivo {nome_arquivo} baicado do S3 com sucesso.')
        except Exception as e:
            print(f'Erro ao baixar o arquivo do S3: {e}' )
            

        
        