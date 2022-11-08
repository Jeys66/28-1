import time
from pages.auth_page import AuthPage
from pages.register_page import MainPage
from pages.auth_page_with_code import AuthPageWithCode
from config import TestData



def test_RT02_page_all_items(web_browser):
    page = AuthPage(web_browser)
    page.wait_page_loaded()

    assert page.email.is_presented()
    assert page.password.is_presented()
    assert page.btn.is_presented()
    assert page.registration_btn.is_presented()
    assert page.forgot_password_btn.is_presented()
    assert page.tab_email.is_clickable()
    assert page.tab_login.is_clickable()
    assert page.tab_phone.is_clickable()
    assert page.tab_ls.is_clickable()


def test_RT03_authorisation_phone(web_browser):
    page = AuthPage(web_browser)
    page.wait_page_loaded()
    page.email.send_keys(TestData.valid_phone)
    page.password.send_keys(TestData.password2)

    page.btn.click()

    assert 'https://b2c.passport.rt.ru/account_b2c/page' in page.get_current_url()


def test_RT05_authorisation_phone(web_browser):
    page = AuthPage(web_browser)
    page.wait_page_loaded()
    page.email.send_keys(TestData.valid_phone)
    page.password.send_keys(TestData.empty_password)
    page.btn.click()

    assert 'https://b2c.passport.rt.ru/account_b2c/page' not in page.get_current_url()


def test_RT06_authorisation_email(web_browser):
    page = AuthPage(web_browser)
    page.wait_page_loaded()
    page.email.send_keys(TestData.valid_email)
    page.password.send_keys(TestData.password2)
    page.btn.click()

    assert 'https://b2c.passport.rt.ru/account_b2c/page' in page.get_current_url()


def test_RT07_authorisation_email(web_browser):
    page = AuthPage(web_browser)
    page.wait_page_loaded()
    page.email.send_keys(TestData.invalid_email)
    page.password.send_keys(TestData.password2)

    page.btn.click()

    assert 'https://b2c.passport.rt.ru/account_b2c/page' not in page.get_current_url()


def test_RT12_authorisation_with_code(web_browser):
    page = AuthPageWithCode(web_browser)
    page.wait_page_loaded()
    page.email.send_keys(TestData.valid_email)
    page.btn_code.click()
    time.sleep(5)

    assert page.code0.is_presented()
    assert page.code1.is_presented()
    assert page.code2.is_presented()
    assert page.code3.is_presented()
    assert page.code4.is_presented()
    assert page.code5.is_presented()


def test_RT14_repeat_code_for_authorisation(web_browser):
    page = AuthPageWithCode(web_browser)
    page.wait_page_loaded()
    page.email.send_keys(TestData.valid_email)
    page.btn_code.click()
    time.sleep(125)
    page.repeat_code.click()
    time.sleep(5)

    assert page.timeout_input_code.is_visible()


def test_RT15_password_recovery(web_browser):
    page = AuthPage(web_browser)
    page.wait_page_loaded()
    page.forgot_password_btn.click()
    page.wait_page_loaded()

    assert page.email.is_presented()
    assert page.captcha.is_presented()
    assert page.captcha_input.is_presented()
    assert page.btn_continue.is_presented()


def test_RT25_reset_button(web_browser):
    page = AuthPage(web_browser)
    page.wait_page_loaded()
    page.forgot_password_btn.click()

    assert page.reset_back.is_clickable()

    page.reset_back.click()

    assert 'https://b2c.passport.rt.ru' in page.get_current_url()


def test_RT18_registration(web_browser):
    page = MainPage(web_browser)
    page.wait_page_loaded()
    page.registration_btn.click()

    page.first_name_input.send_keys(TestData.first_name1)
    page.last_name_input.send_keys(TestData.last_name1)
    page.email_input.send_keys(TestData.valid_email)
    page.password_input.send_keys(TestData.password1)
    page.password_confirm_input.send_keys(TestData.password1)

    page.register_btn.click()

    assert 'https://b2c.passport.rt.ru/account_b2c/page' in page.get_current_url()


