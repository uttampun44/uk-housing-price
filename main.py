# importing files from src folder

from src.data_loader import housing_prices_data
from src.analysis import analysis_data, filter_regions, get_yearly_average_price, calculate_growth
from src.visualization import plot_regional_prices, plot_house_types
from src.prediction import predict_future_prices


df = housing_prices_data()
results = analysis_data(df)
results = filter_regions(results)
df_yearly = get_yearly_average_price(results)
df_yearly = calculate_growth(df_yearly)

plot_regional_prices(df_yearly)
plot_house_types(df)
predict_future_prices(df_yearly)