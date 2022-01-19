from train_data.meta_import import imp_plot
from train_data.meta_import import imp_rosa
from train_data.meta_import import imp_numpy

from train_data.meta_data   import meta_train_data
from train_data.sample      import raw_sample

class train_data_stft(meta_train_data):
    def __init__(self, sample_raw : raw_sample):
        self.stft_raw   = sample_raw.data
        self.stft_array = imp_numpy.abs(imp_rosa.stft(self.stft_raw, n_fft=8192, hop_length=8193))

    def preprocess(self):
        pass

    def show_data(self, plot_total : int, plot_x : int, plot_y : int):
        imp_plot.subplot(plot_total, plot_x, plot_y)
        imp_plot.plot   (self.stft_array)

    def get_train_data(self):
        return self.stft_array