import requests


def get_bib(doi: str) -> str:
    url = f"https://citation-needed.springer.com/v2/references/{doi}"
    params = {"format": "bibtex", "flavour": "citation"}
    r = requests.get(url, params=params)
    r.encoding = "utf-8"
    return r.text.strip()


if __name__ == "__main__":
    print(get_bib(input("Enter Springer DOI:")))
