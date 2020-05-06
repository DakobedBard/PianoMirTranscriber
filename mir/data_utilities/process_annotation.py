import numpy as np
import librosa
from mir.data_utilities.process_midi import extract_notes
import pandas as pd
from librosa import time_to_frames


def generate_annotation_matrix(annotation, frames):
    '''
    This function will return a one hot encoded matrix of notes being played
    The annotation matrix will start w/ note 25 at index 0 and go up to note 100
    The highest and lowest values that I saw in the annotations seemed to be arounnd 29-96 so give a little leeway
    :return:
    '''
    annotation_matrix = np.zeros((88, frames))
    for note in annotation:
        starting_frame = time_to_frames(note[1])
        duration_frames = time_to_frames(note[2] - note[1])
        note_value = note[0]
        annotation_matrix[note_value - 25][starting_frame:starting_frame + duration_frames] = 1

    return annotation_matrix.T

def inverse_annotation_matrix(annotation_matrix):
    '''
    This function will return a list of notes from an annotation
    :return:
    '''
    pass