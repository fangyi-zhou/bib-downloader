# Bib Downloader
Download `.bib` files from DOIs.

## Motivation
I got annoyed that every time I try to download the bibtex file from Springer, the browser creates a new file in my download folder. I have to open it, copy it, and then paste it to my bib file for my paper.

So I decided to make a CLI tool to download bibtex files from DOIs, relieving myself from countless bibtex files in my download folder.

Currently ACM and Springer DOIs are supported.

## How to install
Since there is no released version yet...

First install `pipenv`
```bash
$ python3 -m pip install pipenv
```
Then clone this repo

## How to use

```bash
$ pipenv run python -m bib_downloader 10.1007/3-540-06859-7_148
@InProceedings{10.1007/3-540-06859-7_148,
author="Reynolds, John C.",
editor="Robinet, B.",
title="Towards a theory of type structure",
booktitle="Programming Symposium",
year="1974",
publisher="Springer Berlin Heidelberg",
address="Berlin, Heidelberg",
pages="408--425",
isbn="978-3-540-37819-8"
}
```

## Future work

- Support more publishers (most likely the ones I frequently retrieve from, e.g. LMCS, Elsevier, arXiv)
- Support URL inputs (ACM/Springer links contain DOIs)
- Better error handling
- Fix `title` field of bibtex, so that caplital letters in titles don't become small case
