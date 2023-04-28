import configparser

from data_provider import paths


def get_url():
    config = configparser.ConfigParser()
    config.read(paths.get_project_path() + '/configs/configurations.properties')
    return config.get('URLSection', 'base_Url')

