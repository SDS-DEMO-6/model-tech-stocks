import pandas 
import statsmodels.formula.api

import matplotlib
import matplotlib.pyplot as plt
import pylab
import statsmodels.stats.outliers_influence
from pandas.tools.plotting import autocorrelation_plot

# A script used to train the model. 
# Training scripts (and this code) 
# are not run by Ship Data Science. 
# Ship Data Science only requires 
# scoring code, here included in main.py .
# This file included only for informational 
# purposes.

data_file_path = "/data/ystock_2.txt"

data = pandas.read_csv(data_file_path, sep="\t")

data["GOOG_DIFF_1"] = data["GOOG"].subtract(data["GOOG_LAG_1"])
data["GOOG_DIFF_2"] = data["GOOG_LAG_1"].subtract(data["GOOG_LAG_2"])
#data["GOOG_DIFF_2"] = data["GOOG_LAG_2"].subtract(data["GOOG_LAG_3"])
data["DBC_DIFF_2"] = data["DBC_LAG_1"].subtract(data["DBC_LAG_2"])
data["QQQ_DIFF_2"] = data["QQQ_LAG_1"].subtract(data["QQQ_LAG_2"])

formula = """
  GOOG_DIFF_1 ~ 
  GOOG_DIFF_2 + 
  DBC_DIFF_2 +
  QQQ_DIFF_2 
  """

fit = statsmodels.formula.api.ols(formula=formula, data=data).fit()

print fit.summary()

data["SCORE"]= (
  -0.14 + 
  -.0508 * data["GOOG_DIFF_2"] +
  0.7145* data["DBC_DIFF_2"] +
  0.7493 * data["QQQ_DIFF_2"] +
  data["GOOG_LAG_1"]
  )

matplotlib.style.use('ggplot')
data.plot(x="Date", y=["GOOG", "SCORE"] )
#data.plot(x="Date", y="GOOG_DIFF_1" )
pylab.show()

print "########\n"

print data["GOOG_DIFF_1"].autocorr()
print data["GOOG_DIFF_1"].corr(data["GOOG_LAG_1"])
print data["GOOG_DIFF_1"].corr(data["GOOG_DIFF_2"])
print data["GOOG_DIFF_1"].corr(data["DBC_LAG_1"])
print data["GOOG_DIFF_1"].corr(data["QQQ_LAG_1"])
print data["GOOG_DIFF_1"].corr(data["DBC_DIFF_2"])
print data["GOOG_DIFF_1"].corr(data["QQQ_DIFF_2"])
#autocorrelation_plot(data["GOOG_LAG_1" ] )
#pylab.show()

print "done"


