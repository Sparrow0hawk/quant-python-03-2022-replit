import pandas as pd

# load our data file and assign it
surveys_df = pd.read_csv("surveys.csv")

# describe the weight column
desc_weight = surveys_df["weight"].describe()

# print out the summary statistics
print(desc_weight)
