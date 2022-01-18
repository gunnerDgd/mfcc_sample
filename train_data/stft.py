from train_data.meta_data import meta_train_data
from train_data.sample    import raw_sample as stft_sample

from meta_import import imp_plot
from meta_import import imp_rosa
from meta_import import imp_numpy

class train_data_stft(meta_train_data):
    def __init__(self, sample_raw : stft_sample):
        self.stft_raw   = sample_raw.data
        self.stft_array = stft_numpy.abs(stft_rosa.stft(self.stft_raw, n_fft=8192, hop_length=8193))

    def preprocess(self):
        pass

    def show_data(self, plot_total : int, plot_x : int, plot_y : int):
        stft_plot.subplot(plot_total, plot_x, plot_y)
        stft_plot.plot   (self.stft_array)

    def get_train_data(self):
        return self.stft_array