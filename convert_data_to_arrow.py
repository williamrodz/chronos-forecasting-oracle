from pathlib import Path
from typing import List, Optional, Union

import numpy as np
from gluonts.dataset.arrow import ArrowWriter
import pandas as pd

def convert_to_arrow(
    path: Union[str, Path],
    time_series: Union[List[np.ndarray], np.ndarray],
    start_times: Optional[Union[List[np.datetime64], np.ndarray]] = None,
    compression: str = "lz4",
):
    if start_times is None:
        # Set an arbitrary start time
        start_times = [np.datetime64("2000-01-01 00:00", "s")] * len(time_series)

    assert len(time_series) == len(start_times)

    dataset = [
        {"start": start, "target": ts} for ts, start in zip(time_series, start_times)
    ]
    ArrowWriter(compression=compression).write_to_file(
        dataset,
        path=path,
    )

if __name__ == "__main__":
    # Generate 20 random time series of length 1024
    # time_series = [np.random.randn(1024) for i in range(20)]
    # print(time_series)
    # print(np.shape(time_series))

    # Convert to GluonTS arrow format
    # convert_to_arrow("./noise-data.arrow", time_series=time_series)

    # Load the dataset from csv
    # system_prices_df = pd.read_csv("./data/system_price.csv")
    # sytem_prices_values_np = np.array(system_prices_df["Daily average"].values)
    # print(sytem_prices_values_np)
    # print(sytem_prices_values_np)
    # print(np.shape([sytem_prices_values_np]))
    # convert_to_arrow("./system-prices.arrow", time_series=[sytem_prices_values_np])

    # Prepare Agile Octopus Training Data

    training_data_file_names = [
        "agile_octopus_london_alpha_2_weeks",
        "agile_octopus_london_beta_2_weeks",
        "agile_octopus_london_delta_2_weeks"
    ]

    for file_name in training_data_file_names:
        training_data_df = pd.read_csv(f"./data/{file_name}.csv")
        training_data_values_np = np.array(training_data_df["Price_Ex_VAT"].values)
        # print(training_data_values_np)
        # print(np.shape([training_data_values_np]))
        convert_to_arrow(f"./data/{file_name}.arrow", time_series=[training_data_values_np])
    print("Done converting files to arrow format")
