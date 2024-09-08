
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.medica-tradefair.com/vis/v1/en/search?ticket=g_u_e_s_t&_query=&f_type=profile")
# time.sleep(1)
# max_pages = 315
# page_no = 0
# scroll_no = 0
# current_scroll_page = 1


# while page_no < max_pages:

#     page_no += 1

#     while scroll_no < current_scroll_page:
#         scroll_no += 1
#         body = driver.find_element(By.TAG_NAME, 'body')
#         body.send_keys(Keys.END)
#         time.sleep(2)

#     for i in range(1, 21):

        # wait = WebDriverWait(driver, 10)
        # list_item = wait.until(EC.presence_of_element_located(
        #     (By.XPATH, f"//*[@id='vis-search-scroll-area']/div[{page_no}]/div[{i}]/a/div/div[2]/div/h3")))

        # action_chains = ActionChains(driver)
        # action_chains.key_down(Keys.CONTROL).click(list_item).key_up(Keys.CONTROL).perform()

        # # Switch to the newly opened tab
        # driver.switch_to.window(driver.window_handles[-1])
        # time.sleep(2)

        # wait = WebDriverWait(driver, 10)
        # item_data = wait.until(EC.presence_of_element_located(
        #     (By.XPATH, "//*[@id='finder-profile']/div/div/section/div/div/div[2]/div[5]/button/div/span")))

        # driver.execute_script("arguments[0].click();", item_data)

        # time.sleep(2)

        name_text = ""
        country_text = ""
        email_text = ""
        number_text = ""
        business_area_text = ""
        website_text = ""

        try:
            name = driver.find_element(By.XPATH, value="//*[@id='profile-title']/h1")
            name_text = name.text
        except:
            pass

        try:
            country = driver.find_element(By.XPATH, value="//*[@id='profile-business-data']/div[1]/div[1]/div/div[2]")
            country_text = country.text
        except:
            pass

        try:
            email = driver.find_element(By.XPATH, value="//*[@id='profile-business-data']/div[1]/div[2]/div[1]/div[1]")
            email_text = email.text
        except:
            pass

        try:
            number = driver.find_element(By.XPATH, value="//*[@id='profile-business-data']/div[1]/div[2]/div[1]/div[2]")
            number_text = number.text
        except:
            pass

        try:
            business_area = driver.find_element(By.XPATH, value="//*[@id='profile-business-data']/div[2]/div/table/tbody/tr[3]/td[2]")
            business_area_text = business_area.text
        except:
            pass

        try:
            website = driver.find_element(By.XPATH, value="//*[@id='profile-business-data']/div[1]/div[2]/div[1]/div[3]/div[2]/ul/li/a")
            website_text = website.text
        except:
            pass

        #opening google form
        driver.execute_script("window.open('https://docs.google.com/forms/d/e/1FAIpQLSeABXtU62XVghsKuVzW-aGOazLQE4Rt-Ub8ZOkKbOosAOrTnw/viewform', '_blank');")

        # Switch to the Google Form tab
        driver.switch_to.window(driver.window_handles[-1])

        time.sleep(3)

        company_name = driver.find_element(By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
        company_name.send_keys(name_text)

        company_country = driver.find_element(By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
        company_country.send_keys(country_text)

        company_category = driver.find_element(By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea")
        company_category.send_keys(business_area_text)

        company_number = driver.find_element(By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input")
        company_number.send_keys(number_text)

        company_email = driver.find_element(By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input")
        company_email.send_keys(email_text)

        company_website = driver.find_element(By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input")
        company_website.send_keys(website_text)

        submit = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div")))

        submit.send_keys(Keys.ENTER)

        driver.close()

        driver.switch_to.window(driver.window_handles[-1])
        driver.close()

        driver.switch_to.window(driver.window_handles[0])

        time.sleep(1)

        print(f"page No. {page_no}")

    # current_scroll_page = 2
