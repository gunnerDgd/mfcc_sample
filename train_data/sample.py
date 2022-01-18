import librosa as smp_rosa

class raw_sample:
    def __init__(self, path):
        self.data, self.srate = smp_rosa.load(path)