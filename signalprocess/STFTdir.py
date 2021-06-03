import os
import numpy as np
import scipy.signal
import zaf
import matplotlib.pyplot as plt


TRAINING_DIR = "LFTrain/WAVs_A"
SAVE_PATH = "LFTrain/STFT"

for song in os.listdir(TRAINING_DIR):

    # Read the audio signal (normalized) with its sampling frequency in Hz, and average it over its channels
    song_name = str(song)

    # Read the audio signal (normalized) with its sampling frequency in Hz, and average it over its channels
    audio_signal, sampling_frequency = zaf.wavread("{dir_name}/{song_name}".format(dir_name = TRAINING_DIR, song_name = song_name))
    # audio_signal is two-column (L/R), each column is array of amplitude
    # normalized by zaf.wavread
    audio_signal = np.mean(audio_signal, 1)

    # Set the window duration in seconds (audio is stationary around 40 milliseconds)
    window_duration = 0.04

    # Derive the window length in samples (use powers of 2 for faster FFT and constant overlap-add (COLA))
    window_length = pow(2, int(np.ceil(np.log2(window_duration * sampling_frequency))))

    # Compute the window function (use SciPy's periodic Hamming window for COLA as NumPy's Hamming window is symmetric)
    window_function = scipy.signal.hamming(window_length, sym=False)

    # Set the step length in samples (half of the window length for COLA)
    step_length = int(window_length / 2)

    # Compute the STFT
    audio_stft = zaf.stft(audio_signal, window_function, step_length)

    # Derive the magnitude spectrogram (without the DC component and the mirrored frequencies)
    audio_spectrogram = np.absolute(audio_stft[1:int(window_length / 2) + 1, :])

    # Display the spectrogram in dB, seconds, and Hz
    number_samples = len(audio_signal)
    # print(number_samples)
    # print(audio_stft.shape)
    # print(audio_spectrogram.shape)
    plt.figure(figsize=(17, 10))
    # plt.plot(np.arange(5), np.arange(5))
    zaf.specshow(audio_spectrogram, number_samples, sampling_frequency, xtick_step=1, ytick_step=1000)
    plt.title("Spectrogram (dB)")
    # plt.show()

    plt.savefig("{dir_name}/{song_name}.png".format(dir_name = SAVE_PATH, song_name = song_name[:len(song_name) - 4]))


