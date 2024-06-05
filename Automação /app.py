import openpyxl
import pyperclip 
import pyautogui
import time

# entrar na planilha 

workbook = openpyxl.load_workbook("./produtos_ficticios.xlsx")
sheet_produtos = workbook ["Produtos"]

#copiar informações de um campo e colar no seu campo correspondente. 
for linha in sheet_produtos.iter_rows(min_row=2):
    nome_do_produto = linha[0].value
    pyperclip.copy(nome_do_produto)
    pyautogui.click(902,257,duration=1)
    pyautogui.click(902,257,duration=1)
    pyautogui.hotkey("command","v")

    descricao_do_produto = linha[1].value 
    pyperclip.copy(descricao_do_produto)
    pyautogui.click(896,339,duration=1)
    pyautogui.hotkey("command","v")

    categoria_do_produto = linha[2].value 
    pyperclip.copy(categoria_do_produto)
    pyautogui.click(895,476,duration=1)
    pyautogui.hotkey("command","v")
    
    codigo_do_produto = linha[3].value 
    pyperclip.copy(codigo_do_produto)
    pyautogui.click(896,561,duration=1)
    pyautogui.hotkey("command","v")

    peso_do_produto = linha[4].value 
    pyperclip.copy(peso_do_produto)
    pyautogui.click(899,647,duration=1)
    pyautogui.hotkey("command","v")

    dimensoes_do_produto = linha[5].value 
    pyperclip.copy(dimensoes_do_produto)
    pyautogui.click(892,737,duration=1)
    pyautogui.hotkey("command","v")

    pyautogui.click(918,798,duration=1)
    time.sleep(3)

    preco_do_produto = linha[6].value 
    pyperclip.copy(preco_do_produto)
    pyautogui.click(903,283,duration=1)
    pyautogui.hotkey("command","v")

    quantidadeEstoque_do_produto = linha[7].value 
    pyperclip.copy(quantidadeEstoque_do_produto)
    pyautogui.click(903,364,duration=1)
    pyautogui.hotkey("command","v")

    datadevalidade_do_produto = linha[8].value 
    pyperclip.copy(datadevalidade_do_produto)
    pyautogui.click(903,453,duration=1)
    pyautogui.hotkey("command","v")

    cor_do_produto = linha[9].value 
    pyperclip.copy(cor_do_produto)
    pyautogui.click(905,541,duration=1)
    pyautogui.hotkey("command","v")

    #item tamanho precisa comparar e selecionar.

    tamanho_do_produto = linha[10].value 
    pyperclip.copy(tamanho_do_produto)
    pyautogui.click(913,624,duration=1)
    if tamanho_do_produto == "Pequeno":
        pyautogui.click(913,624,duration=1)
    elif tamanho_do_produto == "Médio":
        pyautogui.click(914,642,duration=1)
    else :
        pyautogui.click(930,669,duration=1)


    material_do_produto = linha[11].value 
    pyperclip.copy(material_do_produto)
    pyautogui.click(903,711,duration=1)
    pyautogui.hotkey("command","v")

    pyautogui.click(921,776,duration=1)
    time.sleep(3)

    fabricante_do_produto = linha[12].value 
    pyperclip.copy(fabricante_do_produto)
    pyautogui.click(904,295,duration=1)
    pyautogui.hotkey("command","v")


    pais_do_produto = linha[13].value 
    pyperclip.copy(pais_do_produto)
    pyautogui.click(901,383,duration=1)
    pyautogui.hotkey("command","v")

    observacoes_do_produto = linha[14].value 
    pyperclip.copy(observacoes_do_produto)
    pyautogui.click(904,476,duration=1)
    pyautogui.hotkey("command","v")

    codigobarras_do_produto = linha[15].value 
    pyperclip.copy(codigobarras_do_produto)
    pyautogui.click(907,601,duration=1)
    pyautogui.hotkey("command","v")

    localizacao_do_produto = linha[16].value
    pyperclip.copy(localizacao_do_produto)
    pyautogui.click(899,689,duration=1)
    pyautogui.hotkey("command","v") 

    pyautogui.click(921,756,duration=1)
    time.sleep(3)

    pyautogui.click(1321,463,duration=1)
    time.sleep(3)

    pyautogui.click(1154,530,duration=1)
    time.sleep(3)



   