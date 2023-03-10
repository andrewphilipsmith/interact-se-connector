from interact_se_connector.connector import InteractConnection
import pandas as pd
from icecream import ic
import pytest


@pytest.mark.skip("need to mock connection")
def test_upload_scrapper_content():
    iac = InteractConnection(
        display_url="https://example.com", api_key="123", search_app_id=1
    )
    hugo_df = pd.read_csv("test_hugo_output.csv")
    iac.upload_scrapper_content(hugo_df.head(2))
    assert False


@pytest.mark.skip("need to mock connection")
def test_check_connection():
    iac = InteractConnection(
        display_url="https://mathison.turing.ac.uk", api_key="123", search_app_id=1
    )

    iac._get_api_details()

    ic(iac.api_url)
    ic(iac.common_headers)
    assert False
