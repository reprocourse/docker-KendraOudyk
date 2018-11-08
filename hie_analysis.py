# LOAD PACKAGES
import pandas as pd
import numpy as np
from statsmodels.formula.api import MNLogit

# LOAD DATA
hie = pd.read_csv('hie_data.csv', na_values='nd')

# DEFINE VARIABLES
## predictors (copeptin, NSE, and intercept)
x = hie[['copeptin_6h_pmol_l','NSE_6h_ng_ml']]
x['intercept'] = 1.0

## outcome options
### single column with all four categories
y_1col = hie['outcome']

### multiple columns (dummy variable for each category)
y_multicols = pd.DataFrame({'healthy':y_1col=='0', 'moderate':y_1col=='1', 'severe':y_1col=='2e', 'death':y_1col=='3'}) 

### multiple columns - with column putting all in one group
col1s = pd.Series(np.ones(len(x)))
coltrues = col1s>0 # turn column of 1's into column of 'true's
y_multicols_withallin1 = pd.DataFrame({'allin1group':coltrues, 'healthy':y_1col=='0', 'moderate':y_1col=='1', 'severe':y_1col=='2e', 'death':y_1col=='3'})

### multiple columns with allin1group column - without one group 
y_multicols_withallin1_drop1group = pd.DataFrame({'allin1group':coltrues, 'healthy':y_1col=='0', 'moderate':y_1col=='1', 'severe':y_1col=='2e'})#, 'death':y_1col=='3'})

# CHOOSE Y
y = y_1col
#y = y_multicols
#y = y_multicols_withallin1
#y = y_multicols_withallin1_drop1group

# ANALYSIS
model = MNLogit(y,x,missing='drop')
model_fit = model.fit()

# RESULTS
print(model_fit.summary())

## y_1col and y_multicols give the same results
## y_multicols_withallin1 doesn't work 
## y_multicols_withallin1_drop1group doesn't work
