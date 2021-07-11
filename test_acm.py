import unittest
import json
import acm


EXPECTED_OUTPUT = """@article{10.1145/3428216,
author = {Zhou, Fangyi and Ferreira, Francisco and Hu, Raymond and Neykova, Rumyana and Yoshida, Nobuko},
title = {Statically Verified Refinements for Multiparty Protocols},
year = {2020},
issue_date = {November 2020},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
volume = {4},
number = {OOPSLA},
url = {https://doi.org/10.1145/3428216},
doi = {10.1145/3428216},
abstract = {With distributed computing becoming ubiquitous in the modern era, safe distributed
programming is an open challenge. To address this, multiparty session types (MPST)
provide a typing discipline for message-passing concurrency, guaranteeing communication
safety properties such as deadlock freedom.  While originally MPST focus on the communication
aspects, and employ a simple typing system for communication payloads, communication
protocols in the real world usually contain constraints on the payload. We introduce
refined multiparty session types (RMPST), an extension of MPST, that express data
dependent protocols via refinement types on the data types.  We provide an implementation
of RMPST, in a toolchain called Session*, using Scribble, a toolchain for multiparty
protocols, and targeting F*, a verification-oriented functional programming language.
Users can describe a protocol in Scribble and implement the endpoints in F* using
refinement-typed APIs generated from the protocol. The F* compiler can then statically
verify the refinements. Moreover, we use a novel approach of callback-styled API generation,
providing static linearity guarantees with the inversion of control. We evaluate our
approach with real world examples and show that it has little overhead compared to
a naive implementation, while guaranteeing safety properties from the underlying theory.},
journal = {Proc. ACM Program. Lang.},
month = nov,
articleno = {148},
numpages = {30},
keywords = {Multiparty Session Types (MPST), Refinement Types, Distributed Programming, F*, Code Generation}
}"""

INPUT = json.load(open("testdata/acm.json"))


class AcmDownloadTestCase(unittest.TestCase):
    def test_example(self):
        self.maxDiff = None
        self.assertEqual(acm.format_bib(INPUT), EXPECTED_OUTPUT)
