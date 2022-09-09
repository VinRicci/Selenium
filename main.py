from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = Chrome('./chromedriver_win32/chromedriver.exe')
driver.maximize_window()
driver.get('https://forms.office.com/pages/responsepage.aspx?id=nVR4D-w-r0O1am97BC'
           '1smtp9krqPskJEt3c5INQR-RJURTU0RzNBN0JOMk5ZSFFaVjZUMjNBUVdMRC4u')
WebDriverWait(driver, 20).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
time.sleep(3)
driver.find_element(By.XPATH, '/html/body/div/div/div/div/div[1]/div/div[1]/'
                              'div[2]/div[2]/div[1]/div/div[3]/div/div/input').send_keys("1541218")
WebDriverWait(driver, 20).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
time.sleep(3)
driver.find_element(By.XPATH, '/html/body/div/div/div/div/div[1]/div/div[1]/div[2]'
                              '/div[2]/div[2]/div/div[3]/div/div/input').send_keys("Vinicio de la Cruz Ricci")
WebDriverWait(driver, 20).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
time.sleep(3)
driver.find_element(By.XPATH, '/html/body/div/div/div/div/div[1]/div/div[1]/div[2]'
                              '/div[2]/div[3]/div/div[3]/div/div/input').send_keys("vdelacruzr@correo.url.edu.gt")
WebDriverWait(driver, 20).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
time.sleep(3)
driver.find_element(By.XPATH, '/html/body/div/div/div/div/div[1]/div/div[1]'
                              '/div[2]/div[2]/div[4]/div/div[3]/div/div/input').send_keys("vinicioricci@gmail.com")
WebDriverWait(driver, 20).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
time.sleep(3)
elemclick = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div[1]/div/'
                                          'div[1]/div[2]/div[2]/div[5]/div/div[3]/div/div[3]/div/label/input').click()
WebDriverWait(driver, 20).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
time.sleep(3)
driver.find_element(By.XPATH, '/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/'
                              'div[2]/div[6]/div/div[3]/div/div[1]/div/label/input').click()
WebDriverWait(driver, 20).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
time.sleep(3)
driver.find_element(By.XPATH, '/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/'
                              'div[2]/div[7]/div/div[3]/div/div[17]/div/label/input').click()
WebDriverWait(driver, 20).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
time.sleep(3)
driver.find_element(By.XPATH, '/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]'
                              '/div[8]/div/div[3]/div/div[2]/div/label/input').click()
WebDriverWait(driver, 20).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
time.sleep(3)
driver.find_element(By.XPATH, '/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/div[4]/div[1]/button/div').click()
WebDriverWait(driver, 20).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
time.sleep(3)
