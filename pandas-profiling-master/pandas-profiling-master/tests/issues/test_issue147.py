"""
Test for issue 147:
https://github.com/pandas-profiling/pandas-profiling/issues/147
"""
import pandas as pd

from pandas_profiling import ProfileReport


def test_issue147(get_data_file):
    file_name = get_data_file(
        "userdata1.parquet",
        "https://github.com/Teradata/kylo/raw/master/samples/sample-data/parquet/userdata2.parquet",
    )

    df = pd.read_parquet(str(file_name), engine="fastparquet")
    report = ProfileReport(df, title="PyArrow with Pandas Parquet Backend")
    html = report.to_html()
    assert type(html) == str
    assert "<p class=h4>Dataset statistics</p>" in html
