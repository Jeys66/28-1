Итоговый проект по тестированию сайта "Ростелеком": https://b2c.passport.rt.ru.

Содержит UI тесты страницы Авторизации.
В проекте были использованы шаблоны PageObject с Selenium и PyTest (Python)

В папке pages:

           base.py - содержит библиотеку Smart Page Object

           auth_page.py - содержит класс для страницы "Авторизация"

           auth_page_with_code.py - содержит класс для страницы "Авторизация с временным кодом"

           elements.py - содержит класс для определения элементов на веб-страницах

           register_page.py - содержит класс для страницы "Регистрация"
           
Тесты собраны в Файле: test_rostel.py  
Требуемые библиотеки в файле requirements.txt.

тесты запускаются из терминала командой: 
pytest -v --driver Chrome --driver-path chromedriver.exe test_rostel.py
