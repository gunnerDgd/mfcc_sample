from train_data.meta_import import imp_plot
from train_data.mfcc        import train_data_mfcc     as train_mfcc
from train_data.stft        import train_data_stft     as train_stft
from train_data.stft_max    import train_data_stft_max as train_stft_max
from train_data.sample      import raw_sample          as train_sample

snd_base_path = 'D:/[2] Project Resource/Python/MFCC/Typecast/SimpleWord/'

snd_sample = []
snd_sample.append(train_sample(snd_base_path + "tc-man-normal.wav"))
snd_sample.append(train_sample(snd_base_path + "tc-man2-normal.wav"))
snd_sample.append(train_sample(snd_base_path + "tc-woman-normal.wav"))

snd_train_data = []
for it_sample in snd_sample:
    train_tuple        = (train_mfcc(it_sample), train_stft(it_sample), train_stft_max(it_sample))
    snd_train_data.append(train_tuple)

for i_sample in range(0, len(snd_train_data)):
    for i_train in range(0, len(snd_train_data[i_sample])):
        snd_train_data[i_sample][i_train].show_data(3, 3, i_sample*3 + i_train + 1)

imp_plot.show()
