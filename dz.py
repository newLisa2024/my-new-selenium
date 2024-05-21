from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import textwrap

def print_paragraphs(content, width=80):
    paragraphs = content.split('\n\n')
    for i, paragraph in enumerate(paragraphs):
        print(f"\nПараграф {i+1}:\n")
        print(textwrap.fill(paragraph, width=width))
        input("\nНажмите Enter, чтобы продолжить...\n")

def show_article(browser):
    while True:
        print("\nOptions:\n1. Перечислить параграфы статьи\n2. Перейти на соответствующую страницу\n3. Выйти\n")
        choice = input("Выберите вариант (1, 2, 3): ")

        if choice == '1':
            content = browser.find_element(By.ID, 'mw-content-text').text
            print_paragraphs(content)
        elif choice == '2':
            links = browser.find_elements(By.CSS_SELECTOR, '#mw-content-text a')
            link_texts = [link.text for link in links if link.text]

            for i, link_text in enumerate(link_texts):
                print(f"{i+1}. {link_text}")

            index = int(input(f"Выберите ссылку для перехода (1-{len(link_texts)}): ")) - 1
            if 0 <= index < len(link_texts):
                links[index].click()
                time.sleep(3)  # Дождитесь загрузки страницы
            else:
                print("Неверный выбор. Попробуйте еще раз.")
        elif choice == '3':
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")

def main():
    browser = webdriver.Chrome()
    browser.get('https://en.wikipedia.org')

    initial_query = input("Введите свой первоначальный поисковый запрос: ")
    search_box = browser.find_element(By.NAME, 'search')
    search_box.send_keys(initial_query)
    search_box.send_keys(Keys.RETURN)

    time.sleep(3)  # Дождитесь загрузки страницы

    show_article(browser)

    browser.quit()

if __name__ == "__main__":
    main()
