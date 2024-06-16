import passenger_analysis as pa

def main():
    # Provide the correct path to your CSV file
    file_path = '/Users/ronnypatel/Desktop/School/CPS 3320/Project 1 Flight/Task 3/passengers.csv'
    
    # Load the data
    try:
        df = pa.load_data(file_path)
        print("Data loaded successfully.")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return
    
    # Print the first few rows of the dataframe to check the load
    print("Initial DataFrame:")
    print(df.head())
    
    # Print the column names to verify they are as expected
    print("Column names in the DataFrame:")
    print(df.columns)
    
    # Clean the data
    try:
        df = pa.clean_data(df)
        print("Data cleaned successfully.")
    except Exception as e:
        print(f"Error in cleaning data: {e}")
        return
    
    # Print the first few rows of the cleaned dataframe to check the cleaning process
    print("Cleaned DataFrame:")
    print(df.head())
    
    # Calculate average age for a specific travel class
    travel_class = 'ECONOMY'  # Example travel class
    try:
        avg_age = pa.calculate_average_age(df, travel_class)
        print(f'Average age for {travel_class} class: {avg_age}')
    except Exception as e:
        print(f"Error in calculating average age: {e}")
        return
    
    # Find loyalty members
    try:
        loyalty_members = pa.find_loyalty_members(df)
        print('Loyalty members:', loyalty_members)
    except Exception as e:
        print(f"Error in finding loyalty members: {e}")
        return
    
    # Get class statistics
    try:
        class_stats = pa.get_class_statistics(df)
        print('Class statistics:', class_stats)
    except Exception as e:
        print(f"Error in getting class statistics: {e}")
        return
    
    # Plot age distribution
    try:
        pa.plot_age_distribution(df)
        print("Age distribution plot created successfully.")
    except Exception as e:
        print(f"Error in plotting age distribution: {e}")
        return
    
    # Plot average age by travel class
    try:
        pa.plot_average_age_by_class(df)
        print("Average age by class plot created successfully.")
    except Exception as e:
        print(f"Error in plotting average age by class: {e}")
        return
    
    # Plot age vs loyalty membership
    try:
        pa.plot_age_vs_loyalty(df)
        print("Age vs loyalty membership plot created successfully.")
    except Exception as e:
        print(f"Error in plotting age vs loyalty membership: {e}")
        return
    
    # Plot age distribution by class
    try:
        pa.plot_age_distribution_by_class(df)
        print("Age distribution by class plot created successfully.")
    except Exception as e:
        print(f"Error in plotting age distribution by class: {e}")
        return

if __name__ == '__main__':
    main()
