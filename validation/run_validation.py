import yaml
import pandas as pd
from validation.csv_validation import validate_csv

def run_validation():

    with open("config/pipeline_config.yaml") as f:
        config = yaml.safe_load(f)

    csv_file = config["source_csv"]

    print("Running CSV validation...")

    df = validate_csv(csv_file)

    print("Validation completed")
    print("Rows processed:", len(df))


if __name__ == "__main__":
    run_validation()