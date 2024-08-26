import warnings
from typing import Tuple

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


from sklearn.metrics import roc_auc_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import validation_curve, learning_curve
