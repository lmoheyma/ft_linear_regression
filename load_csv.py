import pandas as pd


def load(path: str) -> pd.core.frame.DataFrame:
    """
    Takes a path as argument, writes the dimensions of the data set
    and returns it.
    """
    try:
        data = pd.read_csv(path)
    except IOError:
        print(f"Can't open file {path}")
        exit(1)
    print(f"Loading dataset of dimensions {data.shape}")
    return data
