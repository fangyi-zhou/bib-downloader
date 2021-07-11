import requests
import tempfile
import json
import citeproc
import html


def download_bib(doi):
    url = "https://dl.acm.org/action/exportCiteProcCitation"
    payload = {"dois": doi, "targetFile": "custom-bibtex", "format": "bibTex"}
    r = requests.post(url, data=payload)
    return json.loads(r.text.strip())


def format_bib(resp):
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


if __name__ == "__main__":
    print("Enter ACM DOI:")
    resp = download_bib(input())
    print(format_bib(resp))