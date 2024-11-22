
# # Customer Behaviour Segmentation Analysis

# 1.0 Importing Libraries
# Import Python Libraries
%matplotlib inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(
    { "figure.figsize": (8, 6) },
    style='ticks',
    color_codes=True,
    font_scale=0.8
)
%config InlineBackend.figure_formats = set(('retina', 'svg'))
import warnings
warnings.filterwarnings('ignore')

# Adjust the display settings to ensure all columns are shown
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.width', None)        # Adjust the display width to accommodate all columns

# 2.0 Loading the Dataset

# Load dataset using panda read_csv to and check first three rows
df = pd.read_csv('Dataset_ecommerce.csv')
df.head()