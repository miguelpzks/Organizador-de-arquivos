import shutil

def criar_pasta(caminho):
    caminho.mkdir(exist_ok=True)

def mover_arquivo(arquivo, destino):
    novo_caminho = destino / arquivo.name
    shutil.move(str(arquivo), str(novo_caminho))
