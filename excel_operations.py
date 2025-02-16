import pandas as pd

# Function to read data from Excel
def read_excel(file_path):
    df = pd.read_excel(file_path)
    print("Excel Data:")
    print(df)
    return df

# Function to write data to Excel
def write_excel(file_path, data):
    df = pd.DataFrame(data)
    df.to_excel(file_path, index=False)
    print(f"Data written to {file_path}")

# Example usage
if __name__ == "__main__":
    file_name = "data.xlsx"  # Your Excel file in the repo
    new_file = "output.xlsx"  # New file to be written
    
    # Read from Excel
    df = read_excel(file_name)
    
    # Modify data (example: adding a new column)
    df["NewColumn"] = "TestValue"
    
    # Write back to a new Excel file
    write_excel(new_file, df)
