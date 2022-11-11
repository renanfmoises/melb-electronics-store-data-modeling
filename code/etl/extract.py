""" This function downloads the parquet file and converts and stores it to csv. """

from dataclasses import dataclass
import os
import pathlib
import pandas as pd

# @dataclass
class Extract:
    """This method extracts the data from the source URL and stores it locally.

    Args:
        url (str): URL of the source data.
        file_name (str): name of the file to download.

    Returns:
        None
    """

    def __init__(self, file_path: str) -> None:
        self.__accepted_extensions = ["csv"]
        self.__file_path = file_path

        self.__file = self.__file_path.split("/")[-1]
        self.file_name, self.file_extension = self.__file.split(".")

        self.pandas_df = None
        self.n_rows = None

    def load_pandas_df(self) -> None:
        """Load the pandas dataframe into memmory and update n_rows attribute."""
        if self.file_extension == "csv":
            self.pandas_df = pd.read_csv(self.__file_path)

        else:
            raise ValueError(
                f"File extension {self.file_extension} is not supported. Supported extensions are {self.__accepted_extensions}"
            )

        self.n_rows = self.pandas_df.shape[0]
