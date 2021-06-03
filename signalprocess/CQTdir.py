import os # automating through directory
import numpy as np
import zaf
import matplotlib.pyplot as plt


TRAINING_DIR = "LFTrain/WAVs"
SAVE_PATH = "LFTrain/CQT"

for song in os.listdir(TRAINING_DIR):

    # Read the audio signal (normalized) with its sampling frequency in Hz, and average it over its channels
    song_name = str(song)
    # print(song_name)
    audio_signal, sampling_frequency = zaf.wavread("{dir_name}/{song_name}".format(dir_name = TRAINING_DIR, song_name = song_name))
    audio_signal = np.mean(audio_signal, 1)

    # Compute the CQT kernel
    octave_resolution = 24
    minimum_frequency = 20
    maximum_frequency = 20000
    cqt_kernel = zaf.cqtkernel(sampling_frequency, octave_resolution, minimum_frequency, maximum_frequency)

    # Compute the CQT spectrogram using the kernel
    time_resolution = 25
    cqt_spectrogram = zaf.cqtspectrogram(audio_signal, sampling_frequency, time_resolution, cqt_kernel)

    # Display the CQT spectrogram in dB, seconds, and Hz
    plt.figure(figsize=(17, 10))
    zaf.cqtspecshow(cqt_spectrogram, time_resolution, octave_resolution, minimum_frequency, xtick_step=1)
    plt.title("CQT spectrogram (dB)")
    # plt.show()
    plt.savefig("{dir_name}/{song_name}CQT.png".format(dir_name = SAVE_PATH, song_name = song_name[:len(song_name) - 4]))


