from abc import *
import matplotlib.pyplot

class meta_train_data(metaclass=ABCMeta):
    @abstractmethod
    def show_data(self, plot_total : int, plot_x : int, plot_y : int):
        pass

    @abstractmethod
    def get_train_data(self):
        pass

    @abstractmethod
    def preprocess(self):
        pass

    def show(self):
        matplotlib.pyplot.show()
