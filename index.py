import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service("drivers/chromedriver.exe") # Crear el servicio
bot = webdriver.Chrome(service=service) # Crear el bot
bot.maximize_window() # Maximizar la ventana
bot.get("https://www.viajesexito.com") # Abrir el sitio de viajes exito

packages = bot.find_element(By.XPATH, '/html/body/form/header/div[2]/div/div/nav/div[4]/a') # El bot encuentra el elemento de paquetes mediante XPATH
packages.click() # El bot hace click en el elemento de paquetes
time.sleep(1) # El bot espera 1 segundo

origin = bot.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[1]/div/div[1]/div/div/input') # El bot encuentra el input origen mediante XPATH 
origin.click() # El bot hace click en el input origen
time.sleep(1) # El bot espera 1 segundos

focusOrigin = bot.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/div[2]/input') # El bot encuentra el nuevo input de origen mediante XPATH
focusOrigin.send_keys('José María Cordova') # El bot mandar el texto al input de origen
time.sleep(1) # El bot espera 1 segundos
focusOrigin.send_keys(Keys.ENTER) # El bot presiona la tecla ENTER en el input de origen
time.sleep(1)# El bot espera 1 segundos

destination = bot.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[1]/div/div[3]/div/div/input') # El bot encuentra el input de destino mediante XPATH
destination.click() # El bot hace click en el input de destino
time.sleep(1) # El bot espera 1 segundos

focusDestination = bot.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/div[2]/input') # El bot encuentra el nuevo input de destino mediante XPATH
focusDestination.send_keys('Punta Cana') # El bot manda el texto al input de destino
time.sleep(1) # El bot espera 1 segundos
focusDestination.send_keys(Keys.ENTER) # El bot presiona la tecla ENTER en el input de destino
time.sleep(1) # El bot espera 1 segundos


date = bot.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[2]/div/input') # El bot encuentra el input de la fecha mediante XPATH
date.click() # El bot hace click en el input de la fecha
time.sleep(1) # El bot espera 1 segundos

outDate = bot.find_element(By.XPATH, '//html/body/div[11]/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div[5]/div[1]/div[2]/div[1]') # El bot encuentra la fecha de salida mediante XPATH (18-12-2023)
outDate.click() # El bot hace click en la fecha de salida
time.sleep(1) # El bot espera 1 segundos

returnDate = bot.find_element(By.XPATH, '/html/body/div[11]/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div[6]/div[4]/div[2]/div[1]') # El bot encuentra la fecha de regreso mediante XPATH (28-12-2023)
returnDate.click() # El bot hace click en la fecha de regreso
time.sleep(1) # El bot espera 1 segundos

submitDate = bot.find_element(By.XPATH, '/html/body/div[11]/div[2]/div[2]/div[2]/button[2]') # El bot encuentra el botón de aceptar mediante XPATH
submitDate.click() # El bot hace click en el botón de aceptar
time.sleep(1) # El bot espera 1 segundos

rooms = bot.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[3]') # El bot encuentra el botón de habitaciones mediante XPATH
rooms.click() # El bot hace click en el botón de habitaciones
time.sleep(1) # El bot espera 1 segundos

# Cuando se le da click a rooms ya esta por defecto que la habitación es para dos adultos

newRoom = bot.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[2]/div[1]/button[1]') # El bot encuentra el botón de nueva habitación mediante XPATH
newRoom.click() # El bot hace click en el botón de nueva habitación
time.sleep(1) # El bot espera 1 segundos

# Cuando se da click a nueva habitación, se crea una nueva habitación para un adulto por defecto 

submitRooms = bot.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[2]/div[2]/button') # El bot encuentra el botón de aceptar habitaciones mediante XPATH
submitRooms.click() # El bot hace click en el botón de aceptar habitaciones
time.sleep(1) # El bot espera 1 segundos

search = bot.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[4]/a') # El bot encuentra el botón de buscar mediante XPATH
search.click() # El bot hace click en el botón de buscar
time.sleep(1) # El bot espera 1 segundos

# Al darle buscar se genera una nueva ventana

newWindow = bot.window_handles[1] # Se obtiene la nueva ventana
bot.switch_to.window(newWindow) # El bot cambia a la nueva ventana

WebDriverWait(bot, 26).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[1]/div/div/div[2]/div/div[1]/div/p[1]/span[2]'))) # El bot espera a que se cargue el elemento de precio en la nueva ventana, esperará maximo 26 segundos

for i in range(1, 11): # Se hace un ciclo para obtener los 10 primeros precios de los paquetes
    xpath = f'/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[{i}]/div/div/div[2]/div/div[1]/div/p[1]/span[2]' # Se crea el XPATH para obtener el precio el cual se iterará en el div de los paquetes
    price = bot.find_element(By.XPATH, xpath) # El bot encuentra el precio mediante XPATH
    print(price.text) # El bot imprime el precio

advancedSettings = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[6]/a') # El bot encuentra el botón de opciones avanzadas mediante XPATH
advancedSettings.click() # El bot hace click en el botón de opciones avanzadas
time.sleep(1) # El bot espera 1 segundos

airlane = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[7]/div[2]/input') # El bot encuentra el input de aerolinea mediante XPATH
airlane.click() # El bot hace click en el input de aerolinea
airlane.send_keys('Avianca') # El bot manda el texto al input de aerolinea
airlane.send_keys(Keys.ENTER) # El bot presiona la tecla ENTER en el input de aerolinea
time.sleep(1) # El bot espera 1 segundos

advancedSearch = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[8]/input') # El bot encuentra el botón de buscar mediante XPATH
advancedSearch.click() # El bot hace click en el botón de buscar
time.sleep(1) # El bot espera 1 segundos

WebDriverWait(bot, 26).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[1]/div/div/div[2]/div/div[1]/div/p[1]/span[2]'))) # El bot espera a que se carguen los elementos de la ventana, esperará maximo 26 segundos

contactUs = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[5]/footer/div[2]/div/div/div[1]/div/p/a') # El bot encuentra el botón de contactanos mediante XPATH
contactUs.click() # El bot hace click en el botón de contactanos
time.sleep(3) # El bot espera 3 segundos


bot.quit() # Cerrar el bot