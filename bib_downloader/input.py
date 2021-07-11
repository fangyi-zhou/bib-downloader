from . import acm, springer


def extract_doi(input: str) -> str:
    # TODO: Actually extract DOI
    return input


PUBLISHER_LOOKUP = {
    "10.1145": acm.get_bib,
    "10.1007": springer.get_bib,
}


def process_doi(doi: str) -> str:
    splitted = doi.split("/")
    publisher = splitted[0]
    if publisher not in PUBLISHER_LOOKUP:
        raise NotImplementedError()
    return PUBLISHER_LOOKUP[publisher](doi)


def process_input(input: str) -> str:
    doi = extract_doi(input)
    return process_doi(input)
