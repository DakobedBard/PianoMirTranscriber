from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Conv2D, MaxPool2D, Flatten

def build_model(hp):
    model = Sequential()
    model.add(Conv2D(filters = 64, kernel_size = (3,3), kernel_initializer='normal', activation='relu', padding = 'same',input_shape=( 5,252,1)))
    model.add(MaxPool2D(pool_size =(2,2)))
    model.add(Dropout(.25))
    model.add(Flatten())
    model.add(Dense(128, activation='tanh'))
    model.add(Dropout(.2))
    model.add(Dense(88,kernel_initializer='normal', activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam')
    return model