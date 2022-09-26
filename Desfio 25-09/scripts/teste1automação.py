### Importando as bibliotecas a ser usadas ###
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By

### Abrindo o navegador e acessando o arquivo ###
browser = webdriver.Chrome(f"{Path().resolve().parent}\webdriver\chromedriver")
browser.get(f"{Path().resolve().parent}\paginas\Teste1pagina.html")

### Encontrando os valores e os somando ###
val1 = int(browser.find_element(By.ID, "val1").get_property("value"))
val2 = int(browser.find_element(By.ID, "val2").get_property("value"))
total = val1 + val2

### Inserindo o resultado no campo ###
browser.find_element(By.ID, "total").clear()
browser.find_element(By.ID, "total").send_keys(total)

### Clicando no validador e validando a mensagem ###
browser.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/button").click()
try:
    assert "Correto" in browser.find_element(By.ID, "correto").get_property("value")

except:
    print("Resultado estava incorreto")
### Fechando o navegador ###
browser.close()
