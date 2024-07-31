import streamlit as st
import pandas as pd

st.sidebar.header("ESG Dataset Overview")

# Load the dataset
@st.cache_data
def load_data():
    # Replace 'esg_data.csv' with the path to your CSV file
    data = pd.read_csv('updated_final_with_combined_score.csv')
    
    # Trim any extra whitespace from column headers
    data.columns = data.columns.str.strip()
    
    # Ensure that 'ESG Rating' is numeric
    data['ESG Rating'] = pd.to_numeric(data['ESG Rating'], errors='coerce')
    return data

def calculate_brokerage(esg_rating):
    # Example function: Decrease brokerage with increasing ESG rating
    if pd.isna(esg_rating):
        return 0  # or another default value if ESG Rating is missing
    return max(100 - esg_rating, 0)

def main():
    st.title('ESG Dataset Overview')
    
    # Load the dataset
    data = load_data()
    
    # Display the dataset in a table
    st.write('### ESG Data Table')
    st.dataframe(data)

    # Brokerage Section
    st.header('Brokerage Information')
    st.write('Brokerage fees associated with different companies based on their ESG ratings.')

    # Compute brokerage for each company
    data['Brokerage'] = data['ESG Rating'].apply(calculate_brokerage)
    
    # Sort the data by ESG Rating in decreasing order
    sorted_data = data.sort_values(by='ESG Rating', ascending=False)
    
    # Check if 'High Risk Sectors' column exists and display it
    if 'High Risk Sectors' in sorted_data.columns:
        st.write('### Updated ESG Data with Brokerage (Sorted by ESG Rating)')
        st.dataframe(sorted_data[['Company Name', 'ESG Rating', 'Brokerage', 'Combined ESG-SDG Score']])
    else:
        st.write('### Updated ESG Data with Brokerage (Sorted by ESG Rating)')
        st.dataframe(sorted_data[['Company Name', 'ESG Rating', 'Brokerage']])
    
if __name__ == '__main__':
    main()
