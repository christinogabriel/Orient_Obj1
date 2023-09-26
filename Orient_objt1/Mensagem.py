# 1) Criando uma classe :

class Mensagem:
    #Método construtor :
    def __init__(self) -> None:
        self.Mensagem = ""
        self.Titulo = ""
        self.Copia = ""
    #Função:
    def CriarMensagem(self,Mensagem,Titulo,Copia):
            self.Mensagem =Mensagem
            self.Titulo = Titulo
            self.Copia =Copia
            return f"Titulo: {Titulo} , Mensagem: {Mensagem} . CC: {Copia}"
