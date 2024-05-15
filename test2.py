from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

# Создаем экземпляр браузера
browser = webdriver.Chrome()

# Открываем страницу Википедии
browser.get('https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D0%B5%D1%87%D0%BD%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0')

# Инициализируем список для хранения элементов с классом "hatnote navigation-not-searchable"
hatnotes = []
for element in browser.find_elements(By.TAG_NAME, "div"):
    # Получаем значение атрибута "class"
    cl = element.get_attribute("class")
    if cl == "hatnote navigation-not-searchable":
        hatnotes.append(element)

# Печатаем найденные элементы
print(hatnotes)

# Выбираем случайный элемент из найденных
hatnote = random.choice(hatnotes)

# Находим ссылку внутри выбранного элемента
link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")

# Переходим по найденной ссылке
browser.get(link)
time.sleep(10)

# Закрытие браузера
browser.quit()



