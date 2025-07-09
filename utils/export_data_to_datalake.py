from helpers import load_cfg
from minio import Minio
import glob
import os

cfg_path = "./utils/config.yaml"

def main():
    cfg = load_cfg(cfg_path)
    data_lake_cfg = cfg["data_lake"]
    fake_data_cfg = cfg["fake_data"]

    client = Minio(
        endpoint=data_lake_cfg["endpoint"],
        access_key=data_lake_cfg["access_key"],
        secret_key=data_lake_cfg["secret_key"],
        secure=False
    )

    found = client.bucket_exists(bucket_name=data_lake_cfg["bucket_name"])

    if not found:
        found = client.make_bucket(bucket_name=data_lake_cfg["bucket_name"])
    else:
        print(f'bucket {data_lake_cfg["bucket_name"]} da co, bo qua buoc tao')

    all_fps = glob.glob(os.path.join(fake_data_cfg["folder_path"], "*.parquet"))

    for fp in all_fps:
        print(f"upload{fp}")
        client.fput_object(
            bucket_name=data_lake_cfg["bucket_name"],
            object_name=os.path.join(data_lake_cfg["folder_name"], os.path.basename(fp)),
            file_path=fp
        )

if __name__ == "__main__":
    main()