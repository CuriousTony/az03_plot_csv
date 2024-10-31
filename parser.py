from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def get_prices():
    page = 'https://www.divan.ru/sankt-peterburg/category/pramye-divany'
    driver = webdriver.Chrome()
    print('Начинаем упражнение')
    driver.get(page)

    try:
        WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.CLASS_NAME, 'WdR1o')))
        raw_data = driver.find_elements(By.CLASS_NAME, 'WdR1o')
        for data in raw_data:
            price = data.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU.KIkOH').text
            print(price)

    except Exception as e:
        print(f"Ошибка в селекторах - {e}")

    finally:
        print("Закончили упражнение (finally).")
        driver.quit()


get_prices()
