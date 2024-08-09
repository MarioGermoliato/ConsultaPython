import yfinance
import pyautogui
import pyperclip
import webbrowser
import time


ticker = input("Digite a ação desejada: ")
datainicio = input("Digite a data inicial no formato yyyy-mm-dd")
datatermino = input("Digite a data final no formato yyyy-mm-dd")

dados = yfinance.Ticker(ticker).history(start = datainicio, end = datatermino)
fechamento = dados.Close

maxima = round(fechamento.max(), 2)
minima = round(fechamento.min(), 2)
valor_medio = round(fechamento.mean(), 2)

destinatario = "mgermoliato@yahoo.com.br"
assunto = "Analises do de ações"

mensagem = f""""
Prezado gestor, 

Seguem as análises solicitadas da ação {ticker}

Cotação máxima: R${maxima}
Cotação mínima: R${minima}
Valor médio: R${valor_medio}

Atenciosamente,
Mario Germoliato
"""

# abrir o navegador e ir para o gmail
 
webbrowser.open("www.gmail.com")
time.sleep(3)

# configurando uma pausa de 3 segundos entre as etapas
pyautogui.PAUSE = 3

# clicar no botão escrever, colocar as coordenadas corretas para cada computador
pyautogui.click(x = 2017, y = 213)

# digitar o email do destinatário e teclar TAB
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# digitar o assunto e teclar TAB
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# digitar a mensagem
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")

# clicar em enviar
pyautogui.click(x = 3230, y= 998)

print("Email enviado com sucesso!")