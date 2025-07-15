from categorias import Classificador
from utils import mover_arquivo, criar_pasta
from pathlib import Path

def main():
    pasta = Path.home() / "Downloads"
    arquivos = [f for f in pasta.iterdir() if f.is_file()]
    classificador = Classificador()

    for arquivo in arquivos:
        categoria = classificador.definir_categoria(arquivo)
        destino = pasta / categoria
        criar_pasta(destino)
        mover_arquivo(arquivo, destino)
        print(f"Movido: {arquivo.name} → {categoria}/")

if __name__ == "__main__":
    main()
