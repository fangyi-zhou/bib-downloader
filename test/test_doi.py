import pytest

from bib_downloader import doi


def test_acm_doi(monkeypatch):
    acm_doi = "10.1145/3428216"

    def mock_return(_doi_str):
        return "MOCK RETURN"

    monkeypatch.setitem(doi.PUBLISHER_LOOKUP, doi.ACM_PREFIX, mock_return)

    result = doi.process_doi(acm_doi)
    assert result == "MOCK RETURN"


def test_springer_doi(monkeypatch):
    springer_doi = "10.1007/978-3-319-89884-1_28"

    def mock_return(_doi_str):
        return "MOCK RETURN"

    monkeypatch.setitem(doi.PUBLISHER_LOOKUP, doi.SPRINGER_PREFIX, mock_return)

    result = doi.process_doi(springer_doi)
    assert result == "MOCK RETURN"
