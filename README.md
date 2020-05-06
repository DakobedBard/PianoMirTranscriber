In this project I am attempting to perform automatic music transcription of piano music (Produce piano sheet music from recordings of piano music).  Initially I had intended to do this with guitar data and produce guitar tablature, yet this introduces the added complexity that there is not a one to one mapping between notes on the guitar and a guitar tab (each note can be played
in multiple places) unlike on the piano.  

Preprocessing:
- Use the librosa library to perform a constant q transform for each input audio file
   librosa.amplitude_to_db(np.abs(librosa.core.cqt(y, sr=sr, n_bins=252, bins_per_octave=36, fmin=fmin, norm=1))).T 
   - Additionally, we compute the mean and standard deviation of each dimension over the training set and transform
    the data by subtracting the mean and diving by the standard deviation
    - In order to compute the standard deviation and mean of each dimension in the input spectograms , I make use of an approach known as Welford's algorithm to compute these values because the data is unable to fit into memory. 
- For each associated midi file, extract the notes and convert into a one hot encoded binary matrix




Using the archtitecture proposed by Manuel Carretero Minguez
 https://rua.ua.es/dspace/bitstream/10045/76991/1/Automatic_music_transcription_using_neural_networks_MINGUEZ_CARRETERO_MANUEL.pdf 
 
and using techniques derived from this paper from Siddharth Sigtia, Emmanouil Benetos, and Simon Dixon
https://arxiv.org/pdf/1508.01774.pdf 
 
 timidity data/MIDI-Unprocessed_R1_D1-1-8_mid--AUDIO-from_mp3_02_R1_2015_wav--6.midi
 
 Midi control messages 
 64 -> damper pedal
67 -> soft pedal

aws s3 ls s3://maestro-transforms --recursive  | grep -v -E "(Bucket: |Prefix: |LastWriteTime|^$|--)" | awk 'BEGIN {total=0}{total+=$3}END{print total/1024/1024" MB"}'
