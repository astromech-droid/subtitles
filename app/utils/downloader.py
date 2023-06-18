import requests


def download_subs(url: str, path: str):
    response = requests.get(url)

    if response.status_code == 200:
        with open(path, "w") as f:
            f.write(response.text)

    return path
