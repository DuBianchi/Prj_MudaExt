import re
import string
import os
import shutil

# Coloque os seus parametros aqui...
diretorio = input(r'Qual o diretorio do arquivo: ')
extensao = input('Qual a extensão atual do arquivo: ')
extensao = '.*' + extensao
novaExtensao = input('Qyal a nova extensão do arquivo: ')
novaExtensao = '.' + novaExtensao

# Muda extensao
reg = re.compile(extensao)
if os.path.isdir(diretorio) and not os.path.islink(diretorio):
    arquivos = os.listdir(diretorio)
    for arquivo in arquivos:
        newExt = re.compile(extensao).match
        if newExt(arquivo):
            c = os.path.splitext(arquivo)
            b = c[0] + novaExtensao
            a = os.path.join(diretorio,arquivo)
            b = os.path.join(diretorio,b)
            os.rename(a,b)