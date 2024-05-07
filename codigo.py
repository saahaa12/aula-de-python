
#para instalar : pip install pyautogui
import pyautogui
import time

time.sleep(5)
print(pyautogui.position())

pyautogui.scroll(-250)



#pyautogui.click -> clica com o mouse 
#pyautogui.write-> escrever texto
#pyautogui.press->pressionar uma tecla do teclado
#pyautogui.hotkey-> apertar um conjunto de teclas (Ctrl, C,Ctrl,V,Alt Tab)
 
pyautogui.PAUSE = 0.5


#abir o navegador 

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

#entrar no sistema 

pyautogui.write ("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press ("enter")

#aqui pode ser que ele demore alguns segundos para carregar o site 
time.sleep(3)

#2. fazer login

pyautogui.click(x=682, y=462)
pyautogui.write("sasaamaral-16@hotmail.com")


pyautogui.press("tab")
pyautogui.write("sua senha aqui")

pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

#abrir\importar a base de dados de produtos para cadastrar 
#pip install pandas numpy openpyxl

import pandas as pd

tabela= pandas.read_csv("produtos.csv")
print(tabela)

#4 cadastrar um produto 

for linha in tabela.index:
    codigo=str(tabela.loc[linha,"codigo"])
    codigo = "MOLO000251"

    #clicar no campo do código do produto
    pyautogui.click(x=647, y=326)
    #preencher o código
    pyautogui.write(codigo)
    #passar pro proximo campo
    pyautogui.press("tab")
    #marca
    pyautogui.writecodigo(str(tabela.loc[linha,"marca"]))
    #passar para o proximo campo
    pyautogui.press("tab")
    #tipo
    pyautogui.writecodigo(str(tabela.loc[linha,"tipo"]))
    #passar para o proximo
    pyautogui.press("tab")
    #categoria
    pyautogui.writecodigo(str(tabela.loc[linha,"categoria"]))
    #passar para o proximo
    pyautogui.press("tab")
    #preço
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
    #passar para o proximo
    pyautogui.press("tab")
    #custo
    pyautogui.write(str(tabela.loc[linha,"custo"]))
    #passar para o proximo
    pyautogui.press("tab")
    #obs
    obs =  (str(tabela.loc[linha,"obs"]))
    if obs != "nan":
         pyautogui.write(obs)
    
    (str(tabela.loc[linha,"obs"]))

    #passar para o proximo
    pyautogui.press("tab")
    #apertar o botão
    pyautogui.press("enter")
    pyautogui.scroll(5000)



