import os
import json
from datetime import datetime

LOGS_DIR = "logs"
LOG_FILE = os.path.join(LOGS_DIR, "log.json")
'''
Caso nn haja o diretório de logs, ele será criado. O arquivo log.json é onde os registros serão armazenados. 
Cada execução do script irá adicionar um novo registro com a data e hora, além de listar
os arquivos .gitkeep criados e removidos durante o processo de verificação dos diretórios.
'''
def criar_logs():
    os.makedirs(LOGS_DIR, exist_ok=True)

# Carrega os registros existentes do log, ou retorna uma lista vazia se o arquivo não existir ou estiver vazio.
def carregar_logs():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r", encoding="utf-8") as arquivo:
            try:
                return json.load(arquivo)
            except json.JSONDecodeError:
                return []

    return []

'''
Salva um novo registro no log, adicionando-o à lista de registros existentes e
escrevendo tudo de volta no arquivo log.json.
'''
def salvar_logs(registro):
    historico = carregar_logs()
    historico.append(registro)

    with open(LOG_FILE, "w", encoding="utf-8") as arquivo:
        json.dump(
            historico,
            arquivo,
            indent=4,
            ensure_ascii=False
        )

# Processa os diretórios a partir da raiz especificada, verificando se estão vazios ou não.
def processar_diretorios(raiz="."):
    criados = []
    removidos = []

    for caminho, diretorios, arquivos in os.walk(raiz):

        # Ignora completamente o diretório logs
        diretorios[:] = [
            d for d in diretorios
            if d != LOGS_DIR
        ]

        gitkeep = os.path.join(caminho, ".gitkeep")

        # Lista de arquivos desconsiderando o .gitkeep
        arquivos_sem_gitkeep = [
            arq for arq in arquivos
            if arq != ".gitkeep"
        ]

        possui_subdiretorios = len(diretorios) > 0
        possui_arquivos = len(arquivos_sem_gitkeep) > 0

        vazio = not possui_subdiretorios and not possui_arquivos

        if vazio:
            if not os.path.exists(gitkeep):
                with open(gitkeep, "w", encoding="utf-8"):
                    pass
                criados.append(gitkeep)

        else:
            if os.path.exists(gitkeep):
                os.remove(gitkeep)
                removidos.append(gitkeep)

    return criados, removidos


def main():
    criar_logs()

    criados, removidos = processar_diretorios()

    registro = {
        "data_hora": datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        ),
        "gitkeep_criados": criados,
        "gitkeep_removidos": removidos
    }

    salvar_logs(registro)

    print("Execução finalizada!")
    print(f".gitkeep criados: {len(criados)}")
    print(f".gitkeep removidos: {len(removidos)}")


if __name__ == "__main__":
    main()