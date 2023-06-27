from instapy import InstaPy
import random

user = 'gabris.zaza'
password = '123'

session = InstaPy(username=user, password=password)

login_successful = session.login()

if login_successful:
    print("Login bem-sucedido!")
else:
    print("Falha no login. Verifique suas credenciais.")

session.end()