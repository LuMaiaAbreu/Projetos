import tkinter as tk
from tkinter import filedialog
import cv2 
import pytesseract
import pyperclip


def capturar_caminho_imagem():
    global texto_extraido
    # Abrir uma janela de diálogo para selecionar um arquivo de imagem
    caminho_imagem = filedialog.askopenfilename()
    imagem = cv2.imread(caminho_imagem)
    texto_extraido =pytesseract.image_to_string(imagem)
    exibir_texto(texto_extraido)

def exibir_texto(texto):
    # Atualiza o texto na Label para exibir o texto obtido
    tela_leitura.config(text=texto)

def copiar_texto():
    pyperclip.copy(texto_extraido)


janela = tk.Tk()

# Define o caminho para o executável do tesseract
caminho = "/opt/homebrew/bin/tesseract"
# Define o caminho do executável do tesseract
pytesseract.pytesseract.tesseract_cmd = caminho


tela_leitura = tk.Label(janela,text="")
tela_leitura.pack()

botao_selecionar = tk.Button(janela, text="Selecionar Imagem", command=capturar_caminho_imagem)
botao_selecionar.pack()

botao_copiar = tk.Button(janela, text="copiar texto", command=copiar_texto)
botao_copiar.pack()

janela.mainloop()
