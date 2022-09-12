import cfbd

from cfb_ranker import Ranker


def test_null():
    ranker = Ranker(year=2021, week=10)
    assert isinstance(ranker, Ranker)
