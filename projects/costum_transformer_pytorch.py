## costum transformer
class Rescale(object):
  def __init__(self, output_size):
    assert isinstance(output_size, (int, tuple))
    self.output_size = output_size

  def __call__(self, sample):
      img = sample.resize((self.output_size, self.output_size)) ##desired transform

      return img
