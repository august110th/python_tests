import requests

class NewFolder:

    def __init__(self, token: str):
        self.token = token
        self.headers = {"Authorization": f"OAuth {self.token}"}
        self.params = {"path": "new_folder"}

    def folder_create(self, path: str):
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        response = requests.put(url, params=self.params, headers=self.headers)
        return response.status_code

    def folder_check(self, path):
        response = requests.get("https://cloud-api.yandex.net/v1/disk/resources",
        params={'path': path}, headers=self.headers)
        return response.status_code

token = "***************************************"

if __name__ == "__main__":
    nf = NewFolder(token)
    print(nf.folder_create("new_folder"))
    print(nf.folder_check("new_folder"))