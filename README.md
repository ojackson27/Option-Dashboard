# Black-Scholes Options Risk Dashboard

## Project Overview
This project is an interactive financial dashboard built with **Python** and **Streamlit** to visualize option pricing dynamics and risk metrics.

##  Live Demo
**Try the interactive dashboard instantly in your browser:**
 **[Click Here to Launch App](https://option-dashboard.streamlit.app/)**

---

## Project Overview


Using the **Black-Scholes-Merton model**, the tool functions as a pricing engine that allows users to:
1.  **Calculate Real-Time Greeks:** Visualize how Delta, Gamma, Theta, and Vega evolve across different stock prices.
2.  **Simulate P&L Scenarios:** Generate interactive 3D-style heatmaps to stress-test strategies against changes in **Time Decay (Theta)** and **Volatility (Vega)**.
3.  **Assess Risk/Reward:** Dynamic toggle between **Call** and **Put** options to analyze directional risk.

## Key Features
* **Math Engine:** Custom implementation of the Black-Scholes formula using `scipy.stats` for precise probability density calculations.
* **Interactive Visualization:** Utilizes **Plotly** to create responsive heatmaps that allow for granular data inspection (hover-over financial data).
* **Scenario Analysis:**
    * **Spot vs. Volatility:** Visualizes the impact of IV crush or spikes on option value.
    * **Spot vs. Time:** Visualizes the "Theta decay curve" as expiration approaches.
* **Vectorized Calculations:** Leverages `NumPy` for efficient processing of large pricing grids ($10 \times 10$ matrices) for instant rendering.

## Technology Stack
* **Python 3.9+**
* **Streamlit** (Frontend & Interactivity)
* **NumPy & SciPy** (Financial Mathematics & Vectorization)
* **Plotly** (Data Visualization)

## How to Run Locally
To run this dashboard on your local machine:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/ojackson27/options-risk-dashboard.git](https://github.com/ojackson27/options-risk-dashboard.git)
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Launch the App:**
    ```bash
    streamlit run dash.py
    ```
