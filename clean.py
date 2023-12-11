import pandas as pd

def process_csv(input_file, output_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_file)

    # Remove exact duplicate rows
    df = df.drop_duplicates()

    # Remove cells that start with '@'
    df = df.apply(lambda col: col.map(lambda x: '' if isinstance(x, str) and x.startswith('@') else x) if col.dtype == "object" else col)

    # Write the result to a new CSV file
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    input_file = r'C:\Users\hp\Desktop\twitter\tweets2.csv'  # Replace with your actual input CSV file
    output_file = "output.csv"  # Replace with your desired output file

    process_csv(input_file, output_file)
