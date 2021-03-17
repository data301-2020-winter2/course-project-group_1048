import pandas as pd

def process_data(path):
    dataset = pd.read_csv(path)
    features_1 = dataset[['review_scores_rating', 'price', 'property_type', 'neighbourhood_cleansed', 'host_is_superhost']]
    features_1['price'] = features_1['price'].str.replace('$', '').str.replace(',', '').astype('float64')
    features_1 = features_1.dropna()
    return features_1

def popular_locations(df):
    return df[df['neighbourhood_cleansed'].isin(['Downtown/Civic Center', 'Mission', 'Western Addition', 'South of Market', 'Castro/Upper Market', 'Bernal Heights', 'Haight Ashbury', 'Noe Valley', 'Outer Sunset', 'Nob Hill'])]

def chosen_locations(df):
    return df[df['neighbourhood_cleansed'].isin(['Castro/Upper Market', 'Bernal Heights', 'Outer Sunset'])]