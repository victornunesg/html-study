"""
=================
IDEIA DE PROJETO
=================

Fazer uma API por conta propria, com 4 rotas, se comunicando com o banco de dados
    1) Rota que voce recebe cadastros de pessoa, pega alguns dados, valida com marshmallow, usa esses dados para determi
    nar outros campos, tipo: idade, signo, alguma logica por tras;
    2) Rota que devolva todos os usuários, com as informações processadas;
    3) Rota que só envia informação de um cliente especifico;
    4) Rota que deleta um cliente específico;

Evoluções:
    - Autenticação por token para acesso aos dados;
    - Uso de cache;
    - Devolver informações documentadas em algum formato / aceitar os dados na rota por algum formato (json, xml, etc)


Após isso, fazer conta gratuita no GCP (Google Cloud) e testar funcionalidades

"""