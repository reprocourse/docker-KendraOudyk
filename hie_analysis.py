# LOAD PACKAGES
import pandas as pd
import numpy as np
from statsmodels.formula.api import MNLogit
import argparse

# LOAD DATA
## allow user to specify the path
parser = argparse.ArgumentParser(description='Process a csv file.')
parser.add_argument('file')
args = parser.parse_args()

hie = pd.read_csv(args.file, na_values='nd')
#hie = pd.read_csv('./data/hie_data.csv', na_values='nd')

# DEFINE VARIABLES
## predictors (copeptin, NSE, and intercept)
x = hie[['copeptin_6h_pmol_l','NSE_6h_ng_ml']]
x['intercept'] = 1.0

## outcome
y = hie['outcome']

# ANALYSIS
model = MNLogit(y,x,missing='drop')
model_fit = model.fit()

# RESULTS
print(model_fit.summary())

