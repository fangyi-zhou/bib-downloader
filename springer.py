import requests


def download_bib(doi):
    url = f"https://citation-needed.springer.com/v2/references/{doi}"
    params = {"format": "bibtex", "flavour": "citation"}
    print("Downloading bibtex file from:")
    print(url)
    r = requests.get(url, params=params)
    print()
    print(r.text.strip())


if __name__ == "__main__":
    print("Enter Springer DOI:")
    download_bib(input())
