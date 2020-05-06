from keras.utils import Sequence
from random import shuffle
import numpy as np
from mir.data_utilities.process_files import load_transform_and_annotation
from mir.data_utilities.process_annotation import generate_annotation_matrix


def datagenerator(batchsize, train=True):
    def init_file_queue():
        if train:
            fileQueue = list(range(1000))
            fileQueue = set(fileQueue)
            fileQueue.remove(835)  # This file was not processed correctly
            fileQueue = list(fileQueue)
            shuffle(fileQueue)
        else:
            fileQueue = list(range(1000, 1270))
            shuffle(fileQueue)
            fileQueue = set(fileQueue)
        return fileQueue

    def stitch(next_spec, next_annotation):
        '''
        This method will handle the case when the generator reaches the end of one spectogram and stitch together
        the samples from the next.
            Calculate how many samples of the next spectogram I need to grab. Then set the current_spectogra_index to this value
            This method will be called when the spectogram gets pulled off the queue requiring the need to stitch together the spectograms
        '''

        n_samples = batchsize + currentIndex - x.shape[0]  # Number of samples in next spectogram
        prev_n_samples = batchsize - n_samples  # Number of samples in the previous spectogram

        spec1 = x[-prev_n_samples:]
        spec2 = next_spec[:n_samples]
        batchx = np.concatenate((spec1, spec2), axis=0)

        annotation1 = y[-prev_n_samples:]
        annotation2 = next_annotation[:n_samples]
        batchy = np.concatenate((annotation1, annotation2), axis=0)

        return batchx, batchy, next_spec, next_annotation, n_samples

    def generate_windowed_samples(spec):
        '''
        This method creates the context window for a sample at time t, Wi-2, Wi-1, Wi, Wi+1,Wi+2
        '''
        windowed_samples = np.zeros((spec.shape[0], 5, spec.shape[1]))
        for i in range(spec.shape[0]):
            if i <= 1:
                windowed_samples[i] = np.zeros((5, spec.shape[1]))
            elif i >= spec.shape[0] - 2:
                windowed_samples[i] = np.zeros((5, spec.shape[1]))
            else:
                windowed_samples[i, 0] = spec[i - 2]
                windowed_samples[i, 1] = spec[i - i]
                windowed_samples[i, 2] = spec[i]
                windowed_samples[i, 3] = spec[i + 1]
                windowed_samples[i, 4] = spec[i + 2]
        return windowed_samples

    fileQueue = init_file_queue()
    fileID = fileQueue.pop()
    x, annotation = load_transform_and_annotation(fileID, fft='cqt')
    x = generate_windowed_samples(x)
    y = generate_annotation_matrix(annotation, x.shape[0])
    currentIndex = 0

    while True:
        if currentIndex > x.shape[0] - batchsize:
            if len(fileQueue) == 0:
                init_file_queue()
            next_spec_id = fileQueue.pop()
            # print("Processing the next fiel with id {}".format(next_spec_id))
            # print("Length of the queue is {}".format(len(fileQueue)))
            x, annoation = load_transform_and_annotation(next_spec_id, fft='cqt')
            nextSpec = generate_windowed_samples(x)
            batchx, batchy, x, y, currentIndex = stitch(nextSpec,
                                                        generate_annotation_matrix(annoation, nextSpec.shape[0]))
            yield batchx.reshape((batchx.shape[0], batchx.shape[1], batchx.shape[2], 1)), batchy
        else:
            batchx = x[currentIndex:currentIndex + batchsize]
            batchy = y[currentIndex:(currentIndex + batchsize)]
            currentIndex = currentIndex + batchsize
            yield batchx.reshape((batchx.shape[0], batchx.shape[1], batchx.shape[2], 1)), batchy





class DataGenerator(Sequence):

    def init_file_queue(self):
        if self.train:
            fileQueue = list(range(1000))
            self.fileQueue = set(fileQueue)
            self.fileQueue.remove(835)  # This file was not processed correctly
            self.fileQueue = list(fileQueue)
            shuffle(self.fileQueue)
        else:
            fileQueue = list(range(1000, 1270))
            shuffle(fileQueue)
            self.fileQueue = set(fileQueue)

    def __init__(self, batchsize=32, train=True):
        self.train = train
        self.init_file_queue()
        self.batchsize = batchsize
        fileID = self.fileQueue.pop()
        x, annotation = load_transform_and_annotation(fileID, fft='cqt')
        self.x = self.generate_windowed_samples(x)
        self.y = generate_annotation_matrix(annotation, self.x.shape[0])

        self.currentIndex = 0

    def __len__(self):
        pass

    def __getitem__(self, item):

        if self.currentIndex > self.x.shape[0] - self.batchsize:
            if len(self.fileQueue) == 0:
                print("END OF THE EPOCH")
                self.init_file_queue()

            next_spec_id = self.fileQueue.pop()
            print("Processing the next fiel with id {}".format(next_spec_id))
            print("Length of the queue is {}".format(len(self.fileQueue)))
            x, annoation = load_transform_and_annotation(next_spec_id, fft='cqt')
            nextSpec = self.generate_windowed_samples(x)
            batchx, batchy = self.stitch(nextSpec, generate_annotation_matrix(annoation, nextSpec.shape[0]))
            return batchx.reshape((batchx.shape[0], batchx.shape[1], batchx.shape[2], 1)), batchy
        else:
            batchx = self.x[self.currentIndex:self.currentIndex + self.batchsize]
            batchy = self.y[self.currentIndex:(self.currentIndex + self.batchsize)]
            self.currentIndex = self.currentIndex + self.batchsize
            return batchx.reshape((batchx.shape[0], batchx.shape[1], batchx.shape[2], 1)), batchy

    def on_epoch_end(self):
        self.init_file_queue()

    def stitch(self, next_spec, next_annotation):
        '''
        This method will handle the case when the generator reaches the end of one spectogram and stitch together
        the samples from the next.
            Calculate how many samples of the next spectogram I need to grab. Then set the current_spectogra_index to this value
            This method will be called when the spectogram gets pulled off the queue requiring the need to stitch together the spectograms
        '''

        n_samples = self.batchsize + self.currentIndex - self.x.shape[0]  # Number of samples in next spectogram
        prev_n_samples = self.batchsize - n_samples  # Number of samples in the previous spectogram

        spec1 = self.x[-prev_n_samples:]
        spec2 = next_spec[:n_samples]
        batchx = np.concatenate((spec1, spec2), axis=0)

        annotation1 = self.y[-prev_n_samples:]
        annotation2 = next_annotation[:n_samples]
        batchy = np.concatenate((annotation1, annotation2), axis=0)

        self.x = next_spec
        self.y = next_annotation
        self.currentIndex = n_samples

        return batchx, batchy

    def generate_windowed_samples(self, spec):
        '''
        This method creates the context window for a sample at time t, Wi-2, Wi-1, Wi, Wi+1,Wi+2
        '''
        windowed_samples = np.zeros((spec.shape[0], 5, spec.shape[1]))
        for i in range(spec.shape[0]):
            if i <= 1:
                windowed_samples[i] = np.zeros((5, spec.shape[1]))
            elif i >= spec.shape[0] - 2:
                windowed_samples[i] = np.zeros((5, spec.shape[1]))
            else:
                windowed_samples[i, 0] = spec[i - 2]
                windowed_samples[i, 1] = spec[i - i]
                windowed_samples[i, 2] = spec[i]
                windowed_samples[i, 3] = spec[i + 1]
                windowed_samples[i, 4] = spec[i + 2]
        return windowed_samples
