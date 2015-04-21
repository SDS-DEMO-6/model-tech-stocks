import pandas
import os
import json

data_file_path= os.environ["SDS_INPUT_PATH"]
out_file_path=os.environ["SDS_OUTPUT_PATH"]

data = pandas.read_csv(data_file_path, sep="\t")
data.set_index(["Date"])

data["score"] = (
  -38.6847 +
  0.853 * data["GOOG_LAG_1"] +
  2.0675 * data["DBC_LAG_1"] +
  0.6982 * data["QQQ_LAG_1"]
)

data.to_csv(out_file_path, sep="\t")


