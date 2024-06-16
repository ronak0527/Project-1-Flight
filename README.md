# Flight Management System

This project is a Python program to manage and analyze passenger data. It covers data loading, cleaning, analysis, and visualization using various libraries.

## Getting Started

### Prerequisites
- Python 3.x
- pandas
- matplotlib
- seaborn
- plotly

### Installing
1. Clone the repository:
    ```
    git clone https://github.com/yourusername/flight-management-system.git
    cd flight-management-system
    ```

2. Install the required libraries:
    ```
    pip install pandas matplotlib seaborn plotly
    ```

### Running the Program
1. Place your `passengers.csv` file in the project directory.
2. Run the main script:
    ```
    python main.py
    ```

### Files
- `passenger_analysis.py`: Contains all the functions for data loading, cleaning, analysis, and visualization.
- `main.py`: The main script to run the program.
- `README.md`: This file.

### Functions
- `load_data(file_path)`: Loads the CSV file into a pandas DataFrame.
- `clean_data(df)`: Cleans the data by handling missing values and ensuring appropriate data types.
- `calculate_average_age(df, travel_class)`: Calculates the average age for a specified travel class.
- `find_loyalty_members(df)`: Finds loyalty members.
- `get_class_statistics(df)`: Returns class statistics.
- `plot_age_distribution(df)`: Plots the age distribution.
- `plot_average_age_by_class(df)`: Plots the average age by travel class.
- `plot_age_vs_loyalty(df)`: Plots age vs loyalty membership using Seaborn.
- `plot_age_distribution_by_class(df)`: Plots age distribution by travel class using Plotly.

### Bonus
- Implement unit tests for your functions using `unittest` or `pytest`.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
