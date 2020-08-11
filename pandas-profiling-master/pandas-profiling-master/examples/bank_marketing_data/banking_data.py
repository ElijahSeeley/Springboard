# As featured on this Google Cloud Platform page:
# https://cloud.google.com/solutions/building-a-propensity-model-for-financial-services-on-gcp
from pathlib import Path

import pandas as pd

from pandas_profiling import ProfileReport
from pandas_profiling.utils.cache import cache_file

if __name__ == "__main__":
    file_name = cache_file(
        "bank-full.csv",
        "https://storage.googleapis.com/erwinh-public-data/bankingdata/bank-full.csv",
    )

    # Download the UCI Bank Marketing Dataset
    df = pd.read_csv(file_name, sep=";")

    profile = ProfileReport(
        df, title="Profile Report of the UCI Bank Marketing Dataset", explorative=True
    )
    profile.to_file(Path("uci_bank_marketing_report.html"))
