import pandas
import os
import json

data_file_path= os.environ["SDS_INPUT_PATH"]
out_file_path=os.environ["SDS_OUTPUT_PATH"]

data = pandas.read_csv(data_file_path, sep="\t")
data["GOOG_DIFF_1"] = data["GOOG"].subtract(data["GOOG_LAG_1"])
data["GOOG_DIFF_2"] = data["GOOG_LAG_1"].subtract(data["GOOG_LAG_2"])
data["DBC_DIFF_2"] = data["DBC_LAG_1"].subtract(data["DBC_LAG_2"])
data["QQQ_DIFF_2"] = data["QQQ_LAG_1"].subtract(data["QQQ_LAG_2"])
data.set_index(["Date"])

data["score"]= (
  -0.14 + 
  -.0508 * data["GOOG_DIFF_2"] +
  0.7145* data["DBC_DIFF_2"] +
  0.7493 * data["QQQ_DIFF_2"] +
  data["GOOG_LAG_1"]
  )


data.to_csv(out_file_path, sep="\t")


