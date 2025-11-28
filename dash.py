import streamlit as st
import numpy as np
from scipy.stats import norm
import plotly.graph_objects as go


# 1. THE MATH ENGINE (Black-Scholes Function)

def black_scholes(S, K, T, r, sigma, option_type="Call"):
    d1 = (np.log(S/K) + (r + (sigma**2/2))*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)

    try:
        if option_type == "Call":
            price = S*norm.cdf(d1) - K*np.exp(-r*T)*norm.cdf(d2)
        elif option_type == "Put":
            price = K*np.exp(-r*T)*(1-norm.cdf(d2)) - S*(1-norm.cdf(d1))
        return price
    except:
        return 0.0


# 2. THE DASHBOARD LAYOUT (Sidebar & Title)

st.title("Options Profit & Loss Heatmap")

st.sidebar.header("Market Parameters")
asset_price = st.sidebar.number_input("Current Asset Price", value=100.0)
strike_price = st.sidebar.number_input("Strike Price", value=100.0)
time_to_expiry = st.sidebar.number_input("Time to Expiry (Years)", value=1.0)
volatility = st.sidebar.number_input("Volatility (σ)", value=0.2)
risk_free_rate = st.sidebar.number_input("Risk-Free Rate", value=0.05)


# The choice for Call/Put
option_choice = st.sidebar.radio("Option Type",["Call", "Put"])


# 3. THE CALCULATION LOGIC

# A. Create the Heatmap Input Ranges
# "Spot Price" range: +/- 20% from current price
spot_range = np.linspace(asset_price * 0.8, asset_price * 1.2, 10)
# "Time" range: From now down to 0
vol_range = np.linspace(volatility * 0.5, volatility * 1.5, 10)

# B. Calculate the "Purchase Price" (Cost Basis)
purchase_price = black_scholes(asset_price, strike_price, time_to_expiry, risk_free_rate, volatility, option_choice)



# C. Calculate the P&L Grid
pnl_grid = np.zeros((10, 10))
                    
# Heatmap type
heatmap_type = st.selectbox("Select Heatmap Option", ["Spot Price vs Volatility", "Spot Price vs Time"])

if heatmap_type == "Spot Price vs Volatility": 
    y_range = np.linspace((volatility*0.5),(volatility*1.5),10)
    y_label = "Volatility"
    for i in range(10): 
        for j in range(10):
            sim_spot = spot_range[j]
            sim_vol = y_range[i]
            sim_price = black_scholes(sim_spot, strike_price, time_to_expiry, risk_free_rate, sim_vol, option_choice)
            pnl_grid[i, j] = sim_price - purchase_price
            
elif heatmap_type == "Spot Price vs Time":
    y_range = np.linspace(0.1,time_to_expiry,10)
    y_label = "Time to Expiry"
    for i in range(10): 
        for j in range(10):
            sim_spot = spot_range[j]
            sim_time = y_range[i]
            sim_price = black_scholes(sim_spot, strike_price, sim_time, risk_free_rate, volatility, option_choice)
            pnl_grid[i, j] = sim_price - purchase_price
            
    
    



# 4. THE VISUALIZATION (Plotly)

fig = go.Figure(data=go.Heatmap(
    z=pnl_grid,
    x=spot_range,
    y=y_range,
    colorscale='RdYlGn', # Red (Loss) to Green (Profit)
    colorbar=dict(title="Profit/Loss")
))

fig.update_layout(title=f"P&L Heatmap: {y_label} vs Spot Price",
                  xaxis_title="Spot Price",
                  yaxis_title=y_label)

st.plotly_chart(fig)

st.write(f"**Current Option Price:** ${purchase_price:.2f}")


# SIDEBAR - ABOUT ME

st.sidebar.markdown("---") # Adds a visual separator line
st.sidebar.title("About")
st.sidebar.info(
    """
    This dashboard was built by **[Oliver Jackson]**.
    
    Interested in my work?
    - [Connect on LinkedIn](www.linkedin.com/in/oliver-jackson-7a856629b)
    - [View Source Code](https://github.com/ojackson27)
    """
)
