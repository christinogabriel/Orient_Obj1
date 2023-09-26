class Mensagem(Autor):
 def __init__(self, Autor, DataCriacao,Msg,Titulo=None,Copia="") -> None:
    super().__init__(Autor=Autor, DataCriacao=DataCriacao)
            self.Mensagem = Mensagem
            self.Titulo = Titulo
            self.Copia =Copia


    @property0
    def Mensagem2(self) ->str:
        return self.__Mensagem

    @Mensagem2.setter
    def Mensagem(self,valor):
        raise ValueError("Você não pode alterar essa variavel!")

    def CriarMensagem(self,Mensagem,Titulo,Copia):
        self.Mensagem =Mensagem
        self.Titulo = Titulo
        self.Copia =Copia
        return f"Titulo: {Titulo} , Mensagem: {Mensagem} . CC: {Copia}"