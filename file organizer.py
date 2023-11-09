import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione uma pasta para organizar!")

lista_arquivos =  os.listdir(caminho)

locais = {
    "imagens": [".png", ".jpg", ".gif",".jpeg"],
    "Executaveis": [".exe"],
    "planilhas": [".xlsx"],
    "pdfs":[".pdf"],
    "csv":[".csv"],
    "packages":[".package"],
    "prontos para extrair":[".zip",".7z",'rar'],
    "Arquivos ISO": [".iso"]
}

for arquivo in lista_arquivos:
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")