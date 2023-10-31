from tkinter import *
from tkinter import ttk, messagebox
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

pastaApp = os.path.dirname(__file__)


def criarpdf():
    try:
        cnv = canvas.Canvas(pastaApp + "\\novopdf.pdf", pagesize=A4)
        cnv.drawString(100, 100, text=caixa_texto.get('1.0', END))
        cnv.save()
    except:
        messagebox.showinfo(title="ERRO", message="Erro ao gerar PDF!")
        return
    messagebox.showinfo(title="PDF", message="PDF criado com sucesso!")


window = Tk()
window.title("Gerador de PDF")
window.geometry("500x500")

b0 = Button(window, text="Criar PDF", command=criarpdf)
b0.pack(side="left", padx=10)

caixa = Text()
caixa_texto = Text(bd=0, bg="#ffffff", highlightthickness=0)
caixa_texto.place(x=10, y=10, width=300, height=25)

window.resizable(False, False)
window.mainloop()  # loop infinito que só é finalizado quando a janela é fechada, aguardando interação.
