import os
import boto3

class GerenciarS3:
    def __init__(self, nome_bucket):
        self.nome_bucket = nome_bucket
        self.s3 = boto3.client('s3')
        
    def lista_arquivos(self):
        try:
            resposta = self.s3.list_objects_v2(Bucket=self.nome_bucket)
            
            if 'Contents' in resposta:
                files = [obj['Key'] for obj in resposta['Contents']]
                print('Arquivos no S3')
                for file in files:
                    print(file)
            else:
                print('Nenhum arquivo encontrado no S3.')
        except Exception as e:
            print(f'Erro ao excluir o arquivo do S3: {e}')
            
            
    def delete_arquivo(self, nome_arquivo):
        try:
            self.s3.delete_object(Bucket=self.nome_bucket, Key=nome_arquivo)
            print(f'Arquivo {nome_arquivo} excluído do S3 com sucesso.')
        except Exception as e:
            print(f'Erro ao excluir o arquivo do S3: {e}')