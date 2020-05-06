from mir.data_utilities.process_midi import extract_notes
import numpy as np
import librosa
import os
import pandas as pd
import boto3

import concurrent.futures

def process_wav_midi_pair(midi_file, wav_file, filedID):
    prefix = 'train' if filedID < 1000 else 'test'
    path_ = '{}/fileID{}'.format(prefix, filedID)
    s3 = boto3.client('s3')
    bucket = 'maestro-transforms'
    fmin = librosa.note_to_hz('C2')
    if not os.path.isdir(path_):
        os.mkdir(path_)
    y, sr = librosa.load('{}'.format(wav_file))
    cqt =  librosa.amplitude_to_db(np.abs(librosa.core.cqt(y, sr=sr, n_bins=252, bins_per_octave=36, fmin=fmin, norm=1))).T
    spec = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max).T
    # notes = extract_notes('{}/{}'.format(data_folder_, midi_file))
    # notesDF = pd.DataFrame(notes)

    cqt_file = '{}/cqt.npy'.format(path_)
    spec_file = '{}/stft.npy'.format(path_)
    annotation_file = '{}/annotation.npy'.format(path_)
    for file, array in [(cqt_file,cqt)]: # ,(spec_file, spec), (annotation_file, notesDF.values)]:
        np.save(file, arr=array)
        with open(file, "rb") as f:
            s3.upload_fileobj(f, bucket, file)

    # for file, array in [(cqt_file,cqt),(spec_file, spec), (annotation_file, notesDF.values)]:
    #     if not os.path.isfile(file):
    #         np.save(file, arr=array)
    #         with open(file, "rb") as f:
    #             s3.upload_fileobj(f, bucket, file)
    print("Processed file {}".format(filedID))

def uploadS3(cqt_file, spec_file, annotation):
    s3 = boto3.client('s3')
    bucket = 'maestro-transforms'
    for file in [cqt_file, spec_file, annotation]:
        with open(file, "rb") as f:
            s3.upload_fileobj(f, bucket, file)

def generate_midi_wav_file_pairs():
    folders  =['2013','2011','2006','2017','2015','2008', '2009', '2014', '2018', '2004']
    data_folder = 'data/maestro-v2.0.0/'
    folders = [data_folder + folder for folder in folders]
    count = 0
    file_pairs = []

    for folder in folders:
        files = os.listdir("{}".format(folder))
        files.sort()
        for i in range(0, len(files), 2):
            if files[i][:-4] == files[i + 1][:-3]:
                file_pairs.append((folder + '/' + files[i], folder + '/' + files[i + 1]))
    return file_pairs

def process_data(file_pairs):
    bucket = 'maestro-transforms'
    s3 = boto3.client('s3')

    prefix = 'train'
    for i, pair in enumerate(file_pairs):
        if i> len(file_pairs) * 70:
            prefix ='test'
        if i> len(file_pairs) * 2:
            break
        # Try with just 4 octaves for the cqt...
        path_ = '{}/filedID{}'.format(prefix, i)

        if os.path.isdir(path_) == False:
            os.mkdir(path_)
        process_wav_midi_pair(pair, path_)
        # key = "{}/file{}".format(prefix, i)
        # url = 's3://{}'.format(bucket, key)
        print('Done writing to {}')


data_folder = 'data/maestro-v2.0.0/'
pairs = generate_midi_wav_file_pairs()

for i, pair in enumerate(pairs[1137:]):
    process_wav_midi_pair(pair[0], pair[1],i+1137)


# start_time = time.time()
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     results = [executor.submit(*pairID) for pairID in pair_ids]
#     # for f in concurrent.futures.as_completed(results):
#     #     print(f.result())
# print('Time Taken:', time.strftime("%H:%M:%S",time.gmtime(seconds)))