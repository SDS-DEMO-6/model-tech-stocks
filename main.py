import pandas

data = pandas.read_csv(data_file_path, sep="\t")

data.set_index(["Date"])


