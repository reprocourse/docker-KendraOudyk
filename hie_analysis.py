# LOAD PACKAGES
import pandas as pd
import numpy as np
from statsmodels.formula.api import MNLogit
import argparse

# SET UP ARGPARSER to allow user to specify the path
parser = argparse.ArgumentParser(description='Process a csv file.')
parser.add_argument('file',help='name of the csv file containing the data')
parser.add_argument('--not_a_number','-n',help='value for absent numbers in the data')

args = parser.parse_args()

# LOAD DATA
hie = pd.read_csv(args.file, na_values=args.not_a_number)

# DEFINE VARIABLES
#  predictors (copeptin, NSE, and intercept)
x = hie[['copeptin_6h_pmol_l','NSE_6h_ng_ml']]
x['intercept'] = 1.0

# outcome (i.e., death, etc)
y = hie['outcome'] 

# ANALYSIS
model = MNLogit(y,x,missing='drop')
model_fit = model.fit()

# RESULTS
print(model_fit.summary())

