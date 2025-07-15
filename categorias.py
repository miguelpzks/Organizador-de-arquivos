# categorias.py

class Classificador:
    def __init__(self):
        self.categorias = {
            "Imagens": [".jpg", ".jpeg", ".png", ".gif"],
            "Documentos": [".pdf", ".docx", ".txt"],
            "Compactados": [".zip", ".rar", ".7z"],
            "Instaladores": [".exe", ".msi"],
            "Vídeos": [".mp4", ".mkv", ".avi"],
        }

    def definir_categoria(self, arquivo):
        ext = arquivo.suffix.lower()
        for categoria, extensoes in self.categorias.items():
            if ext in extensoes:
                return categoria
        return "Outros"
