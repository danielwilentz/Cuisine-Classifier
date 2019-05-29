"""
Note this file contains _NO_ flask functionality.
Instead it makes a file that takes the input dictionary Flask gives us,
and returns the desired result.

This allows us to test if our modeling is working, without having to worry
about whether Flask is working. A short check is run at the bottom of the file.
"""

from joblib import dump, load
import numpy as np
import pandas as pd

# open our vectorizer and model with joblib
nmf = load('../models/nmf_tf_idf_model')
vectorizer = load('../models/tf_idf')

topics = ['Burger', 'Pizza', 'Asian Fusion', 'Dessert', 'Breakfast', 'American Entree']

def make_prediction(text):
    """
    Input:
    feature_dict: a dictionary of the form {"feature_name": "value"}

    Function makes sure the features are fed to the model in the same order the
    model expects them.

    Output:
    Returns (x_inputs, probs) where
      x_inputs: a list of feature values in the order they appear in the model
      probs: a list of dictionaries with keys 'name', 'prob'
    """
    text_vect = vectorizer.transform([text])
    result = nmf.transform(text_vect)
    return text, topics[np.argmax(result)]


# This section checks that the prediction code runs properly
# To run, type "python predictor_api.py" in the terminal.
#
# The if __name__='__main__' section ensures this code only runs
# when running this file; it doesn't run when importing
if __name__ == '__main__':
    print('hello world')
    test = 'mozzarella and olives with pepperoni and anchovies'
    print('the test is: {}'.format(test))
    print()
    print('making a prediction on this test:')
    print(make_prediction(test))
