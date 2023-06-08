from classes.GerenciarS3 import GerenciarS3
class MenuGerenciadorS3:
    def __init__(self, nome_bucket):
        self.gerenciador = GerenciarS3(nome_bucket)
        
    def exibir_menu(self):
        print('--- Menu --- \n1. Listar aquivos. \n2. Enviar arquivos. \n3. Baixar arquivo \n4. Excluir arquivo \n0. Sair')
            
    def listar_arquivos(self):
        self.gerenciador.lista_arquivos()
    
    def enviar_arquivo(self):
        caminho_arquivo = input('Digite o caminho do arquivo: ')
        nome_arquivo = input('Digite o caminho para salvat o arquivo: ')
        self.gerenciador.upload_arquivo(nome_arquivo, caminho_arquivo)
    
    def baixar_arquivo(self):
        caminho_arquivo = input('Digite o caminho do arquivo: ')
        nome_arquivo = input('Digite o caminho para salvat o arquivo: ')
        self.gerenciador.download_arquivo(nome_arquivo, caminho_arquivo)
        
    def excluir_arquivo(self):
        nome_arquivo = input('Digite o nome do arquivo que desejo excluir: ')
        self.gerenciador.delete_arquivo(nome_arquivo)
        
    def executar(self):
        while True:
            self.exibir_menu()
            opcao = input('Digite a opção desejada: ')
            if opcao == '1':
                self.listar_arquivos()
            elif opcao == '2':
                self.enviar_arquivo()
            elif opcao == '3':
                self.baixar_arquivo()
            elif opcao == '4':
                self.excluir_arquivo()
            elif opcao == '0':
                print('Encerrando o programa')
                break
            else:
                print('Opção inválida. Digite novamente')
                
                