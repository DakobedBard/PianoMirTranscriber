'''
This script will train the model and save the model to S3

'''

from mir.generators.generator import DataGenerator,datagenerator
from math import floor
from mir.models.cnn import build_model
'''
a Keras data generator is meant to loop infinitely — it should never return or exit.

'''
#
# # generator = DataGenerator()
# valgenerator = DataGenerator(train=False)

batch_size = 32
model = build_model(None)
num_epochs = 10

model.fit_generator(generator=datagenerator(32),
                    epochs=num_epochs,
                    steps_per_epoch = floor(8382182/batch_size),
                    verbose=1,
                    use_multiprocessing=True,
                    workers=16,
                    validation_data = datagenerator(32,False),
                    validation_steps = floor(888281/batch_size),
                    max_queue_size=32)

