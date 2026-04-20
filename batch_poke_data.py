import pandas as pd
import math
import os

BATCH_SIZE = 30
INPUT_FILE = "poke_data.json"
OUTPUT_DIR = "poke_batches"


def parse_poke_data(file_path):
    try:
        poke_df = pd.read_json(file_path)
        print(f"Successfully loaded data from {file_path}")
        return poke_df
    except Exception as e:
        print(f"Error loading data from {file_path}: {e}")
        return None


def split_into_batches(df, batch_size, output_dir):
    total_records = len(df)
    num_batches = math.ceil(total_records / batch_size)

    os.makedirs(output_dir, exist_ok=True)

    print(f"\nTotal records : {total_records}")
    print(f"Batch size    : {batch_size}")
    print(f"Total batches : {num_batches}")
    print(
        f"Last batch    : {total_records % batch_size or batch_size} records\n")

    for batch_num in range(num_batches):
        start = batch_num * batch_size
        # slice handles overflow automatically
        end = start + batch_size

        batch_df = df.iloc[start:end]

        # Zero-padded filename so files sort correctly (batch_001, batch_002, ...)
        file_name = f"poke_batch_{str(batch_num + 1).zfill(len(str(num_batches)))}.json"
        file_path = os.path.join(output_dir, file_name)

        batch_df.to_json(file_path, orient="records", indent=4)
        print(
            f"  Wrote batch {batch_num + 1:>3} → {file_path}  ({len(batch_df)} records)")

    print(f"\nDone. {num_batches} files saved to '{output_dir}/'")


if __name__ == "__main__":
    poke_data_df = parse_poke_data(INPUT_FILE)

    if poke_data_df is not None:
        print(poke_data_df.head())
        split_into_batches(poke_data_df, BATCH_SIZE, OUTPUT_DIR)
