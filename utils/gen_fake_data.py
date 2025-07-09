import os
import pandas as pd
import numpy as np
from helpers import load_cfg

cfg_path = "./utils/config.yaml"

if __name__ == "__main__":
    start_ts = "20-01-2025"
    end_ts = "31-12-2029"

    features = ["pressure", "velocity", "speed"]

    ts = pd.date_range(start=start_ts, end=end_ts, freq="H")
    df = pd.DataFrame(ts, columns=["event_timestamp"])

    for feature in features:
        df[feature] = np.random.random_sample((len(ts),))

    cfg = load_cfg(cfg_file=cfg_path)
    fake_data_cfg = cfg["fake_data"]
    number_file = fake_data_cfg["number_file"]

    os.makedirs(fake_data_cfg["folder_path"], exist_ok=True)

    df_splits = np.array_split(df, number_file)
    for i in range(number_file):
        df_splits[i].reset_index().to_parquet(
            os.path.join(fake_data_cfg["folder_path"], f"part_{i}.parquet")
        )

    