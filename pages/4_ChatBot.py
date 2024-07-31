import streamlit as st
import warnings

warnings.filterwarnings('ignore')


# Sample questions and answers
questions_answers = {
    "General Investment Questions": {
        "What is an investment?": "An investment is an asset or item acquired with the goal of generating income or appreciation over time. Common forms of investment include stocks, bonds, mutual funds, real estate, and commodities.",
        "How do I start investing?": "To start investing, you need to define your financial goals, determine your risk tolerance, research investment options, open a brokerage account, and start purchasing investments that align with your strategy.",
        "What are the different types of investments?": "The main types of investments include stocks, bonds, mutual funds, ETFs (Exchange-Traded Funds), real estate, and commodities. Each type has different risk and return characteristics."
    },
    "Specific Investment Products": {
        "What is a mutual fund?": "A mutual fund is a type of investment vehicle that pools money from many investors to purchase a diversified portfolio of stocks, bonds, or other securities. It is managed by a professional fund manager.",
        "What is an ETF (Exchange-Traded Fund)?": "An ETF is similar to a mutual fund but trades like a stock on an exchange. It holds a diversified portfolio of assets and offers the flexibility of buying and selling shares throughout the trading day.",
        "What are bonds?": "Bonds are debt securities issued by governments or corporations to raise capital. When you buy a bond, you are essentially lending money to the issuer in exchange for periodic interest payments and the return of the principal at maturity."
    },
    "Risk and Strategy": {
        "What is investment risk?": "Investment risk refers to the possibility of losing some or all of the invested capital. It can arise from market fluctuations, economic downturns, or other factors affecting the value of investments.",
        "How can I assess my risk tolerance?": "To assess your risk tolerance, consider your financial goals, investment timeline, comfort with market fluctuations, and overall financial situation. Many financial advisors and online tools offer risk assessment questionnaires."
    },
    "Retirement and Long-Term Planning": {
        "How can I save for retirement?": "To save for retirement, contribute to retirement accounts like a 401(k) or IRA, take advantage of employer matching contributions, diversify your investments, and regularly review and adjust your retirement plan.",
        "What is a 401(k) plan?": "A 401(k) plan is a retirement savings plan sponsored by an employer. It allows employees to save and invest a portion of their paycheck before taxes are taken out. Employers often match a portion of the contributions."
    },
    "Tools and Resources": {
        "What are some good investment apps?": "Some popular investment apps include Robinhood, E*TRADE, TD Ameritrade, Fidelity, and Acorns. These apps offer various features like commission-free trading, investment education, and automated investing.",
        "How can I track my investments?": "You can track your investments using online brokerage accounts, investment apps, or financial software like Mint, Personal Capital, or Quicken. These tools help monitor performance, asset allocation, and financial goals."
    },
    "Market Analysis and News": {
        "What are the current market trends?": "Current market trends vary based on economic conditions, political events, and investor sentiment. It's important to stay informed through financial news sources, market reports, and analysis from reputable institutions.",
        "What economic indicators should I watch?": "Key economic indicators to watch include GDP growth, unemployment rates, inflation rates, interest rates, and consumer confidence. These indicators provide insights into the overall health of the economy."
    },
    "Personal Finance and Budgeting": {
        "How do I create a budget?": "To create a budget, list your income sources, track your expenses, categorize spending, set savings and investment goals, and adjust as needed. Budgeting apps like YNAB or spreadsheets can help manage this process.",
        "How much should I save each month?": "The amount you should save each month depends on your financial goals and income. A common recommendation is to save at least 20% of your monthly income, but your individual situation may require more or less."
    },
    "Technical Questions (for advanced users)": {
        "What is technical analysis?": "Technical analysis is a method of evaluating securities by analyzing statistical trends from trading activity, such as price movements and volume. It uses charts and other tools to identify patterns and make investment decisions.",
        "What are moving averages, and how are they used in investing?": "Moving averages smooth out price data to identify trends over time. Common types include the simple moving average (SMA) and the exponential moving average (EMA). They help investors determine support and resistance levels."
    },
    "Miscellaneous": {
        "How do I set up an investment account?": "To set up an investment account, choose a brokerage firm, complete the account application, verify your identity, fund your account, and start selecting investments. Online brokers often offer easy-to-follow setup processes.",
        "What fees should I be aware of when investing?": "Be aware of brokerage fees, mutual fund expense ratios, management fees for financial advisors, trading commissions, and account maintenance fees. These can impact your investment returns over time."
    }
}

# Streamlit app
st.set_page_config(page_title="Chatbot Home Page", page_icon="🤖", layout="wide", initial_sidebar_state="auto")


st.sidebar.header("Help Center")

st.title("Welcome to the Chatbot Page")
st.write("Ask me anything about investments!")

# Initialize session state to keep track of the conversation
if 'history' not in st.session_state:
    st.session_state.history = []
if 'current_category' not in st.session_state:
    st.session_state.current_category = None
if 'current_question' not in st.session_state:
    st.session_state.current_question = None

# Custom CSS for alignment
st.markdown("""
    <style>
    .user-input {text-align: right; color: white;}
    .robo-response {text-align: left; color: white;}
    </style>
    """, unsafe_allow_html=True)

# Display chat history
for chat in st.session_state.history:
    if chat.startswith("You:"):
        st.markdown(f"<div class='user-input'>{chat}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='robo-response'>{chat}</div>", unsafe_allow_html=True)

# Display initial categories as buttons
if st.session_state.current_category is None:
    st.write("Please select a category:")
    for category in questions_answers.keys():
        if st.button(category):
            st.session_state.current_category = category
            st.session_state.history.append(f"You: {category}")
            st.session_state.history.append(f"ROBO: Here are the questions for {category}:")
elif st.session_state.current_question is None:
    # Display questions from the selected category as buttons
    st.write(f"Category: {st.session_state.current_category}")
    for question in questions_answers[st.session_state.current_category].keys():
        if st.button(question):
            user_input = question
            st.session_state.current_question = question
            st.session_state.history.append(f"You: {user_input}")
            st.session_state.history.append(f"ROBO: {questions_answers[st.session_state.current_category][question]}")

    # Option to go back to the main category selection
    if st.button("Go back to categories"):
        st.session_state.current_category = None
else:
    # Show the selected question and its answer
    st.write(f"Question: {st.session_state.current_question}")
    st.write(f"Answer: {questions_answers[st.session_state.current_category][st.session_state.current_question]}")

    # Option to go back to the question list
    if st.button("Go back to questions"):
        st.session_state.current_question = None

    # Option to go back to the main category selection
    if st.button("Go back to categories"):
        st.session_state.current_category = None
        st.session_state.current_question = None