# api_01_sms

API 01 sms - скрипт для отправки сообщения на номер телефона указанный в настройках, о появившемся пользователе в социальной сети вконтакте в online. 
Запускаем скрипт, вводим id пользователя, которого хотите поймать в онлайне, как только пользователь появится в сети, вам поступит смс уведомление. Скрип проверяет статус каждые 5 сенкунд.

- python 3.9
- Для доступа к переменным установите через pip библиотеку dotenv: pip install python-dotenv
- Затем импортируйте и выполните функцию load_dotenv :
		import os
		from dotenv import load_dotenv 
		load_dotenv()
		
		Пример: token = os.getenv('Token')
- TWILIO_ACCOUNT_SID - sid аккаунта
- TWILIO_AUTH_TOKEN -токен
- NUMBER_TO - телефон на который посылаете сообщение
- NUMBER_FROM - телефон с которго приходит сообщение
- Зарегистрироваться в сервисе https://twilio.com
