class MetaWords:
    meta = {'from_timestamp': 'from',
            'to_timestamp': 'to'}


class ChangeKeys(MetaWords):
    def __init__(self, data_dict: dict):
        self.data_dict = data_dict

    def reformat(self):
        return {i if i not in MetaWords.meta.keys() else MetaWords.meta[i]: self.data_dict[i] for i in self.data_dict}

