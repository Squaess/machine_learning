import numpy as np

class Perceprton( object ):
  """Perceptron classifier.

  Parameters
  ------------
  eta : float
      Learning rate (between 0.0 and 1.0)
  n_iter : int
      Passes over the training dataset.
  Attributes
  -----------
  w_ : 1d-array
      Weights after fitting.
  errors_ : list
      Number of misclassifications (updates) in each epoch.

  """

  def _init_(self, eta=0.01, n_iter=10):
    self.eta = eta
    self.n_iter = n_iter