def test_RT19_registration(web_browser):
    page = MainPage(web_browser)
    page.wait_page_loaded()
    page.registration_btn.click()

    page.first_name_input.send_keys(TestData.first_name2)
    page.last_name_input.send_keys(TestData.last_name2)
    page.email_input.send_keys(TestData.valid_email)
    page.password_input.send_keys(TestData.password1)
    page.password_confirm_input.send_keys(TestData.password1)

    page.register_btn.click()

    assert 'https://b2c.passport.rt.ru/account_b2c/page' in page.get_current_url()


def test_RT20_registration_lowercase_password(web_browser):
    page = MainPage(web_browser)
    page.wait_page_loaded()
    page.registration_btn.click()

    page.first_name_input.send_keys(TestData.first_name1)
    page.last_name_input.send_keys(TestData.last_name1)
    page.email_input.send_keys(TestData.valid_email)
    page.password_input.send_keys(TestData.lowercase_password)
    page.password_confirm_input.send_keys(TestData.lowercase_password)

    assert 'https://b2c.passport.rt.ru/account_b2c/page' not in page.get_current_url()
    assert 'Пароль должен содержать хотя бы одну заглавную букву' in page.get_page_source()


def test_RT21_registration_cyrillic_password(web_browser):
    page = MainPage(web_browser)
    page.wait_page_loaded()
    page.registration_btn.click()

    page.first_name_input.send_keys(TestData.first_name1)
    page.last_name_input.send_keys(TestData.last_name1)
    page.email_input.send_keys(TestData.valid_email)
    page.password_input.send_keys(TestData.cyrillic_password)
    page.password_confirm_input.send_keys(TestData.cyrillic_password)

    assert 'https://b2c.passport.rt.ru/account_b2c/page' not in page.get_current_url()
    assert 'Пароль должен содержать только латинские буквы' in page.get_page_source()


def test_RT22_registration_different_passwords(web_browser):
    page = MainPage(web_browser)
    page.wait_page_loaded()
    page.registration_btn.click()

    page.first_name_input.send_keys(TestData.first_name1)
    page.last_name_input.send_keys(TestData.last_name1)
    page.email_input.send_keys(TestData.valid_email)
    page.password_input.send_keys(TestData.password1)
    page.password_confirm_input.send_keys(TestData.password2)
    page.register_btn.click()

    assert 'https://b2c.passport.rt.ru/account_b2c/page' not in page.get_current_url()
    assert 'Пароли не совпадают' in page.get_page_source()


def test_RT23_registration_non_unique_email(web_browser):
    page = MainPage(web_browser)
    page.wait_page_loaded()
    page.registration_btn.click()

    page.first_name_input.send_keys(TestData.first_name1)
    page.last_name_input.send_keys(TestData.last_namee1)
    page.email_input.send_keys(TestData.valid_email)
    page.password_input.send_keys(TestData.password3)
    page.password_confirm_input.send_keys(TestData.password3)
    page.register_btn.click()

    assert 'https://b2c.passport.rt.ru/account_b2c/page' not in page.get_current_url()
    assert 'Учётная запись уже существует' in page.get_page_source()


def test_RT24_registration_short_password(web_browser):
    page = MainPage(web_browser)
    page.wait_page_loaded()
    page.registration_btn.click()

    page.first_name_input.send_keys(TestData.first_name1)
    page.last_name_input.send_keys(TestData.last_name1)
    page.email_input.send_keys(TestData.valid_email)
    page.password_input.send_keys(TestData.short_password)
    page.password_confirm_input.send_keys(TestData.short_password)

    assert 'https://b2c.passport.rt.ru/account_b2c/page' not in page.get_current_url()
    assert 'Длина пароля должна быть не менее 8 символов' in page.get_page_source()
