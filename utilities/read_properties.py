import configparser

config = configparser.RawConfigParser()
config.read(r".\Configuration\config.ini")


class ReadConfig:

    @staticmethod
    def get_url():
        url = config.get('common info', 'base_url')
        return url

    @staticmethod
    def get_username():
        username = config.get('common info', 'raw_username')
        return username

    @staticmethod
    def get_password():
        password = config.get('common info', 'raw_password')
        return password

