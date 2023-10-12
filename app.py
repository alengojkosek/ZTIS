import streamlit as st
import requests
import json

# Define the 8 functionalities of the app
functionalities = [
    "Create Portfolio",
    "Add Coin",
    "Remove Coin",
    "Calculate Portfolio Value",
    "View Portfolio History",
    "Set Alerts",
    "Export Portfolio",
    "Import Portfolio",
]

# Create a function to fetch the latest crypto prices from an API
def get_crypto_prices():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100"
    response = requests.get(url)
    data = json.loads(response.content)
    prices = {}
    for coin in data:
        prices[coin["symbol"]] = coin["current_price"]
    return prices

# Create a function to create a new crypto portfolio
def create_crypto_portfolio():
    st.header("Create Portfolio")
    name = st.text_input("Enter Portfolio Name")
    if name:
        portfolio = {}
        portfolio["name"] = name
        portfolio["coins"] = []
        portfolio["history"] = []
        portfolio["alerts"] = []
        st.success(f"Portfolio '{name}' created successfully!")
        return portfolio

# Create a function to add a new coin to a crypto portfolio
def add_coin_to_portfolio(portfolio):
    st.header("Add Coin")
    symbol = st.selectbox("Select Coin Symbol", [
        "btc",
        "eth",
        "usdt",
        "bnb",
        "usdc",
        "xrp",
        "ada",
        "sol",
        "luna",
        "ada",
        "dot"
    ])
    
    quantity = st.number_input("Enter Quantity")
    if symbol and quantity:
        portfolio["coins"].append({"symbol": symbol, "quantity": quantity})
        st.success(f"Added {quantity} {symbol} to the portfolio.")
        update_portfolio_history(portfolio, "add", symbol, quantity, get_crypto_prices()[symbol])

def remove_coin_from_portfolio(portfolio):
    st.header("Remove Coin")
    coins = [coin["symbol"] for coin in portfolio["coins"]]
    coin_to_remove = st.selectbox("Select Coin to Remove", coins)
    
    if st.button("Remove"):
        for i, coin in enumerate(portfolio["coins"]):
            if coin["symbol"] == coin_to_remove:
                update_portfolio_history(portfolio, "remove", coin["symbol"], coin["quantity"], get_crypto_prices()[coin["symbol"]])
                portfolio["coins"].pop(i)
                st.success(f"Removed {coin_to_remove} from the portfolio.")
                break

# Create a function to calculate the total value of a crypto portfolio
def calculate_portfolio_value(portfolio):
    total_value = 0
    for coin in portfolio["coins"]:
        price = get_crypto_prices()[coin["symbol"]]
        total_value += coin["quantity"] * price
    return total_value

def update_portfolio_history(portfolio, action, coin, quantity, price):
    if "history" not in portfolio:
        portfolio["history"] = []

    portfolio["history"].append({
        "action": action,
        "coin": coin,
        "quantity": quantity,
        "price": price
    })


# Create a function to view the portfolio history
def view_portfolio_history(portfolio):
    st.header("View Portfolio History")
    st.table(portfolio["history"])

# Create a function to set alerts
def set_alerts(portfolio):
    st.header("Set Alerts")
    alert_type = st.selectbox("Alert type", ["Price", "Percentage"])
    symbol = st.text_input("Coin symbol")
    value = st.number_input("Value")
    if alert_type and symbol and value:
        portfolio["alerts"].append({"type": alert_type, "symbol": symbol, "value": value})
        st.success(f"Alert set for {symbol} at {value} {alert_type}.")

# Create a function to export the portfolio
def export_portfolio(portfolio):
    st.header("Export Portfolio")
    if st.button("Export"):
        with open("portfolio.json", "w") as f:
            json.dump(portfolio, f)
        st.success("Portfolio exported successfully.")

# Create a function to import the portfolio
def import_portfolio():
    st.header("Import Portfolio")
    uploaded_file = st.file_uploader("Choose a file", type=["json"])
    if uploaded_file is not None:
        try:
            portfolio = json.load(uploaded_file)
            return portfolio
        except json.JSONDecodeError:
            st.error("Invalid JSON file. Please upload a valid portfolio file.")

# Create a Streamlit app to display the crypto portfolio
st.title("Crypto Portfolio")

# Get the current portfolio from the session state
portfolio = st.session_state.get("portfolio", {})

# Display the selected functionality
selected_functionality = st.sidebar.selectbox("Select Functionality", functionalities)

if selected_functionality == "Create Portfolio":
    portfolio = create_crypto_portfolio()
elif selected_functionality == "Add Coin":
    add_coin_to_portfolio(portfolio)
elif selected_functionality == "Remove Coin":
    remove_coin_from_portfolio(portfolio)
elif selected_functionality == "Calculate Portfolio Value":
    st.header("Calculate Portfolio Value")
    st.write("Total portfolio value:", calculate_portfolio_value(portfolio))
elif selected_functionality == "View Portfolio History":
    view_portfolio_history(portfolio)
elif selected_functionality == "Set Alerts":
    set_alerts(portfolio)
elif selected_functionality == "Export Portfolio":
    export_portfolio(portfolio)
elif selected_functionality == "Import Portfolio":
    portfolio = import_portfolio()


# Save the portfolio to the session state
st.session_state["portfolio"] = portfolio