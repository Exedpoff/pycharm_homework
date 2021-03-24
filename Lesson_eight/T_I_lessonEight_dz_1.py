import re

def parser_email(e_address):
    r_mail = re.compile(r'(?P<username>([\w]+))@(?P<domain>[^&]+\.\w+)')
    if not r_mail.match(e_address):
        raise ValueError(f'Ошибочный email:{e_address}')
    print(r_mail.match(e_address).groupdict())


try:
    parser_email('someone@geekbrains.ru')
    parser_email('som$eone@mailru')
except ValueError as error:
    print(error)
