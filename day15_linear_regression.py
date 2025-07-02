import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

weather_df=pd.read_csv("weather.csv")

X = weather_df[["day_number", "humidity", "wind"]]
Y= weather_df[["temperature"]]

