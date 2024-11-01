# Необходимо спарсить цены на диваны с сайта divan.ru в csv файл,
# обработать данные

import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def get_prices():
    page = 'https://www.divan.ru/sankt-peterburg/category/torshery'
    driver = webdriver.Chrome()
    print('Начинаем упражнение')
    driver.get(page)

    WebDriverWait(driver, 5).until(ec.presence_of_all_elements_located(
        (By.CLASS_NAME, 'WdR1o')))
    raw_data = driver.find_elements(By.CLASS_NAME, 'WdR1o')
    try:
        with open('data_to_df.csv', 'w', newline='', encoding='utf-8-sig') as file:
            writer = csv.writer(file)
            writer.writerow(['Цена'])
        try:
            for data in raw_data:
                price = data.find_element(By.XPATH, './/span[@data-testid="price"]').text.replace('руб.', '').strip()
                with open('data_to_df.csv', 'a', newline='', encoding='utf-8-sig') as file:
                    writer = csv.writer(file)
                    writer.writerow([price])
        except Exception as e:
            print(f"Ошибка в ходе записи в файл - {e}")
    except Exception as ex:
        print(f"Ошибка в ходе парсинга цен - {ex}")
    finally:
        print("Закончили упражнение (finally).")
        driver.quit()


get_prices()
