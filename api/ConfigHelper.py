import os
import configparser


class ConfigHelper:

    config: configparser

    def __init__(self):
        # Получаем абсолютный путь к текущему скрипту
        current_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

        # Собираем путь к файлу config.ini

        config_file = 'config.ini'
        config_path = os.path.join(current_dir, 'configs', config_file)

        self.config = configparser.ConfigParser()
        self.config.read(config_path)
