from train_data import sample
import matplotlib.pyplot as plot

from train_data.mfcc     import train_data_mfcc     as train_mfcc
from train_data.stft     import train_data_stft     as train_stft
from train_data.stft_max import train_data_stft_max as train_stft_max
from train_data.sample   import raw_sample          as train_sample

snd_base_path = 'D:/[2] Project Resource/Python/MFCC/Typecast/MultipleSentence/'


snd_sample = []
for i in range(1, 6):
    snd_sample.append(train_sample(snd_base_path + 'tc_man0_sound' + str(i) + '.wav'))

snd_train_data = [()]
for it_sample in snd_sample:
    train_tuple        = (train_mfcc(it_sample), train_stft(it_sample), train_stft_max(it_sample))
    snd_train_data.append(train_tuple)

for i in range(0, len(snd_train_data[0])):
    snd_train_data[0][i].show_data(5, 1, i + 1)

plot.show()
