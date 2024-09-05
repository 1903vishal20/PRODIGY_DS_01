import pandas as pd

# Replace with your actual file path
file_path = 'dataset.csv'

try:
    # First attempt: Read the file with the default settings
    df = pd.read_csv(file_path)
    print("File read successfully with default settings!")
    print(df.head())
except pd.errors.ParserError as e:
    print("ParserError encountered. Trying alternative methods...")
    try:
        # Second attempt: Specify a different delimiter (e.g., semicolon)
        df = pd.read_csv(file_path, delimiter=';')
        print("File read successfully with semicolon delimiter!")
        print(df.head())
    except pd.errors.ParserError as e:
        print("ParserError encountered with semicolon delimiter.")
        try:
            # Third attempt: Read with low_memory option and skip bad lines
            df = pd.read_csv(file_path, low_memory=False, error_bad_lines=False)
            print("File read successfully with low_memory=False and skipping bad lines!")
            print(df.head())
        except pd.errors.ParserError as e:
            print("ParserError encountered with low_memory=False.")
            try:
                # Fourth attempt: Read the first few lines to inspect the file
                with open(file_path, 'r') as file:
                    print("Inspecting the first few lines of the file:")
                    for _ in range(5):
                        print(file.readline())
                # Attempt to read with manual column names
                df = pd.read_csv(file_path, header=None)
                print("File read successfully with manual column names!")
                print(df.head())
            except Exception as e:
                print(f"An unexpected error occurred while inspecting the file: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
