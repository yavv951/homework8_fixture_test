# homework8_fixture_test

Задание:

● Написать параметризированный тест с помощью PyTest, который проверяет, что входной список email является корректными email. Пример корректных email 'test@test.ru', 'w@w.com', '123QWE@mmm.mmm’.
● Написать параметризированный тест с помощью PyTest, который проверяет, что входной список email является некорректными email. Пример некорректных email'test@test.', 'w@', '@tt’.
● Сделать фикстуру, которая передает имя файла, в который будут писаться результаты тестов (например 1 или 0, на ваше усмотрение )
● Имя файла задается в ini файле, дефолтное значение ‘log.txt’

Установка и запуск тестов:

1. Установите все пакеты командой pip install requirements.txt
2. Запустите тесты командой pytest
