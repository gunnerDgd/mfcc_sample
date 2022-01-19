from train_data.meta_import import imp_plot
from train_data.meta_import import imp_rosa_disp
from train_data.meta_import import imp_mfcc

from train_data.meta_data   import meta_train_data
from train_data.sample      import raw_sample

class train_data_mfcc(meta_train_data):
    def __init__(self, sample_raw : raw_sample):
        self.mfcc_raw   = sample_raw.data
        self.mfcc_array = imp_mfcc.mfcc(sample_raw.data, sample_raw.srate, winlen=0.010, winstep=0.01, numcep=13, nfilt=26, nfft=512, lowfreq=0, highfreq=None, preemph=0.97, ceplifter=22, appendEnergy=True)

    def preprocess(self):
        pass

    def show_data(self, plot_total : int, plot_x : int, plot_y : int):
        imp_plot     .subplot (plot_total, plot_x, plot_y)
        imp_rosa_disp.specshow(self.mfcc_array, y_axis='time')

    def get_train_data(self):
        return self.mfcc_array