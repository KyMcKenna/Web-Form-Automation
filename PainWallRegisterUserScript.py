from selenium import webdriver
import pandas as pd
import time

df = pd.read_excel('painwallmembers.xlsx')

driver = webdriver.chrome.webdriver.WebDriver(executable_path=r"C:\Users\thelegendofky\Downloads\chromedriver_win32\chromedriver.exe")

driver.get("https://www.thepainwall.com/membership-join/")

time.sleep(3)


for i in df.index:
    entry = df.loc[i]

    join_btn = driver.find_element_by_xpath('//*[@id="1516"]')
    join_btn.click()

    time.sleep(10)

    Email_input = (entry['Emails'])
    mail = driver.find_element_by_xpath('//*[@id="email"]')
    mail.send_keys(Email_input)

    Card_input = (entry['CardNo'])
    card = driver.find_element_by_xpath('//*[@id="cardNumber"]')
    card.send_keys(str(Card_input))
 
    Expire_input = (entry['Expire'])
    expiration = driver.find_element_by_xpath('//*[@id="cardExpiry"]')
    expiration.send_keys(str(Expire_input))

    Cvc_input = (entry['Security'])
    cvc = driver.find_element_by_xpath('//*[@id="cardCvc"]')
    cvc.send_keys(str(Cvc_input))

    NameOnCard_input = (entry['CustName'])
    name = driver.find_element_by_xpath('//*[@id="billingName"]')
    name.send_keys(NameOnCard_input)

    Zip_input = (entry['Zips'])
    areacode = driver.find_element_by_xpath('//*[@id="billingPostalCode"]')
    areacode.send_keys(str(Zip_input))

    time.sleep(4)

    submit_btn = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/form/div[2]/div[4]/button/div[3]')
    submit_btn.click()

    time.sleep(15)

    get_confirmation = driver.find_element_by_css_selector('.fusion-text.fusion-text-1')
    print(get_confirmation.text)
    if ((get_confirmation.text) == "Join the pain wall army today!"):
        print ('Customer was added')
    else:
        print ('Customer was unable to be added')

    time.sleep(5)