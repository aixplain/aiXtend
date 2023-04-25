__author__ = "thiagocastroferreira"

import logging
import pandas as pd

from aixplain.enums.file_type import FileType
from aixplain.enums.storage_type import StorageType
from aixplain.modules.file import File
from aixplain.modules.metadata import MetaData
from aixplain.utils.file_utils import upload_data
from pathlib import Path
from tqdm import tqdm
from typing import List, Optional, Text, Tuple


def process_text(content: str, storage_type: StorageType) -> Text:
    """Process text files

    Args:
        content (str): URL with text, local path with text or textual content
        storage_type (StorageType): type of storage: URL, local path or textual content

    Returns:
        Text: textual content
    """
    if storage_type == StorageType.FILE:
        with open(content) as f:
            text = f.read()
    else:
        text = content
    return text


def run(
    metadata: MetaData, paths: List, folder: Path, batch_size: int = 1000, split_data: Optional[MetaData] = None
) -> Tuple[List[File], int]:
    """Process a list of local textual files, compress and upload them to pre-signed URLs in S3

    Explanation:
        Each text on "paths" is processed. If the text is in a public link or local file, it will be downloaded and added to an index CSV file.
        The texts are processed in batches such that at each "batch_size" texts, the index CSV file is uploaded into a pre-signed URL in s3 and reset.

    Args:
        metadata (MetaData): meta data of the asset
        paths (List): list of paths to local files
        folder (Path): local folder to save compressed files before upload them to s3.
        split_data (Optional[MetaData], optional): info regarding data split into train, val and test. Defaults to None.

    Returns:
        Tuple[List[File], int]: list of s3 links and data colum index
    """
    logging.debug(f'Data Asset Onboarding: Processing "{metadata.name}".')
    idx = 0
    data_column_idx = -1
    files, batch, split = [], [], []
    for i in tqdm(range(len(paths)), desc=f' Data "{metadata.name}" onboarding progress', position=1, leave=False):
        path = paths[i]
        try:
            dataframe = pd.read_csv(path)
        except Exception as e:
            message = f'Data Asset Onboarding Error: Local file "{path}" not found.'
            logging.exception(message)
            raise Exception(message)

        # process texts and labels
        for j in tqdm(range(len(dataframe)), desc=" File onboarding progress", position=2, leave=False):
            row = dataframe.iloc[j]
            try:
                text_path = row[metadata.name]
            except Exception as e:
                message = f'Data Asset Onboarding Error: Column "{metadata.name}" not found in the local file {path}.'
                logging.exception(message)
                raise Exception(message)

            try:
                text = process_text(text_path, metadata.storage_type)
                batch.append(text)
            except Exception as e:
                logging.warning(
                    f'Data Asset Onboarding: The instance "{row}" of "{metadata.name}" could not be processed and will be skipped.'
                )

            if split_data is not None:
                try:
                    split_row = str(row[split_data.name]).upper()
                except Exception as e:
                    message = (
                        f'Data Asset Onboarding Error: Split Column "{split_data.name}" not found in the local file {path}.'
                    )
                    logging.exception(message)
                    raise Exception(message)

                assert split_row in [
                    "TRAIN",
                    "VALIDATION",
                    "TEST",
                ], f'Data Asset Onboarding Error: Split Column must consist of "TRAIN", "VALIDATION", "TEST" labels.'

                split.append(split_row)

            idx += 1
            if ((idx + 1) % batch_size) == 0:
                batch_index = str(len(files) + 1).zfill(8)
                file_name = f"{folder}/{metadata.name}-{batch_index}.csv.gz"

                df = pd.DataFrame({metadata.name: batch})
                start, end = idx - len(batch), idx
                df["@INDEX"] = range(start, end)
                # add split info
                if len(split) > 0:
                    df["@SPLIT"] = split
                df.to_csv(file_name, compression="gzip", index=False)
                s3_link = upload_data(file_name, content_type="text/csv", content_encoding="gzip")
                files.append(File(path=s3_link, extension=FileType.CSV, compression="gzip"))
                # get data column index
                data_column_idx = df.columns.to_list().index(metadata.name)
                batch, split = [], []

    if len(batch) > 0:
        batch_index = str(len(files) + 1).zfill(8)
        file_name = f"{folder}/{metadata.name}-{batch_index}.csv.gz"

        df = pd.DataFrame({metadata.name: batch})
        start, end = idx - len(batch), idx
        df["@INDEX"] = range(start, end)
        # add split info
        if len(split) > 0:
            df["@SPLIT"] = split
        df.to_csv(file_name, compression="gzip", index=False)
        s3_link = upload_data(file_name, content_type="text/csv", content_encoding="gzip")
        files.append(File(path=s3_link, extension=FileType.CSV, compression="gzip"))
        # get data column index
        data_column_idx = df.columns.to_list().index(metadata.name)
        batch, split = [], []
    return files, data_column_idx
