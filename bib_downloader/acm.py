import requests
import tempfile
import json
import citeproc  # type: ignore
import html
from typing import Dict


def download_bib(doi: str) -> Dict:
    url = "https://dl.acm.org/action/exportCiteProcCitation"
    payload = {"dois": doi, "targetFile": "custom-bibtex", "format": "bibTex"}
    r = requests.post(url, data=payload)
    r.encoding = "utf-8"
    return json.loads(r.text.strip())


def format_bib(resp: Dict) -> str:
    style = resp["style"]
    items = [list(e.values())[0] for e in resp["items"]]
    # HACK: Make type lower case to avoid issues with case-sensitive string
    # comparison
    for item in items:
        item["type"] = item["type"].lower()
    bib_source = citeproc.source.json.CiteProcJSON(items)
    with tempfile.NamedTemporaryFile("w") as f:
        f.write(style)
        f.flush()
        bib_style = citeproc.CitationStylesStyle(f.name, validate=False)
        bib = citeproc.CitationStylesBibliography(
            bib_style, bib_source, citeproc.formatter.plain
        )
        for item in items:
            citation = citeproc.Citation([citeproc.CitationItem(item["id"])])
            bib.register(citation)
        return "\n".join([str(item) for item in bib.bibliography()])


def get_bib(doi: str) -> str:
    resp = download_bib(doi)
    return format_bib(resp)


if __name__ == "__main__":
    print(get_bib(input("Enter ACM DOI:")))
