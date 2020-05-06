from mir.generators.generator import DataGenerator

def test_generate_window_sample():
    generator = DataGenerator()
    batchx, batchy = generator.__getitem__(0)
    windowed_samples, spec = generator.generate_windowed_samples(batchx)
    s = windowed_samples[5, 2, :]
    s2 = windowed_samples[4, 3, :]
    assert all(s == s2)
    return windowed_samples


def testGenerator():
    i = 0
    generator = DataGenerator()
    while True:
        i += 1
        BatchX,Batchy = generator.__getitem__(0)


def test_generator_():
    generator = DataGenerator()
    while True:
        batchx, batchy = generator.__getitem__(0)
        print(batchx.shape)

        return batchx, batchy


x,y = test_generator_()