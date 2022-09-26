### Importando as bibliotecas a ser usadas ###
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By

### Abrindo o navegador e acessando o arquivo ###
browser = webdriver.Chrome(f"{Path().resolve().parent}\webdriver\chromedriver")
browser.get(f"{Path().resolve().parent}\paginas\Teste2pagina.html")

nome = "Gustavo Melo"
email = "gnorbertom@Hotmail.com"
telefone = "12 1234-5678"

### Alterando o nome ###
browser.find_element(By.ID, "nome").click()
browser.find_element(By.ID, "nome").clear()
browser.find_element(By.ID, "nome").send_keys(nome)

browser.find_element(By.XPATH, "/html/body/div[2]/div/div/button").click()

### Alterando o email ###
browser.find_element(By.ID, "email").click()
browser.find_element(By.ID, "email").clear()
browser.find_element(By.ID, "email").send_keys(email)

browser.find_element(By.XPATH, "/html/body/div[2]/div/div/button").click()

### Alterando o telefone ###
browser.find_element(By.ID, "tel").click()
browser.find_element(By.ID, "tel").clear()
browser.find_element(By.ID, "tel").send_keys(telefone)

browser.find_element(By.XPATH, "/html/body/div[2]/div/div/button").click()

### Fazendo as validações ###
try:
    assert nome in browser.find_element(By.ID, "nome").get_property("value")
    assert email in browser.find_element(By.ID, "email").get_property("value")
    assert telefone in browser.find_element(By.ID, "tel").get_property("value")

except:
    print("Algum campo não estava compativel")
### Fechando o navegador ###

browser.close()
