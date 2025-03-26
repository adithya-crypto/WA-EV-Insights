# WA-EV-Insights: Washington State Electric Vehicle Population Analysis

A comprehensive data analysis project examining electric vehicle adoption patterns across Washington State using Python, Pandas, and data visualization techniques.

## Project Overview

This project analyzes the Electric Vehicle Population Data for Washington State to uncover trends, patterns, and insights related to EV adoption. The analysis includes geographic distribution, vehicle characteristics, electric range comparisons, and statistical testing of relationships between vehicle types and clean alternative fuel eligibility.

## Key Features

- **Data Cleaning & Preprocessing**: Handles missing values and prepares data for analysis
- **Exploratory Data Analysis**: Investigates patterns and distributions in the dataset
- **Statistical Analysis**: Includes hypothesis testing using chi-square test
- **Data Visualization**: Creates insightful visualizations to represent findings
- **Comprehensive Reporting**: Summarizes results in a well-structured analysis report

## Key Findings

- Battery Electric Vehicles (BEVs) dominate the market at 77.8% of all EVs in Washington
- BEVs have significantly higher electric range compared to Plug-in Hybrid Electric Vehicles (PHEVs)
- There is a statistically significant relationship between vehicle type and clean alternative fuel eligibility
- Geographic distribution shows concentration in specific counties
- Tesla is the dominant manufacturer in the Washington EV market

## Dataset Information

The analysis is based on the Electric Vehicle Population Data for Washington State, which includes information such as:

- Vehicle identification
- Geographic information (County, City)
- Vehicle specifications (Make, Model, Year)
- Electric vehicle type (BEV, PHEV)
- Electric range
- MSRP information
- Clean alternative fuel eligibility

## Technologies Used

- **Python**: Primary programming language
- **Pandas**: Data manipulation and analysis
- **Matplotlib & Seaborn**: Data visualization
- **SciPy**: Statistical testing
- **Jupyter Notebook**: Development environment

## File Structure

- `project.py`: Main Python script containing the full analysis code
- `Electric_Vehicle_Population_Data.csv`: Dataset (not included in repository due to size)
- `Electric Vehicle Population Data Analysis Report.docx`: Comprehensive analysis report

## How to Run

1. Clone the repository
   ```
   git clone https://github.com/yourusername/WA-EV-Insights.git
   cd WA-EV-Insights
   ```

2. Install required packages
   ```
   pip install pandas matplotlib seaborn scipy
   ```

3. Download the dataset
   - The Electric Vehicle Population Data for Washington State can be obtained from [data.wa.gov](https://data.wa.gov/Transportation/Electric-Vehicle-Population-Data/f6w7-q2d2)
   - Place the CSV file in the project directory

4. Run the analysis script
   ```
   python project.py
   ```

## Visualizations

The project includes several visualizations:

1. **Geographic Distribution**: Shows EV distribution across Washington counties
2. **Make Distribution**: Displays the breakdown of EVs by manufacturer
3. **Electric Range vs. MSRP**: Scatter plot examining relationship between range and price
4. **Vehicle Type Distribution**: Compares proportion of BEVs vs PHEVs
5. **Range Comparison**: Box plot comparing electric range between vehicle types

## Future Work

- Time series analysis of EV adoption rates
- Predictive modeling for future EV growth by county
- Analysis of charging infrastructure in relation to EV population density
- Deeper examination of factors affecting EV price and range

## Acknowledgments

- Washington State Department of Licensing for providing the EV population data
- Contributors to the Python data science ecosystem for their excellent tools
