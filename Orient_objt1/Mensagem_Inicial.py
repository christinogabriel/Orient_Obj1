# 2) Criando uma Mensagem inicial : 

class Mensagem:
    #Método construtor :
    def __init__(self,Msg,Titulo=None,Copia="") -> None:
        self.Mensagem = Msg
        self.Titulo = Titulo
        self.Copia = Copia

    def CriarMensagem(self,Mensagem,Titulo,Copia):
        self.Mensagem =Mensagem
        self.Titulo = Titulo
        self.Copia =Copia
        return f"Titulo: {Titulo} , Mensagem: {Mensagem} . CC: {Copia}"