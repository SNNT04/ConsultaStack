import webbrowser

url = "https://stackoverflow.com/search?q="

texto = input("¿Que quieres buscar? ")

webbrowser.open_new_tab(url + texto)