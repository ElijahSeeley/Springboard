"""
Test for issue 169:
https://github.com/pandas-profiling/pandas-profiling/issues/169
"""
from io import StringIO

import pandas as pd
import pytest

import pandas_profiling


@pytest.fixture
def issue_169_data() -> StringIO:
    data = StringIO(
        """index,company-code,company,shop-code,shop,description,brand
    item_24119,13,COMPANY NAME,32,COMPANY - EXITS,GREAT PRODUCT SELLING,BRAND1
    item_27405,13,COMPANY NAME,32,COMPANY - EXITS,THIS IS THE BEST PRODUCT,
    """
    )

    return data


def test_issue_169_column(issue_169_data):
    df = pd.read_csv(issue_169_data, sep=",")
    report = df.profile_report(missing_diagrams={"dendrogram": True, "heatmap": True})
    html = report.to_html()
    assert type(html) == str
    assert "<p class=h4>Dataset statistics</p>" in html


def test_issue_169_index(issue_169_data):
    df = pd.read_csv(issue_169_data, sep=",", index_col=0)
    report = df.profile_report(missing_diagrams={"dendrogram": True, "heatmap": True})
    html = report.to_html()
    assert type(html) == str
    assert "<p class=h4>Dataset statistics</p>" in html
