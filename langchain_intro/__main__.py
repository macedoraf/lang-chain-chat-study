import polars as pl

HOSPITAL_DATA_PATH = "data/physicians.csv"
data_hospitals = pl.read_csv(HOSPITAL_DATA_PATH)
data_hospitals.shape
print(data_hospitals.head())