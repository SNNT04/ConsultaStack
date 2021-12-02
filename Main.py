import webbrowser
from selenium import webdriver

url = "https://stackoverflow.com/search?q="

texto = input("¿Que quieres buscar? ")



driver = webdriver.Chrome()
driver.get(url)


webbrowser.open_new_tab(url + texto)

driver.find_elements_by_xpath("//*[@id='question-summary-27509']/div[2]/div[1]/h3/a")