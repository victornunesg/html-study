from tkinter import *
from tkinter import ttk, messagebox
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

pastaApp = os.path.dirname(__file__)


def criarpdf():
    try:
        cnv = canvas.Canvas(pastaApp + "\\novopdf.pdf", pagesize=A4)
        cnv.drawString(100, 100, "Teste de texto")
        cnv.save()
    except:
        messagebox.showinfo(title="ERRO", message="Erro ao gerar PDF!")
        return
    messagebox.showinfo(title="PDF", message="PDF criado com sucesso!")


window = Tk()
window.title("Gerador de PDF")
window.geometry("500x500")

b0 = Button(window, text="Criar PDF", command=criarpdf())
b0.pack(side="left", padx=10)

window.resizable(False, False)
window.mainloop()  # loop infinito que só é finalizado quando a janela é fechada, aguardando interação.

# window.configure(bg="#ffffff")
# canvas = Canvas(
#     window,
#     bg="#ffffff",
#     height=646,
#     width=711,
#     bd=0,
#     highlightthickness=0,
#     relief="ridge")
# canvas.place(x=0, y=0)
#
#
#
#
#

#
# b0.place(
#     x=479, y=195,
#     width=178,
#     height=34)
#
# img1 = PhotoImage(file = f"images/img1.png")
# b1 = Button(
#     image = img1,
#     borderwidth = 0,
#     highlightthickness = 0,
#     command = deletar_insumo,
#     relief = "flat")
#
# b1.place(
#     x = 247, y = 197,
#     width = 178,
#     height = 34)
#
# img2 = PhotoImage(file = f"images/img2.png")
# b2 = Button(
#     image = img2,
#     borderwidth = 0,
#     highlightthickness = 0,
#     command = consumir_insumo,
#     relief = "flat")
#
# b2.place(
#     x = 479, y = 123,
#     width = 178,
#     height = 34)
#
# img3 = PhotoImage(file = f"images/img3.png")
# b3 = Button(
#     image = img3,
#     borderwidth = 0,
#     highlightthickness = 0,
#     command = adicionar_insumo,
#     relief = "flat")
#
# b3.place(
#     x = 247, y = 125,
#     width = 178,
#     height = 34)
#
# entry0_img = PhotoImage(file = f"images/img_textBox0.png")
# entry0_bg = canvas.create_image(
#     455.0, 560.0,
#     image = entry0_img)
#
# caixa_texto = Text(
#     bd = 0,
#     bg = "#ffffff",
#     highlightthickness = 0)
#
# caixa_texto.place(
#     x = 250, y = 502,
#     width = 410,
#     height = 114)
#
# entry1_img = PhotoImage(file = f"images/img_textBox1.png")
# entry1_bg = canvas.create_image(
#     517.0, 294.5,
#     image = entry1_img)
#
# nome_insumo = Entry(
#     bd = 0,
#     bg = "#ffffff",
#     highlightthickness = 0)
#
# nome_insumo.place(
#     x = 377, y = 278,
#     width = 280,
#     height = 31)
#
# entry2_img = PhotoImage(file = f"images/img_textBox2.png")
# entry2_bg = canvas.create_image(
#     517.0, 340.5,
#     image = entry2_img)
#
# data_insumo = Entry(
#     bd = 0,
#     bg = "#ffffff",
#     highlightthickness = 0)
#
# data_insumo.place(
#     x = 377, y = 324,
#     width = 280,
#     height = 31)
#
# entry3_img = PhotoImage(file = f"images/img_textBox3.png")
# entry3_bg = canvas.create_image(
#     517.0, 388.5,
#     image = entry3_img)
#
# lote_insumo = Entry(
#     bd = 0,
#     bg = "#ffffff",
#     highlightthickness = 0)
#
# lote_insumo.place(
#     x = 377, y = 372,
#     width = 280,
#     height = 31)
#
# entry4_img = PhotoImage(file = f"images/img_textBox4.png")
# entry4_bg = canvas.create_image(
#     517.0, 436.5,
#     image = entry4_img)
#
# qtde_insumo = Entry(
#     bd = 0,
#     bg = "#ffffff",
#     highlightthickness = 0)
#
# qtde_insumo.place(
#     x = 377, y = 420,
#     width = 280,
#     height = 31)
#
