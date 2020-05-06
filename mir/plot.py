
import matplotlib.pyplot as plt
import librosa
import librosa.display
import numpy as np
file = './pair/swave.wav'
y, sr = librosa.load(file)
fmin = librosa.note_to_hz('C2')

cqt = np.abs(librosa.core.cqt(y, sr=sr, n_bins=252, bins_per_octave=36,fmin=fmin, norm=1))
plt.figure(figsize=(12, 8))
shortCQT = cqt[:2000]
librosa.display.specshow(shortCQT, y_axis='cqt_note')

import matplotlib.pyplot as plt
import librosa
y, sr = librosa.load(librosa.util.example_audio_file())
plt.figure(figsize=(12, 8))
CQT = librosa.amplitude_to_db(np.abs(librosa.cqt(y, sr=sr)), ref=np.max)
librosa.display.specshow(CQT, y_axis='cqt_note')

import matplotlib.pyplot as plt
import librosa.display
import numpy as np

y2 ,sr2 = librosa.load('./pair/swave.wav')
fmin = librosa.note_to_hz('C2')
cqt = np.abs(librosa.core.cqt(y2, sr=sr2, n_bins=252, bins_per_octave=36,fmin=fmin, norm=1))
shortCQT = cqt[:,:2500]
plt.figure(figsize=(12, 8))
librosa.display.specshow(shortCQT, y_axis='cqt_note')