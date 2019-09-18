# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 17:19:52 2019

@author: utilisateur
"""

import pandas as pd
from sklearn.model_selection import train_test_split
import seaborn as sns; sns.set()
import statsmodels.api as sm
import pickle
data = pd.read_csv("Salary_Data.csv")


x = data.iloc[:,0].values
y = data.iloc[:,1].values
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0);
 


print('before' +str(x))
#x = sm.add_constant(x) # adding a constant
print('after' + str(x))
model = sm.OLS(y, x).fit()
predictions = model.predict(x) 
pickle.dump( model, open( "save.p", "wb" ) )
print_model = model.summary()
print(print_model)

