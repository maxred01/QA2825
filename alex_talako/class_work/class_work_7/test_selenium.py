import time
from os import times_result
from re import search

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_selenium():
    driver = webdriver.Chrome()
    driver.get('https://tryhackme.com/')
    driver.maximize_window()
    driver.find_element(By.XPATH, '//button[@class="sc-jEACwC hnVovF sc-gqteRq ctqrBQ"]').click()
    time.sleep(3)
    driver.execute_script("""
        Array.from(document.querySelectorAll('*')).find(el => 
            ['auto','scroll'].includes(getComputedStyle(el).overflowY)
        )?.scrollBy(0,1300);
    """)
    time.sleep(3)


    learn_button = driver.find_element(By.XPATH, '//*[@aria-label="Navigate to Learn page"]')
    assert learn_button.is_displayed(), 'Элемент отсутствует'
    assert learn_button.is_enabled(), 'Элемент не кликабелен'
    assert learn_button.text == 'Learn', f"Неверный текст. Получено {learn_button}"
    learn_button.click()
    time.sleep(3)
    driver.execute_script("""
        Array.from(document.querySelectorAll('*')).find(el => 
            ['auto','scroll'].includes(getComputedStyle(el).overflowY)
        )?.scrollBy(0,1600);
    """)
    time.sleep(3)
    driver.execute_script("""
        Array.from(document.querySelectorAll('*')).find(el => 
            ['auto','scroll'].includes(getComputedStyle(el).overflowY)
        )?.scrollBy(0,-1600);
    """)
    time.sleep(3)

    paths_button = driver.find_element(By.XPATH, '(//*[@aria-selected="false"])[1]')
    assert paths_button.is_displayed(),'Элемент отсутствует'
    assert paths_button.is_enabled(),'Элемент не кликабелен'
    assert paths_button.text == 'Paths',f"Неверный текст. Получено {paths_button}"
    paths_button.click()
    time.sleep(3)
    driver.execute_script("""
            Array.from(document.querySelectorAll('*')).find(el => 
                ['auto','scroll'].includes(getComputedStyle(el).overflowY)
            )?.scrollBy(0,500);
        """)
    time.sleep(3)
    driver.execute_script("""
            Array.from(document.querySelectorAll('*')).find(el => 
                ['auto','scroll'].includes(getComputedStyle(el).overflowY)
            )?.scrollBy(0,-500);
        """)
    time.sleep(3)

    modules_button = driver.find_element(By.XPATH, '(//*[@aria-selected="false"])[2]')
    assert modules_button.is_displayed(),'Элемент отсутствует'
    assert modules_button.is_enabled(),'Элемент кликабелен'
    assert modules_button.text == 'Modules',f"Неверный текст. Получено {modules_button}"
    modules_button.click()
    time.sleep(3)
    driver.execute_script("""
              Array.from(document.querySelectorAll('*')).find(el => 
                  ['auto','scroll'].includes(getComputedStyle(el).overflowY)
              )?.scrollBy(0,500);
          """)
    time.sleep(3)
    driver.execute_script("""
              Array.from(document.querySelectorAll('*')).find(el => 
                  ['auto','scroll'].includes(getComputedStyle(el).overflowY)
              )?.scrollBy(0,-500);
          """)
    time.sleep(3)


    walkthroughs_button = driver.find_element(By.XPATH, '//*[@aria-orientation="horizontal"]/*[4]')
    assert walkthroughs_button.is_displayed(),'Элемент отсутствует'
    assert walkthroughs_button.is_enabled(),'Элемент не кликабелен'
    assert walkthroughs_button.text == 'Walkthroughs', f"Неверный текст. Получено {walkthroughs_button}"
    walkthroughs_button.click()
    time.sleep(3)
    driver.execute_script("""
              Array.from(document.querySelectorAll('*')).find(el => 
                  ['auto','scroll'].includes(getComputedStyle(el).overflowY)
              )?.scrollBy(0,500);
          """)
    time.sleep(3)
    driver.execute_script("""
              Array.from(document.querySelectorAll('*')).find(el => 
                  ['auto','scroll'].includes(getComputedStyle(el).overflowY)
              )?.scrollBy(0,-500);
          """)
    time.sleep(3)


    networks_button = driver.find_element(By.XPATH, '//*[@aria-orientation="horizontal"]/*[5]')
    assert networks_button.is_displayed(),'Элемент отсутствует'
    assert networks_button.is_enabled(),'Элемент не кликабелен'
    assert networks_button.text == 'Networks', f"Неверный текст. Получено {networks_button}"
    networks_button.click()
    time.sleep(3)
    driver.execute_script("""
              Array.from(document.querySelectorAll('*')).find(el => 
                  ['auto','scroll'].includes(getComputedStyle(el).overflowY)
              )?.scrollBy(0,500);
          """)
    time.sleep(3)
    driver.execute_script("""
              Array.from(document.querySelectorAll('*')).find(el => 
                  ['auto','scroll'].includes(getComputedStyle(el).overflowY)
              )?.scrollBy(0,-500);
          """)
    time.sleep(3)


    practice_button = driver.find_element(By.XPATH, '//*[@aria-label="Toggle dropdown for Practice"]')
    assert practice_button.is_displayed(), 'Элемент отсутствует'
    assert practice_button.is_enabled(), 'Элемент не кликабелен'
    assert practice_button.text == 'Practice', f"Неверный текст. Получено {practice_button}"
    practice_button.click()
    time.sleep(3)


    challenges_button = driver.find_element(By.XPATH, '(//*[@data-testid="splitScreenMiddle"]//*[@type="main"])[1]')
    assert challenges_button.is_displayed(),'Элемент отсутствует'
    assert challenges_button.is_enabled(),'Элемент не кликабелен'
    assert challenges_button.text == 'Challenges\nReinforce your learning', f"Неверный текст. Получено {challenges_button}"
    challenges_button.click()
    time.sleep(3)
    driver.execute_script("""
            Array.from(document.querySelectorAll('*')).find(el => 
                ['auto','scroll'].includes(getComputedStyle(el).overflowY)
            )?.scrollBy(0,500);
        """)
    time.sleep(3)
    driver.execute_script("""
            Array.from(document.querySelectorAll('*')).find(el => 
                ['auto','scroll'].includes(getComputedStyle(el).overflowY)
            )?.scrollBy(0,-500);
        """)
    time.sleep(3)


    compete_button = driver.find_element(By.XPATH, '//*[@aria-label="Toggle dropdown for Compete"]')
    assert compete_button.is_displayed(), 'Элемент отсутствует'
    assert compete_button.is_enabled(), 'Элемент не кликабелен'
    assert compete_button.text == 'Compete', f"Неверный текст. Получено {compete_button}"
    compete_button.click()
    time.sleep(3)

    compete_king_button = driver.find_element(By.XPATH,'(//*[@type="main"])[1]')
    assert compete_king_button.is_displayed(),'Элемент отсутствует'
    assert compete_king_button.is_enabled(), 'Элемент не кликабелен'
    assert compete_king_button.text, 'King of the Hill\nAttack & Defend'
    compete_king_button.click()
    time.sleep(3)
    driver.execute_script("""
                Array.from(document.querySelectorAll('*')).find(el => 
                    ['auto','scroll'].includes(getComputedStyle(el).overflowY)
                )?.scrollBy(0,500);
            """)
    time.sleep(3)
    driver.execute_script("""
                Array.from(document.querySelectorAll('*')).find(el => 
                    ['auto','scroll'].includes(getComputedStyle(el).overflowY)
                )?.scrollBy(0,-500);
            """)
    time.sleep(3)


    education_button = driver.find_element(By.XPATH, '//*[@aria-label="Toggle dropdown for Education"]')
    assert education_button.is_displayed(), 'Элемент отсутствует'
    assert education_button.is_enabled(), 'Элемент не кликабелен'
    assert education_button.text == 'Education', f"Неверный текст. Получено {education_button}"
    education_button.click()
    time.sleep(3)

    teaching_button = driver.find_element(By.XPATH,'(//*[@data-testid="splitScreenMiddle"]//*[@type="main"])[1]')
    assert teaching_button.is_displayed(),'Элемент отсутствует'
    assert teaching_button.is_enabled(),'Элемент не кликабелен'
    assert teaching_button.text =='Teaching\nUse our security labs',f"Неверный текст. Получено {teaching_button}"
    teaching_button.click()
    time.sleep(3)
    driver.execute_script("""
                    Array.from(document.querySelectorAll('*')).find(el => 
                        ['auto','scroll'].includes(getComputedStyle(el).overflowY)
                    )?.scrollBy(0,600);
                """)
    time.sleep(3)
    driver.execute_script("""
                    Array.from(document.querySelectorAll('*')).find(el => 
                        ['auto','scroll'].includes(getComputedStyle(el).overflowY)
                    )?.scrollBy(0,-600);
                """)
    time.sleep(3)


    business_button = driver.find_element(By.XPATH, '//*[@aria-label="Navigate to Business page"]')
    assert business_button.is_displayed(), 'Элемент отсутствует'
    assert business_button.is_enabled(), 'Элемент не кликабелен'
    assert business_button.text == 'Business', f"Неверный текст. Получено {business_button}"
    business_button.click()
    time.sleep(3)
    driver.execute_script("""
                    Array.from(document.querySelectorAll('*')).find(el => 
                        ['auto','scroll'].includes(getComputedStyle(el).overflowY)
                    )?.scrollBy(0,700);
                """)
    time.sleep(3)
    driver.execute_script("""
                    Array.from(document.querySelectorAll('*')).find(el => 
                        ['auto','scroll'].includes(getComputedStyle(el).overflowY)
                    )?.scrollBy(0,-700);
                """)
    time.sleep(3)


    pricing_button = driver.find_element(By.XPATH, '//*[@aria-label="Navigate to Pricing page"]')
    assert pricing_button.is_displayed(), 'Элемент отсутствует'
    assert pricing_button.is_enabled(), 'Элемент не кликабелен'
    assert pricing_button.text == 'Pricing', f"Неверный текст. Получено {pricing_button}"
    pricing_button.click()
    time.sleep(3)


    search_button = driver.find_element(By.XPATH, '//*[@data-testid="search-btn"]')
    assert search_button.is_displayed(), 'Элемент отсутствует'
    assert search_button.is_enabled(), 'Элемент не кликабелен'
    assert search_button.text == '', f"Неверный текст. Получено {search_button}"
    search_button.click()
    driver.find_element(By.XPATH, '//*[@data-testid="search-input"]').send_keys('kali')
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@data-testid="search-input"]').send_keys(Keys.ENTER)
    time.sleep(4)
    driver.execute_script("""
                    Array.from(document.querySelectorAll('*')).find(el => 
                        ['auto','scroll'].includes(getComputedStyle(el).overflowY)
                    )?.scrollBy(0,500);
                """)
    time.sleep(3)
    driver.find_element(By.XPATH, '(//*[@data-testid="new-content"]//a)[1]').click()
    time.sleep(3)


    authorization_button = driver.find_element(By.XPATH, '(//*[@data-link="outlined"])[2]')
    assert authorization_button.is_displayed(), 'Элемент отсутствует'
    assert authorization_button.is_enabled(), 'Элемент не кликабелен'
    assert authorization_button.text == 'Log In', f"Неверный текст. Получено {authorization_button}"
    authorization_button.click()
    time.sleep(3)


    join_button = driver.find_element(By.XPATH, '//*[@data-link="join"]')
    assert join_button.is_displayed(), 'Элемент отсутствует'
    assert join_button.is_enabled(), 'Элемент не кликабелен'
    assert join_button.text == 'Join for FREE', f"Неверный текст. Получено {join_button}"
    join_button.click()
    time.sleep(3)

    driver.close()
    driver.quit()


