import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    This function returns a loaded file.
    """
    try:
        if not path:
            raise ValueError("Path cannot be empty")
        loaded_data = pd.read_csv(path)
        if loaded_data.empty:
            print("The file is empty.")
            return None
        print(f"Loading dataset of dimensions {loaded_data.shape}")
        return loaded_data
    except (pd.errors.ParserError, FileNotFoundError) as e:
        print("File Error:", e)
        return None
