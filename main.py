# importing files from src folder

from src.data_loader import housing_prices
# from src.analysis import analyze_data
# from src.visualization import visualize_data

df = housing_prices()
# results = analyze_data(df)
print(df)
# plot_regional(results)