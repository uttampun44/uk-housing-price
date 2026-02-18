# importing files from src folder

from src.data_loader import housing_prices
from src.analysis import analysis_data
# from src.visualization import visualize_data

df = housing_prices()
results = analysis_data(df)
# print(results.head())
# plot_regional(results)