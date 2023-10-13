import pyautogui
import time

assunto = "Assunto X"
mensagem = "Mensagem X"

path = "C:\\Users\\Vitor\\Downloads\\Estudo\\Python\\Projetos\\Email_Bot\\Emails.txt"

with open(path, "r", encoding="UTF-8") as file:
    listEmails = file.readlines()

for i in range(0,len(listEmails)):

    # Nova mensagem
    pyautogui.click(80, 186, duration= 1)

    # Destinatario
    pyautogui.click(1545, 488, duration= 1)
    pyautogui.write(listEmails[i])

    # Assunto
    pyautogui.click(1271, 526, duration= 1)
    pyautogui.write(assunto)

    # Conteudo da mensagem
    pyautogui.click(1551, 721, duration= 1)
    pyautogui.write(mensagem)

    # Enviar email
    pyautogui.click(1305, 1008, duration= 1)
    time.sleep(5)