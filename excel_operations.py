import pandas as pd

# File paths
input_file = "Lab Assay Values (H 003 and 006).xlsx"   # Ensure this file exists in your repo
output_file = "output.xlsx"

def read_excel(file_path):
    try:
        df = pd.read_excel(file_path, engine='openpyxl')  # Specify engine
        print("Excel Data Read Successfully:")
        print(df)
        return df
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return None

def write_excel(file_path, data):
    try:
        df = pd.DataFrame(data)
        df.to_excel(file_path, index=False, engine='openpyxl')  # Specify engine
        print(f"Data written to {file_path}")
    except Exception as e:
        print(f"Error writing Excel file: {e}")

if __name__ == "__main__":
    df = read_excel(input_file)
    if df is not None:
        df["NewColumn"] = "TestValue"  # Modify data
        write_excel(output_file, df)
