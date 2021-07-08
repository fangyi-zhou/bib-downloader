import requests
import tempfile
import json
import citeproc
import html


def download_bib(doi):
    url = "https://dl.acm.org/action/exportCiteProcCitation"
    payload = {"dois": doi, "targetFile": "custom-bibtex", "format": "bibTex"}
    r = requests.post(url, data=payload)
    print()
    bib = json.loads(r.text.strip())
    style = html.unescape(bib["style"])
    print(style)
    items = [list(e.values())[0] for e in bib["items"]]
    bib_source = citeproc.source.json.CiteProcJSON(items)
    with tempfile.TemporaryFile("w") as f:
        f.write(style)
        bib_style = citeproc.CitationStylesStyle(f.name)
        bib = citeproc.CitationStylesBibliography(
            bib_style, bib_source, citeproc.formatter.plain
        )
        for item in bib.bibliography():
            print(str(item))


if __name__ == "__main__":
    print("Enter ACM DOI:")
    download_bib(input())
