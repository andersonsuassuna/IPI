from django.shortcuts import render

SERVICOS_DB = [
    {"id": 1, "nome_servico": "Consultoria em TI", "responsavel": "Carlos Silva", "tempo_estimado": "40 horas", "requisitos": "Acesso root aos servidores e topologia da rede."},
    {"id": 2, "nome_servico": "Manutenção Preventiva", "responsavel": "Ana Paula", "tempo_estimado": "12 horas", "requisitos": "Equipamentos desligados durante a janela de manutenção."},
    {"id": 3, "nome_servico": "Migração para Nuvem", "responsavel": "João Souza", "tempo_estimado": "120 horas", "requisitos": "Backup integral do banco de dados atualizado."},
    {"id": 4, "nome_servico": "Auditoria de Segurança", "responsavel": "Mariana Lima", "tempo_estimado": "80 horas", "requisitos": "Lista de usuários, permissões e políticas da empresa."},
    {"id": 5, "nome_servico": "Treinamento Corporativo", "responsavel": "Roberto Alves", "tempo_estimado": "24 horas", "requisitos": "Sala de reuniões com projetor e laptops para os alunos."}
]

def listagem(request):
    return render(request, 'servicos/listagem.html', {'servicos': SERVICOS_DB})

def detalhe(request, id):
    servico_selecionado = next((s for s in SERVICOS_DB if s["id"] == id), None)
    return render(request, 'servicos/detalhe.html', {'servico': servico_selecionado})