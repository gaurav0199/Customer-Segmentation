import yaml
import pandas as pd
import os

def write_schema_yaml(csv_file):
    # Read CSV file and get number of columns and column names
    df = pd.read_csv(csv_file)
    num_cols = len(df.columns)
    column_names = df.columns.tolist()
    column_dtypes = df.dtypes.astype(str).tolist()  # Convert data types to string for YAML compatibility

    # Create schema dictionary
    schema = {
        "FileName": os.path.basename(csv_file),
        "NumberOfColumns": num_cols,
        "ColumnNames": dict(zip(column_names, column_dtypes))
    }

    # Write schema to schema.yaml file
    with open("schema.yaml", "w") as file:
        yaml.dump(schema, file)

# Call the function with the CSV file path
ROOT_DIR = os.getcwd()
path = os.path.join(ROOT_DIR,"data","Online Retail.csv")
# write_schema_yaml(r"P:\MLiveCoding2\Customer-Segmentation\data\Online Retail.csv")
write_schema_yaml(path)