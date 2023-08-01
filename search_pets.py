import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(autouse=True)
def driver():
   driver = webdriver.Chrome()
   # Переходим на страницу авторизации
   driver.get("https://petfriends.skillfactory.ru/login")
   driver.implicitly_wait(10)
   search_element = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')

   yield driver

   driver.quit()


def test_show_my_pets(driver):
   # Вводим email
   driver.find_element(By.ID, 'email').send_keys("juliaa-15@yandex.ru")
   # Вводим пароль
   driver.find_element(By.ID, 'pass').send_keys("123456789")
   # Нажимаем на кнопку входа в аккаунт
   driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   #Нажимаем на кнопку "Мои питомцы"
   driver.find_element(By.XPATH, '//a[@href="/my_pets"]').click()
   WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.TAG_NAME, 'h2'), 'Лютик'))
   # Проверяем, что мы оказались на странице пользователя
   assert driver.find_element(By.TAG_NAME, 'h2').text == "Лютик"
   counts_pets = driver.find_elements(By.CSS_SELECTOR, "tbody>tr")
   counts_pets_user = driver.find_element(By.CSS_SELECTOR, 'div.task3 div')
   amount = counts_pets_user.text.split('\n')
   statistic_pets = amount[1].split(': ')[1]
   assert len(counts_pets) == int(statistic_pets)

def test_photo_my_pets(driver):
   # Вводим email
   driver.find_element(By.ID, 'email').send_keys("juliaa-15@yandex.ru")
   # Вводим пароль
   driver.find_element(By.ID, 'pass').send_keys("123456789")
   # Нажимаем на кнопку входа в аккаунт
   driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   driver.find_element(By.XPATH, '//a[@href="/my_pets"]').click()
   # Проверяем, что мы оказались на странице пользователя
   assert driver.find_element(By.TAG_NAME, 'h2').text == "Лютик"
   pets = driver.find_elements(By.CSS_SELECTOR, 'tbody>tr')
   images = driver.find_elements(By.CSS_SELECTOR, 'img')
   counts_photo_pets = 0
   for i in range(len(pets)):
      if images[i].get_attribute('src') != '':
         counts_photo_pets = counts_photo_pets+1
   counts_pets_user = driver.find_element(By.CSS_SELECTOR, 'div.task3 div')
   amount = counts_pets_user.text.split('\n')
   statistic_pets = amount[1].split(': ')[1]
   half_stat_pets = int(statistic_pets) / 2
   assert counts_photo_pets >= half_stat_pets

def test_all_my_pets(driver):
   # Вводим email
   driver.find_element(By.ID, 'email').send_keys("juliaa-15@yandex.ru")
   # Вводим пароль
   driver.find_element(By.ID, 'pass').send_keys("123456789")
   # Нажимаем на кнопку входа в аккаунт
   driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   driver.find_element(By.XPATH, '//a[@href="/my_pets"]').click()
   # Проверяем, что мы оказались на странице пользователя
   assert driver.find_element(By.TAG_NAME, 'h2').text == "Лютик"
   pets = driver.find_elements(By.CSS_SELECTOR, 'tbody>tr')
   names = driver.find_elements(By.TAG_NAME, 'td')[0::4]
   anymal_types = driver.find_elements(By.TAG_NAME, 'td')[1::4]
   age = driver.find_elements(By.TAG_NAME, 'td')[2::4]
   for i in range(len(pets)):
      assert names[i].text != ''
      assert len(names[i].text) > 0
      assert anymal_types[i].text != ''
      assert len(anymal_types[i].text) > 0
      assert age[i].text != ''
      assert len(age[i].text) > 0

def test_names_my_pets(driver):
   # Вводим email
   driver.find_element(By.ID, 'email').send_keys("juliaa-15@yandex.ru")
   # Вводим пароль
   driver.find_element(By.ID, 'pass').send_keys("123456789")
   # Нажимаем на кнопку входа в аккаунт
   driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   driver.find_element(By.XPATH, '//a[@href="/my_pets"]').click()
   # Проверяем, что мы оказались на странице пользователя
   assert driver.find_element(By.TAG_NAME, 'h2').text == "Лютик"
   pets = driver.find_elements(By.CSS_SELECTOR, 'tbody>tr')
   names = []
   for i in range(len(pets)):
      names.append(pets[i].text.split(' ')[0])
   for i in range(len(names)-1):
      for j in range(i+1, len(names)):
         assert names[i] != names[j]

def test_other_my_pets(driver):
   # Вводим email
   driver.find_element(By.ID, 'email').send_keys("juliaa-15@yandex.ru")
   # Вводим пароль
   driver.find_element(By.ID, 'pass').send_keys("123456789")
   # Нажимаем на кнопку входа в аккаунт
   driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   driver.find_element(By.XPATH, '//a[@href="/my_pets"]').click()
   # Проверяем, что мы оказались на странице пользователя
   assert driver.find_element(By.TAG_NAME, 'h2').text == "Лютик"
   pets = driver.find_elements(By.CSS_SELECTOR, 'tbody>tr')
   for i in range(len(pets)-1):
      for j in range(i+1, len(pets)):
         assert pets[i].text != pets[j].text
