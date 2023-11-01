from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors


def mm_to_p(mm):
    return mm / 0.352777


data = {
    "dados_cliente": {
        "cliente": "Roberto",
        "foto_cnh": "url",
        "data_entrada": "dd/MM/YYYY hh:mm",
        "chassis": "aaaa, aaaa",
        "placa": "xxx-9999",
        "tipo_implemento": "MELOSA/COMBOIO"
    }
    # "frente": {
    #     "parabrisa": "true",
    #     "parabrisa_obs": "texto",
    #     "retrovisores": "false",
    #     "retrovisores_obs": "texto",
    #     "capo_grade": "true",
    #     "capo_grade_obs": "text",
    #     "farois": "true",
    #     "farois_obs": "text",
    #     "parachoque": "true",
    #     "parachoque_obs": "text",
    #     "evidencias": "url"
    # },
    # "lateral_direita": {
    #     "porta_direita": "true",
    #     "porta_direita_obs": "text",
    #     "vidro_direito": "true",
    #     "vidro_direito_obs": "text",
    #     "estribo_direito": "true",
    #     "estribo_direito_obs": "text",
    #     "paralama_direito": "true",
    #     "paralama_direito_obs": "text",
    #     "evidencias": "url"
    # },
    # "lateral_esquerda": {
    #     "porta_esquerda": "true",
    #     "porta_esquerda_obs": "text",
    #     "vidro_esquerdo": "true",
    #     "vidro_esquerdo_obs": "text",
    #     "estribo_esquerdo": "true",
    #     "estribo_esquerdo_obs": "text",
    #     "paralama_esquerdo": "true",
    #     "paralama_esquerdo_obs": "text",
    #     "evidencias": "url"
    # },
    # "traseira": {
    #     "lanterna": "true",
    #     "lanterna_obs": "text",
    #     "parachoque": "true",
    #     "parachoque_obs": "text",
    #     "vidro_traseiro": "true",
    #     "vidro_traseiro_obs": "text",
    #     "filtro_ar": "true",
    #     "filtro_ar_obs": "text",
    #     "evidencias": "url"
    # },
    # "chassis": {
    #     "bateria": "true",
    #     "bateria_obs": "text",
    #     "tampa_bateria": "true",
    #     "tampa_bateria_obs": "text",
    #     "tampa_combustivel": "true",
    #     "tampa_combustivel_obs": "text",
    #     "tanque_combustivel": "true",
    #     "tanque_combustivel_obs": "text",
    #     "evidencias": "url"
    # },
    # "checagem_complementar": {
    #     "pneus": {
    #         "dianteiros_presentes": "true",
    #         "traseiros_presentes": "true",
    #         "estepe_presente": "true",
    #         "pneus_obs": "text"
    #     },
    #     "itens_obrigatorios": {
    #         "macaco": "true",
    #         "pino_reboque": "true",
    #         "extintor": "true",
    #         "som": "true",
    #         "tacografo": "true",
    #         "manual": "true",
    #         "chave_reserva": "true",
    #         "chave_basculante": "true",
    #         "itens_obrigatorios_obs": "text"
    #     },
    #     "nivel_combustivel": "text",
    #     "assinatura": "url"
    # }
}

data_list = list()

for key in data.keys():
    data_list.append(list(data[key].keys()))
    data_list.append(list(data[key].values()))

print(data_list)

filename = 'pdfTable.pdf'

pdf = SimpleDocTemplate(filename, pagesize=A4)

table = Table(data_list)

style = TableStyle([
    ('BACKGROUND', (0,0), (5,0), colors.green),
    ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
    ('ALIGN',(0,0),(-1,-1),'CENTER'),
    ('FONTNAME', (0,0), (-1,0), 'Courier-Bold'),
    ('FONTSIZE', (0,0), (-1,0), 12),
    ('BOTTOMPADDING', (0,0), (-1,0), 12),
    ('BACKGROUND',(0,1),(-1,-1),colors.beige),
])

table.setStyle(style)

elements = list()
elements.append(table)

pdf.build(elements)
