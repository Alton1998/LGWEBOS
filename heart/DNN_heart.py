# DNNClassifier on CSV input dataset.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import urllib

import numpy as np
import tensorflow as tf
old_v = tf.compat.v1.logging.get_verbosity()
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)
import pandas as pd 
# Data sets
TRAINING = "train.csv"
TEST = "test.csv"

def main():
  # Load datasets.
  training_set =pd.read_csv(TRAINING)
  
  test_set = pd.read_csv(TEST)

  # Specify that all features have real-value data
  feature_columns = [tf.contrib.layers.real_valued_column("", dimension=4)]

  # Build 3 layer DNN
  classifier = tf.contrib.learn.DNNClassifier(feature_columns=feature_columns,
                                              hidden_units=[5,10,5],
                                              n_classes=3)
  # Define the training inputs
  def get_train_inputs():
    x = tf.constant(np.array(training_set.drop('target',axis=1)))
    y = tf.constant(np.array(training_set['target']))

    return x, y

  # Fit model.
  classifier.fit(input_fn=get_train_inputs, steps=2000)

  # Define the test inputs
  def get_test_inputs():
    x = tf.constant(np.array(test_set.drop('target',axis=1)))
    y = tf.constant(np.array(test_set['target']))

    return x, y

  # Evaluate accuracy.
  accuracy_score = classifier.evaluate(input_fn=get_test_inputs,
                                       steps=1)["accuracy"]

  print("\nTest Accuracy: {0:f}\n".format(accuracy_score))

  # Classify new flower
  #def new_samples():
  #  return np.array([[6.4, 2.7, 5.6, 2.1]], dtype=np.float32)

  #predictions = list(classifier.predict(input_fn=new_samples))

  #print("Predicted class: {}\n".format(predictions))

if __name__ == "__main__":
    main()
