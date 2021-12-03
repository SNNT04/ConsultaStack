import time
from time import sleep
import webbrowser
import os
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

#url = "https://stackoverflow.com/search?q=" + input("¿Que quieres buscar? ")
#se intentó pero tiene captcha y mucho lío saltarselo

#URL de Google buscando lo que se inserte
url = f"https://www.google.com/search?q=%3Asite+stackoverflow.com%2Fquestions%2F" + input("¿Que quieres buscar? ")

#Cosas raras del WebDriver de Selenium
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()

#Le asignamos la URL de la busqueda de Google
driver.get(url)
#Pillamos el valor de 'href' de la etiqueta 'a' correspondiente
url2 = driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/div/div/div/div[1]/a').get_attribute("href")
#Le asignamos como URL el valor de la etiqueta, vamos como si se hiciese click
driver.get(url2)

#Cogemos los div/p que queramos
titulo = driver.find_element_by_xpath('//*[@id="question-header"]/h1/a').text
contenido = driver.find_element_by_xpath('//*[@id="question"]/div[2]/div[2]/div[1]/p').get_attribute("innerHTML")

respuesta_texto = driver.find_element_by_xpath('//*[@id="answer-17844580"]/div/div[2]/div[1]/p').get_attribute("innerHTML")
respuesta_codigo = driver.find_element_by_xpath('//*[@id="answer-17844580"]/div/div[2]/div[1]/pre').get_attribute("innerHTML")

#Esto basicamente hace que se mantenga el programa ejecutandose mientras el usuario no cierre el navegador 
#En caso sacar el resultado por consola, comentar esas lineas seleccionandolas y pulsando 'Control + K + C'
#Para descomentar pulsar 'Control + K + U'

while True:
    try:
        _ = driver.window_handles
    except selenium.common.exceptions.InvalidSessionIdException as e:
        break
    time.sleep(1)

#Muchos prints de manera pocha
print("----Titulo----\n")
print(titulo + "\n\n")

print("----Contenido----\n")
print(contenido + "\n\n")

print("----Respuesta----\n")
print(respuesta_texto + "\n\n")

print("----Codigo----\n")
print(respuesta_codigo + "\n\n")



