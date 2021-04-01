import pandas as pd

def process_data_1(path):
    dataset = pd.read_csv(path)
    features_1 = dataset[['review_scores_rating', 'price', 'property_type', 'neighbourhood_cleansed', 'host_is_superhost']]
    features_1['price'] = features_1['price'].str.replace('$', '').str.replace(',', '').astype('float64')
    features_1 = features_1.dropna()
    return features_1

def process_data_2(path):
    dataset = pd.read_csv(path)
    features_1 = dataset[['availability_30', 'availability_60', 'availability_90', 'instant_bookable']]
    features_1 = features_1.dropna()
    return features_1

def process_data_3(path):
    dataset = pd.read_csv(path)
    features_1 = dataset[['calculated_host_listings_count', 'reviews_per_month']]
    features_1 = features_1.dropna()
    return features_1

def popular_locations(df):
    return df[df['neighbourhood_cleansed'].isin(['Downtown/Civic Center', 'Mission', 'Western Addition', 'South of Market', 'Castro/Upper Market', 'Bernal Heights', 'Haight Ashbury', 'Noe Valley', 'Outer Sunset', 'Nob Hill'])]

def chosen_locations(df):
    return df[df['neighbourhood_cleansed'].isin(['Castro/Upper Market', 'Bernal Heights', 'Outer Sunset'])]