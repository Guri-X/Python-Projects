import pandas as pd

nba = pd.read_csv("nba_all_elo.csv")
print(type(nba)) #Type of object
print("\n")

print("The total number of rows in this file are:")
print(len(nba))
print("\n")

print("The dimensionality of this file is:")
print(nba.shape)
print("\n")

print("The first 5 rows of the dataset are:")
print(nba.head())
print("\n")
