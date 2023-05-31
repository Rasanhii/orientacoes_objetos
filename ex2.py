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
        
        