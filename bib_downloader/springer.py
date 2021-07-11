import requests


def download_bib(doi: str) -> str:
    url = f"https://citation-needed.springer.com/v2/references/{doi}"
    params = {"format": "bibtex", "flavour": "citation"}
    r = requests.get(url, params=params)
    return r.text.strip()


if __name__ == "__main__":
    print("Enter Springer DOI:")
    print(download_bib(input()))
