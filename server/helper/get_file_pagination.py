import math
import os

import pandas as pd

LABEL_MAPPER = {
    "good": 1,
    "bad": -1,
    "marginal": 0
}


class PaginationDataFrameIterator:
    def __init__(self, dataframe: pd.DataFrame, save_location: str):
        self.df = dataframe
        self.save_loc = save_location

    def _get_all_unlabelled(self) -> pd.DataFrame:
        return self.df.loc[self.df['label'].isna()]

    def _get_all_labelled(self) -> pd.DataFrame:
        return self.df.loc[self.df['label'].notna()]

    def _get_row_from_filename(self, filename) -> pd.DataFrame:
        return self.df.loc[self.df.filename == filename]

    def get_top_unlabelled_filename(self, page_length=5, page=1):
        assert page > 0, "page start from 1"
        assert page_length > 0
        return self._get_all_unlabelled().head(page_length)['filename'].tolist()

    def get_pagination_of_type(self, type_of: str, page_length: int):
        assert page_length > 0
        if type_of.lower() == "labelled":
            return math.ceil(len(self._get_all_labelled().index) / page_length)
        elif type_of.lower() == "unlabelled":
            return math.ceil(len(self._get_all_unlabelled().index) / page_length)

    def get_labelled_paginated(self, page_length: int = 5, page: int = 1):
        offset = (page - 1) * page_length
        temp_df = self._get_all_labelled().iloc[offset: offset + page_length]
        return temp_df.apply(lambda x: x.to_dict(), axis=1).to_list()

    def sync_folder(self, directory=None):
        if directory is None:
            directory = self.save_loc
        parsed = set(self.df['filename'])
        un_parsed = []
        with os.scandir(directory) as scanner:
            un_parsed.extend(filename.name for filename in scanner if
                             filename.is_file() and filename.name not in parsed and filename.name.lower().endswith(
                                 ('.png', '.jpg', '.jpeg')))

        temp_df = pd.DataFrame(un_parsed, columns=['filename'])
        self.df = pd.concat([self.df, temp_df], ignore_index=True)
        self.df.drop_duplicates(subset='filename', keep="last", inplace=True)

    def change_label(self, filename, label):
        row = self._get_row_from_filename(filename)
        self.df.loc[row.index, 'label'] = LABEL_MAPPER[label]

    def save_df(self):
        self.df.to_feather(os.path.join(self.save_loc, 'label-data.feather'))

    def add_image(self, image_filename):
        temp_df = pd.DataFrame(image_filename, columns=['filename'])
        self.df = pd.concat([self.df, temp_df], ignore_index=True)
        self.df.drop_duplicates(subset='filename', keep="last", inplace=True, ignore_index=True)
