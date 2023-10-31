import backend
from tkinter import *


class Model(object):

    def __init__(self, lista_veiculo):
        self.adicionar_itens(lista_veiculo)
        self.gerar_pdf(lista_veiculo)

    def adicionar_itens(self, lista_veiculo):
        backend.adicionar_dados(lista_veiculo)

    def gerar_pdf(self,lista_veiculo):
        backend.gerar_pdf(lista_veiculo)


class View(object):

    @staticmethod
    def abrir_janela(self):
        window = Tk()
        window.title("Gerador de PDF")
        window.geometry("500x500")

        b0 = Button(window, text="Criar PDF", command=backend.gerar_pdf())
        b0.pack(side="left", padx=10)

        window.resizable(False, False)
        window.mainloop()  # loop infinito que só é finalizado quando a janela é fechada, aguardando interação.


class Controller(object):

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def coletar_campos(self, lista_itens):
        self.model.adicionar_itens(lista_itens)

    def gerar_pdf(self, lista_itens):
        self.model.gerar_pdf(lista_itens)
