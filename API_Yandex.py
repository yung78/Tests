import requests


class YaDisk:
    url_newfolder = 'https://cloud-api.yandex.net:443/v1/disk/resources/'

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}

    def new_folder(self):
        headers = self.get_headers()
        params_new_folder = {'path': '/Folder for test'}
        response_new_folder = requests.put(self.url_newfolder, params=params_new_folder, headers=headers)
        return response_new_folder
