from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture()
def driver():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.maximize_window()
    yield browser
    browser.close()


@pytest.mark.parametrize(
    'creds',
    [
        ('user1@mail.com', 'asasas'),
        ('user2@mail.com', 'qwqwqw'),
        ('user3@mail.com', 'lmlmlm')
    ]
)
def test_login(driver, creds):
    login, passw = creds
    driver.get('https://magento.softwaretestingboard.com/customer/account/login')
    driver.find_element(By.ID, 'email').send_keys(login)
    driver.find_element(By.ID, 'pass').send_keys(passw)
    driver.find_element(By.ID, 'send2').click()
    error_text = driver.find_element(By.CSS_SELECTOR, '[data-ui-id="message-error"]').text
    assert (
        'The account sign-in was incorrect or your account is disabled temporarily. '
        'Please wait and try again later.'
        == error_text
    )
