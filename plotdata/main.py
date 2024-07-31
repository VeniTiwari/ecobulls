import numpy as np
import pandas as pd
import streamlit as st

# Load Data
@st.cache_data
def load_data():
    # Load the dataset from the CSV file
    return pd.read_csv('esg_data.csv')

data = load_data()

# ESG Scoring System
def esg_score(company):
    # Simple scoring logic
    return data.loc[data['Company Name'] == company, 'ESG Rating'].values[0]

# Portfolio Builder
def build_portfolio(companies):
    portfolio = data[data['Company Name'].isin(companies)]
    return portfolio

# Risk Assessment
def assess_risk(portfolio):
    # Mock risk assessment
    return np.random.random()

# Streamlit App
st.title('Sustainable Finance Platform')

# Display the dataset
st.header('ESG Data')
st.write('The dataset containing ESG scores and other information:')
st.dataframe(data)

# ESG Scoring
st.header('ESG Scoring')
company = st.selectbox('Select a company', data['Company Name'].unique())
score = esg_score(company)
st.write(f'ESG Score for {company}: {score}')

# Portfolio Builder
st.header('Portfolio Builder')
selected_companies = st.multiselect('Select companies for your portfolio', data['Company Name'].unique())
if selected_companies:
    portfolio = build_portfolio(selected_companies)
    st.write('Your Portfolio:', portfolio)
    risk = assess_risk(portfolio)
    st.write(f'Portfolio Risk: {risk}')

# Sorting functionality
st.header('Sort Companies by ESG Score')
sort_order = st.radio('Select sorting order:', ('Ascending', 'Descending'))

if sort_order == 'Ascending':
    sorted_data = data.sort_values(by='ESG Rating', ascending=True)
else:
    sorted_data = data.sort_values(by='ESG Rating', ascending=False)

st.dataframe(sorted_data)

# Risk Dashboard
st.header('Risk Dashboard')
# Visualize risks (placeholder)
st.line_chart(np.random.randn(100, 3))

# Financial Inclusion Portal
st.header('Financial Inclusion Portal')
st.write('Educational content and investment simulation tools will be here.')

if st.button('Deploy'):
    st.write('App deployed successfully!')
