# Abre esto en la consola:
import configparser
config = configparser.ConfigParser()
config.read('alembic.ini', encoding='utf-8')
print(config['alembic']['sqlalchemy.url'])