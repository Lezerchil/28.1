import pytest
import pdb
import requests
import requests_toolbelt
import pytest_selenium
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from requests_toolbelt.multipart.encoder import MultipartEncoder
from settings import driverfolder, site, telnum, email, login, ls, password_telnum, password_email, password_login, password_ls, redirect_uri
from settings import bad_email, bad_telnum, bad_login, bad_ls, bad_password_telnum, bad_password_email, bad_password_login, bad_password_ls
from settings import expected_class

@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome(driverfolder)
    pytest.driver.get(site)
    yield
    pytest.driver.quit()


def test_by_number():
    WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.ID, "t-btn-tab-phone"))).click()
    #pytest.driver.find_element(By.ID, 't-btn-tab-phone')
    pytest.driver.find_element(By.ID, 'username').clear()
    pytest.driver.find_element(By.ID, 'username').send_keys(telnum)
    pytest.driver.find_element(By.ID, 'password').clear()
    pytest.driver.find_element(By.ID, 'password').send_keys(password_telnum)
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    assert WebDriverWait(pytest.driver, 10).until(ec.url_to_be(redirect_uri))

def test_by_number_bad():
    WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.ID, "t-btn-tab-phone"))).click()
    #pytest.driver.find_element(By.ID, 't-btn-tab-phone')
    pytest.driver.find_element(By.ID, 'username').clear()
    pytest.driver.find_element(By.ID, 'username').send_keys(bad_telnum)
    pytest.driver.find_element(By.ID, 'password').clear()
    pytest.driver.find_element(By.ID, 'password').send_keys(bad_password_telnum)
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    assert WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located(By.CLASS_NAME, "rt-link rt-link--orange rt-link--muted login-form__forgot-pwd login-form__forgot-pwd--muted"))


def test_by_email():
    WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.ID, "t-btn-tab-mail"))).click()
    #pytest.driver.find_element_by_id('t-btn-tab-mail').click()
    pytest.driver.find_element(By.ID, 'username').clear()
    pytest.driver.find_element(By.ID, 'username').send_keys(email)
    pytest.driver.find_element(By.ID, 'password').clear()
    pytest.driver.find_element(By.ID, 'password').send_keys(password_email)
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    assert WebDriverWait(pytest.driver, 10).until(ec.url_to_be(redirect_uri))

def test_by_email_bad():
    WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.ID, "t-btn-tab-mail"))).click()
    #pytest.driver.find_element_by_id('t-btn-tab-mail').click()
    pytest.driver.find_element(By.ID, 'username').clear()
    pytest.driver.find_element(By.ID, 'username').send_keys(bad_email)
    pytest.driver.find_element(By.ID, 'password').clear()
    pytest.driver.find_element(By.ID, 'password').send_keys(bad_password_email)
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    assert expected_class == WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.CLASS_NAME, expected_class)))

def test_by_login():
    WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.ID, "t-btn-tab-login"))).click()
    #pytest.driver.find_element_by_id('t-btn-tab-login').click()
    pytest.driver.find_element(By.ID, 'username').clear()
    pytest.driver.find_element(By.ID, 'username').send_keys(login)
    pytest.driver.find_element(By.ID, 'password').clear()
    pytest.driver.find_element(By.ID, 'password').send_keys(password_login)
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    assert WebDriverWait(pytest.driver, 10).until(ec.url_to_be(redirect_uri))

def test_by_login_bad():
    WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.ID, "t-btn-tab-login"))).click()
    #pytest.driver.find_element_by_id('t-btn-tab-login').click()
    pytest.driver.find_element(By.ID, 'username').clear()
    pytest.driver.find_element(By.ID, 'username').send_keys(bad_login)
    pytest.driver.find_element(By.ID, 'password').clear()
    pytest.driver.find_element(By.ID, 'password').send_keys(bad_password_login)
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    assert expected_class == WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located(By.CLASS_NAME, expected_class))

def test_by_ls():
    WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.ID, "t-btn-tab-ls"))).click()
    #pytest.driver.find_element_by_id('t-btn-tab-ls').click()
    pytest.driver.find_element(By.ID, 'username').clear()
    pytest.driver.find_element(By.ID, 'username').send_keys(ls)
    pytest.driver.find_element(By.ID, 'password').clear()
    pytest.driver.find_element(By.ID, 'password').send_keys(password_ls)
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    assert WebDriverWait(pytest.driver, 10).until(ec.url_to_be(redirect_uri))

def test_by_ls_bad():
    WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.ID, "t-btn-tab-ls"))).click()
    #pytest.driver.find_element_by_id('t-btn-tab-ls').click()
    pytest.driver.find_element(By.ID, 'username').clear()
    pytest.driver.find_element(By.ID, 'username').send_keys(bad_ls)
    pytest.driver.find_element(By.ID, 'password').clear()
    pytest.driver.find_element(By.ID, 'password').send_keys(bad_password_ls)
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    assert expected_class == WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located(By.CLASS_NAME, expected_class))

#Авторизация по временному коду (Где она?)

