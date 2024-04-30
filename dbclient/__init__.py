import os
import json


class Collection:
    def __init__(self, fp: os.PathLike):
        self.fp = fp

    def __getitem__(self, key):
        children = os.listdir(self.fp)
        if key in children:
            if os.path.isdir(os.path.join(self.fp, key)):
                return Collection(os.path.join(self.fp, key))
            else:
                with open(os.path.join(self.fp, key), "r") as f:
                    return json.load(f)
        else:
            return None

    def __setitem__(self, key, value):
        if not isinstance(value, dict):
            raise ValueError("Value must be a dictionary")
            return
        if not os.path.exists(self.fp):
            os.makedirs(self.fp)
        with open(os.path.join(self.fp, key), "w") as f:
            json.dump(value, f)

    def __delitem__(self, key):
        os.remove(os.path.join(self.fp, key))
    
    def keys(self):
        return os.listdir(self.fp)
    

class Document:
    def __init__(self, fp: os.PathLike):
        self.fp = fp

    def __getitem__(self, key):
        with open(self.fp, "r") as f:
            data = json.load(f)
            return data[key]

    def __setitem__(self, key, value):
        with open(self.fp, "r") as f:
            data = json.load(f)
        data[key] = value
        with open(self.fp, "w") as f:
            json.dump(data, f)

    def __delitem__(self, key):
        with open(self.fp, "r") as f:
            data = json.load(f)
        del data[key]
        with open(self.fp, "w") as f:
            json.dump(data, f)