from mir.generators.generator import generate_annotation_matrix
from mir.generators.generator import load_transform_and_annotation
from librosa import time_to_frames
import numpy as np


x,annotation = load_transform_and_annotation(0)
y = generate_annotation_matrix(annotation, x.shape[0])
#annotation_matrix = np.zeros((75, frames))

