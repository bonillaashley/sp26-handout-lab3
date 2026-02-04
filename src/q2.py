"""
We will use the same dataset as last time, spam.csv.
The original dataset is available at 
https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset
Please ignore the rows that do not follow the correct format.

Implement this class to analyze the data according to the documentation.

You are not required to test visualizations, so you are not required to
write tests for this problem. If you are curious, there is a test that
you can read in test_q2.py.
"""

import sys
sys.path.append(".")
import pandas as pd
import matplotlib.pyplot as plt
from src.q1 import SpamReader # SpamReader.get_dictionary() may be useful here

class SpamPlotter:
    """A class to plot word frequencies in spam and ham messages."""
    def __init__(self, df: pd.DataFrame) -> None:
        """
        Store the provided dataframe.

        Args:
            df (pd.DataFrame): A dataframe containing the spam dataset.
        
        Raises:
            ValueError: If the dataframe does not contain the columns 'v1' and 'v2'
        """
        self.df = df

    def plot_word_frequencies(self) -> None:
        """
        For each word in the dictionary (from get_dictionary()), count the number of times
        that it appears in spam, and the number of times that it appears in ham.
        Plot it with ham on the x axis and spam on the y axis.
        """
        # Hints:
        #  - At some point, call get_dictionary() from SpamReader (from q1).
        #  - Create a helper method to separate out the logic for computing the counts.
        #    It should, for each word in the dictionary, count how often it appears
        #    in ham, and how often it appears in spam.
        #  - Then, in this method, call your helper method, and make the plot.
        pass
