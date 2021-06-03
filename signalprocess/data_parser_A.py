import os
from pydub import AudioSegment
from pydub.utils import make_chunks

CHUNK_LENGTH = 4 * 1000 # chunk length in milliseconds, 10 seconds
TRAINING_DIR = "Train/Training_Wavs_A"

def main():
    #Export all of the individual chunks as wav files
    for song in os.listdir(TRAINING_DIR):
        song_name = str(song)
        if song_name == ".DS_Store":
            continue

        full_audio = AudioSegment.from_file("{dir_name}/{song_name}".format(dir_name = TRAINING_DIR, song_name = song_name), "wav")
        chunks = make_chunks(full_audio, CHUNK_LENGTH) #Make chunks of CHUNK_LENGTH

        limit = len(chunks) - 1

        for i, chunk in enumerate(chunks):
            if i == limit:
                break #cut off the last chunk as it may not be proper length

            # name chunk by where it starts in the wav file (second)
            chunk_name = "LFTrain/WAVs_A/{song_name}{start}.wav".format(song_name = song_name[:(len(song_name) - 4)], start = i*(CHUNK_LENGTH / 1000))
            print ("exporting", chunk_name)
            chunk.export(chunk_name, format="wav")

if __name__ == '__main__':
    main()
