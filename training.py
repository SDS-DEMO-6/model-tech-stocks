import pandas 
import statsmodels.formula.api
import statsmodels.stats.outliers_influence

# A script used to train the model. 
# Training scripts (and this code) 
# are not run by Ship Data Science. 
# Ship Data Science only requires 
# scoring code, here included in main.py .
# This file included only for informational 
# purposes.

data_file_path = "/data/ystocks.txt"

data = pandas.read_csv(data_file_path, sep="\t")

formula = """
  GOOG ~ GOOG_LAG_1 + 
  DBC_LAG_1 + 
  QQQ_LAG_1  
  """

fit = statsmodels.formula.api.ols(formula=formula, data=data).fit()

print fit.summary()



