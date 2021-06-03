import os # automating through directory
import numpy as np
import zaf
from PIL import Image
import matplotlib.pyplot as plt
import scipy

#TRAINING_DIR = "Train/WAVs_A"
#SAVE_PATH = "Train/MEL_A"
TRAINING_DIR = "Train/WAVs_A"
SAVE_PATH = "Train/MEL_A_Final_Rect"

for song in os.listdir(TRAINING_DIR):
    song_name = str(song)
    if song_name == ".DS_Store":
        continue

    # Read the audio signal (normalized) with its sampling frequency in Hz, and average it over its channels
    audio_signal, sampling_frequency = zaf.wavread("{dir_name}/{song_name}".format(dir_name = TRAINING_DIR, song_name = song_name))
    audio_signal = np.mean(audio_signal, 1)

    # Set the parameters for the Fourier analysis
    window_length = pow(2, int(np.ceil(np.log2(0.04*sampling_frequency))))
    window_function = scipy.signal.hamming(window_length, sym=False)
    step_length = int(window_length/2)

    # Compute the mel filterbank
    number_mels = 128
    mel_filterbank = zaf.melfilterbank(sampling_frequency, window_length, number_mels)
    #print(mel_filterbank.shape)

    # Compute the mel spectrogram using the filterbank
    mel_spectrogram = zaf.melspectrogram(audio_signal, window_function, step_length, mel_filterbank)

    # Display the mel spectrogram in dB, seconds, and Hz
    number_samples = len(audio_signal)
    # plt.figure(figsize=(10, 10))
    zaf.melspecshow(mel_spectrogram, number_samples, sampling_frequency, window_length, xtick_step=1)
    # plt.title("Mel spectrogram (dB)")
    # plt.show()

    plt.axis("off")
    plt.savefig("{dir_name}/{song_name}MEL.png".format(dir_name=SAVE_PATH,
                                                               song_name=song_name[:len(song_name) - 4]), pad_inches=0, bbox_inches="tight")

    #fig.patch.set_visible(False)
    #ax.axis('off')



    # im = Image.open(r"{dir_name}/{song_name}MEL.png".format(dir_name=SAVE_PATH,
    #                                                                 song_name=song_name[:len(song_name) - 4]))
    # width, height = im.size
    #
    # left = width * .125
    # right = width * .9
    # top = height * .125
    # bottom = height * .89
    #
    # cropped = im.crop((left, top, right, bottom))
    # cropped = cropped.resize((256, 256))
    # cropped.save(r"{dir_name}/{song_name}MEL.png".format(dir_name=SAVE_PATH,
    #                                                                  song_name=song_name[:len(song_name) - 4]))

    # temp = os.get(cd)

    # plt.savefig("{dir_name}/{song_name}MEL.png".format(dir_name = SAVE_PATH, song_name = song_name[:len(song_name) - 4]))
