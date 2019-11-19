# Дни 015-021

Общий результат за эти 7 дней: (будет позже)

Пост в блоге: (будет позже)

## День 15 (17.11.2019)

Продолжаю изучать Bottle и в этот раз написал простой API для отправки писем по виду, как, например, у Mailgun. Приложение добавил в папку bottle_api_mail_sender. Проверял его локально и через VDS, запуская через встроенный веб-сервер Bottle. Для использования нужно создать secrets.cfg с данными вида:

```
smtp_address=...
smtp_port=...
sender_email=...
password=...
```

А отправку можно тестить через CURL:

```
$ curl -X POST -F receiver_email=... -F message_subject=... http://host_name/send_mail
```

Специально для удобства тестирования оставил заглушки текста для отправки, если не передавать параметры `message_text` и `message_html`.

Код отправки почты взял полностью с realpython, который ранее уже использовал в [прошлые дни](https://github.com/etoFlash/100-days-of-Python/tree/master/008-014#%D0%B4%D0%B5%D0%BD%D1%8C-11-13112019).

Всего: 01:45

## День 16 (18.11.2019)

Решил Bites of Py (мои решения доступны в моем репозитории https://github.com/etoFlash/bitesofpy):

* [238. Write tests for Fibonacci](https://codechalleng.es/bites/238/)
* [239. Test FizzBuzz](https://codechalleng.es/bites/239/) (добавил в избранное, потом надо будет попробовать сделать с @pytest.mark.parametrize, а не как делал я)

/ 00:50

Доработка add_bites.py в моем репозитории https://github.com/etoFlash/bitesofpy для поддержки тегов для Test Bites.

/ 00:15

Всего: 01:05

## 19.11.2019 пропустил ➡⏭️