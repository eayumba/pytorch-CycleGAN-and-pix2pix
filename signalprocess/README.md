This folder contains all the signal processing / data processing that was done to train our CycleGAN. 

You must create a folder Train in this same directory. Train is the folder where our data is stored. In Train, you must create subfolders: 
	CQT (optional)
	STFT (optional)
	MEL_A_Final_Rect
	MEL_B_Final_Rect
	MEL_C_Final_Rect
	Training_Wavs_A
	Training_Wavs_B
	Training_Wavs_C
	WAVs_A
	WAVs_B
	WAVs_C

Train/Training_Wavs_A contains the raw ~1.5 hour long .wav file from the Lo-Fi genre. 
	% https://www.youtube.com/watch?v=-FlxM_0S2lA&ab_channel=LofiGirl
Train/Training_Wavs_B contains the raw ~1 hour long .wav file from the Trap genre. 
	% https://www.youtube.com/watch?v=nMD4eg5VKkE&ab_channel=Sh1nobiBeats
Train/Training_Wavs_C contains the raw ~2 hour long .wav file from the R\&B genre. 
	% https://www.youtube.com/watch?v=2vnePeBIP2U&ab_channel=TomSmith
Train/WAVs_A is the first file cut into 4 second chunks. 
Train/WAVs_B is the second file cut into 4 second chunks. 
Train/WAVs_C is the third file cut into 4 second chunks. 

CQT and STFT are test folders for when we had done the CQT and STFT transforms. They should respectively have CQT and STFT spectrograms. 

MEL_X_Final_Rect contain the spectrograms for each genre. It produces as many spectrograms as there are 4-second chunks, in each respective file. 


%% CODE %% 

* zaf.py is written by Zafar Rafii that provides a set of signal processing transforms, like short-time fourier transform (STFT), constant-Q transform (CQT), and others. 

* data_parser_X.py takes the long waveform in Train/Training_Wavs_X and cuts it into 4 second chunks and places them in WAVs_X 

* melspectrogramdirX.py takes each 4 second .wav from WAVs_X and computes the MEL transform and places them into MEL_X_Final_Rect. 

* CQTdir.py computes the CQT transform for all 4 second .wav files of a specific genre. You will have to manually change the train and save paths, as we are no longer doing these transforms. 

* STFTdir.py computes the STFT transform for all 4 second .wav files of a specific genre. You will have to manually change the train and save paths, as we are no longer doing these transforms. 

