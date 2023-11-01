from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

pastaApp = os.path.dirname(__file__)

dados = {
  "dados_cliente": {
    "cliente": "Roberto",
    "foto_cnh": "url",
    "data_entrada": "dd/MM/YYYY hh:mm",
    "chassis": "aaaa, aaaa",
    "placa": "xxx-9999",
    "tipo_implemento": "MELOSA/COMBOIO"
  },
  "frente": {
    "parabrisa": "true",
    "parabrisa_obs": "texto",
    "retrovisores": "false",
    "retrovisores_obs": "texto",
    "capo_grade": "true",
    "capo_grade_obs": "text",
    "farois": "true",
    "farois_obs": "text",
    "parachoque": "true",
    "parachoque_obs": "text",
    "evidencias": ["url", "url", "..."]
  }
}


# def adicionar_dados(lista):
#     lista.append(input("Modelo: "))
#     lista.append(input("Placa: "))
#     lista.append(input("Ano: "))
#     lista.append(input("Status: "))
#     print(lista)
#     return lista
#
#
def gerar_pdf(dados):
    try:
        pdf = canvas.Canvas(pastaApp + "\\arquivos\checklist.pdf", pagesize=A4)
        y = 800
        # for dado in lista_preenchida:
        #     cnv.drawString(100, y, dado)
        #     y -= 20
        for chave in dados['dados_cliente']:
          print(f'{chave}: {dados["dados_cliente"][chave]}')
          pdf.drawString(100, y, f'{chave}: {dados["dados_cliente"][chave]}')
          y -= 20
        pdf.setFont('Arial', 12)
        pdf.save()
    except:
        print("Erro ao gerar PDF!")
        return
    print("PDF criado com sucesso!")


gerar_pdf(dados)