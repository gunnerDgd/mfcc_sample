from train_data.stft_max import train_data_stft_max

class method_window_slice:
    def __init__(self, stft_width : int, stft_max_count : int, stft : train_data_stft_max):
        self.stft_data         = stft.stft_max
        self.stft_sliced       = []
        self.stft_slice_dict   = dict()

        self.stft_window_width     = stft_width
        self.stft_window_max_count = stft_max_count
        self.stft_window_count     = int(len(self.stft_data) / self.stft_window_width) + 1

    def __stft_slice_find_max(self):
        window_max_dict = dict()

        for it_slice in range(0, len(self.stft_sliced)):
            for it_row in range(0, len(self.stft_sliced[it_slice])):
                self.stft_slice_dict[]

    def __stft_slice_section(self):
        for it_slice in range(0, self.stft_window_count):
