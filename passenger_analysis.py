import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def clean_data(df):
    # Print the columns before renaming to debug
    print("Columns before renaming:", df.columns)
    
    # Rename columns to match expected names
    df = df.rename(columns={
        'DOB': 'Birthdate',
        'Class': 'TravelClass',
        'First Class': 'LoyaltyMember',
        'Flight Number': 'FlightNumber'
    })
    
    # Print the columns after renaming to debug
    print("Columns after renaming:", df.columns)
    
    # Check if 'Birthdate' column exists and is properly named
    if 'Birthdate' not in df.columns:
        raise KeyError("The 'Birthdate' column was not found after renaming.")
    
    # Handling missing values
    df = df.dropna()  # You can also use df.fillna() for imputation
    
    # Ensuring data types are appropriate
    df['Birthdate'] = pd.to_datetime(df['Birthdate'])
    df['LoyaltyMember'] = df['LoyaltyMember'].astype(bool)
    
    return df

def calculate_average_age(df, travel_class):
    filtered_df = df[df['TravelClass'] == travel_class]
    average_age = filtered_df['Birthdate'].apply(lambda x: (pd.Timestamp.now() - x).days // 365).mean()
    return average_age

def find_loyalty_members(df):
    loyalty_members = df[df['LoyaltyMember'] == True]['Name'].tolist()
    return loyalty_members

def get_class_statistics(df):
    class_stats = {}
    for travel_class in df['TravelClass'].unique():
        class_df = df[df['TravelClass'] == travel_class]
        average_age = class_df['Birthdate'].apply(lambda x: (pd.Timestamp.now() - x).days // 365).mean()
        loyalty_members = class_df[class_df['LoyaltyMember'] == True].shape[0]
        class_stats[travel_class] = {'Average Age': average_age, 'Loyalty Members': loyalty_members}
    return class_stats

def plot_age_distribution(df):
    ages = df['Birthdate'].apply(lambda x: (pd.Timestamp.now() - x).days // 365)
    plt.hist(ages, bins=20, edgecolor='black')
    plt.title('Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Number of Passengers')
    plt.savefig('age_distribution.png')
    plt.show()

def plot_average_age_by_class(df):
    class_stats = get_class_statistics(df)
    classes = list(class_stats.keys())
    avg_ages = [class_stats[cls]['Average Age'] for cls in classes]
    
    plt.bar(classes, avg_ages, color='blue')
    plt.title('Average Age by Travel Class')
    plt.xlabel('Travel Class')
    plt.ylabel('Average Age')
    plt.savefig('average_age_by_class.png')
    plt.show()

def plot_age_vs_loyalty(df):
    df['Age'] = df['Birthdate'].apply(lambda x: (pd.Timestamp.now() - x).days // 365)
    sns.scatterplot(x='Age', y='LoyaltyMember', data=df)
    plt.title('Age vs Loyalty Membership')
    plt.savefig('age_vs_loyalty.png')
    plt.show()

def plot_age_distribution_by_class(df):
    df['Age'] = df['Birthdate'].apply(lambda x: (pd.Timestamp.now() - x).days // 365)
    fig = px.box(df, x='TravelClass', y='Age', title='Age Distribution by Travel Class')
    fig.write_image('age_distribution_by_class.png')
    fig.show()
