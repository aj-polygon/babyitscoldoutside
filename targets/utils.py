import pandas as pd
from urllib.parse import urlencode

base_url = "https://docs.google.com/forms/d/e/"


def make_form_url_from_series(target_dict: dict, series: pd.Series) -> str:

    target_fields = target_dict["fields"]
    form_id = target_dict["form_id"]

    query_params = {
        target_fields["name"]: "melt",
        target_fields["plate"]: series["Plate"].item(),
        target_fields["color"]: series["Color"].item(),
        target_fields["make"]: series["Make"].item(),
        target_fields["model"]: series["Model"].item(),
    }

    query_string = urlencode(query_params)

    url = f"{base_url}{form_id}/viewform?{query_string}"

    return url


def make_form_url_from_plate(target_dict: dict, plate_string: str) -> str:

    target_fields = target_dict["fields"]
    form_id = target_dict["form_id"]

    query_params = {
        target_fields["plate"]: plate_string,
    }

    query_string = urlencode(query_params)

    url = f"{base_url}{form_id}/viewform?{query_string}"

    return url
