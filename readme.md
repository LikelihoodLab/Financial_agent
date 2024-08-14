# Financial Analysis Crew
## Overview
The Financial Analysis Crew is an intelligent and automated tool designed to fetch, analyze, and report on financial market data with a focus on gold. It utilizes advanced AI agents to gather data from various sources and generate detailed reports.
### Features
- **Data Collection and Summarization**: Utilizes tools to scrape websites and search news articles.
- **Financial Analysis**: Analyzes collected data to generate meaningful insights and recommendations.
- **Gold Market Focus**: Specifically tailored to analyze and report on the gold market.
## Setup Instructions
### Prerequisites
- **Python**: Ensure Python version 3.10 or higher is installed.
- **Poetry**: Dependency management tool for Python.
### Step-by-Step Setup
1. **Clone the repository**:
    ```bash
    git clone <https://github.com/kevin-00115/Financial_agent.git>
    cd <repo-directory>
    ```
2. **Install dependencies**:
    Using Poetry:
    ```bash
    poetry install
    ```
3. **Environment Variables**:
    Create a `.env` file in the root directory with the following variables. These are necessary for API access and tool functionality.
    ```
    GOOGLE_SERPER_API_KEY=<your_google_serper_api_key>
    OPENAI_API_KEY=<your_openai_api_key>
    ```
4. **Run the application**:
    ```bash
    python main.py
    ```
## Project Structure
- **`agents.py`**: Defines the different AI agents used for performing specialized tasks such as researching, financial analysis, and investment advising.
- **`tasks.py`**: Contains tasks for the agents, focused on researching financial data, performing financial analysis, and generating investment recommendations.
- **`tools/`**:
  - **`browser_tool.py`**: Tool for scraping and summarizing website content.
  - **`search_tool.py`**: Tool for searching the internet and fetching news articles.
- **`main.py`**: The main entry point of the application which initializes and executes the `FinancialCrew`.
- **`pyproject.toml`**: Project configuration file for Poetry.
## Usage
1. **Start the Financial Analysis Crew**:
    ```bash
    python main.py
    ```
   This will run the crew, utilizing various agents and tasks to generate a comprehensive report on the gold market.
2. **Output**:
    After execution, the result of the analysis will be printed in the terminal.
### Example Output
```plaintext
########################
## Here is the Report
########################

**Gold Market Report - August 14, 2024**

---

**Introduction**

As of August 14, 2024, the gold market is navigating a complex landscape shaped by inflationary pressures, geopolitical tensions, and evolving central bank policies. This report synthesizes recent market data, forecasts, and expert analyses to provide a comprehensive investment recommendation concerning gold.

---

**Current Market Overview**

- **Current Gold Price**: $2,468.73 per ounce, reflecting a slight decrease amid market volatility.
- **Price Trends**: Gold prices have been fluctuating in response to U.S. inflation data, with recent predictions suggesting a rise to $2,500 per ounce by the end of 2024.

---

**Recent Events Summary**

1. **U.S. Inflation Data**: The recent Consumer Price Index (CPI) data indicated a rise in consumer prices, which has dimmed expectations for immediate rate cuts from the Federal Reserve. This resulted in a cautious sentiment among traders, contributing to a temporary dip in gold prices.
   
2. **Central Bank Policies**: Analysts from J.P. Morgan predict that gold prices will benefit from ongoing inflationary pressures and potential easing of monetary policy, which historically leads to increased demand for safe-haven assets.

3. **Geopolitical Tensions**: Heightened geopolitical uncertainties are reinforcing gold's appeal as a safe-haven investment. Central banks worldwide are increasing their gold reserves, further supporting prices.

---

**Geopolitical Impact**

Geopolitical tensions are a significant factor influencing gold prices. Ongoing global conflicts and economic instability have led to increased demand for gold as a hedge against uncertainty. Surveys indicate that geopolitical risks are now perceived as a greater threat than inflation, shifting investor focus towards gold.

---

**Central Banks' Policies**

The Federal Reserve's monetary policy is crucial for gold prices. Currently, there's an expectation of a cautious approach to rate changes. Analysts suggest that a hawkish stance may continue to induce volatility in gold markets, but any signs of easing could bolster prices significantly.

---

**Potential Risks**

1. **Market Volatility**: The immediate reaction to inflation data can lead to unpredictable price movements, presenting risks to gold investments.
2. **Rate Hikes**: If the Federal Reserve pursues aggressive rate hikes to combat inflation, this may negatively impact gold prices.
3. **Global Economic Conditions**: A strong recovery in the global economy could shift investor interest away from precious metals.

---

**Demand Trends**

Gold demand has remained robust, driven by both retail and institutional investors seeking to secure their portfolios against inflation and market volatility. The ongoing purchases by central banks highlight the sustained interest in gold as a pivotal asset.

---

**Price Forecast**

Analysts forecast that gold prices could rise to approximately $2,500 per ounce by the end of 2024, supported by persistent inflation and geopolitical uncertainty. The technical analysis suggests that reclaiming levels above $2,460 could trigger further upward momentum.

---

**Gold Index Calculation**

To provide a numerical assessment of gold's current performance, we have developed a Gold Index based on the following parameters:

1. **Current Gold Price**: $2,468.73 (Weight: 30%)
2. **Central Bank Policy Impact**: Current Fed stance and expectations (Weight: 25%)
3. **Geopolitical Influence**: Assessment of current tensions (Weight: 20%)
4. **Demand Trends**: Retail and institutional interest (Weight: 15%)
5. **Price Forecast**: Expected future price trajectory (Weight: 10%)

**Calculation Steps**:

- **Current Gold Price Impact**: 100 * (Current Price / $2,500) = 100 * (2468.73 / 2500) = 98.74
- **Central Bank Policy Impact**: Given current expectations, we rate this as 80/100 = 80
- **Geopolitical Influence**: Given the current landscape, we rate this as 85/100 = 85
- **Demand Trends**: Assessing strong demand, we rate this as 90/100 = 90
- **Price Forecast**: With a positive outlook, we rate this as 75/100 = 75

**Weighted Index Calculation**:
- Gold Index = (98.74 * 0.30) + (80 * 0.25) + (85 * 0.20) + (90 * 0.15) + (75 * 0.10) 
- Gold Index = 29.62 + 20 + 17 + 13.5 + 7.5 = **87.62**

---

**Conclusion and Recommendation**

The gold market on August 14, 2024, demonstrates a nuanced interplay of inflation, central bank policies, and geopolitical tensions. The calculated Gold Index of **87.62** indicates that gold is currently performing well, reflecting strong demand and economic uncertainty.

**Investment Strategy**: 

- **Short-term**: Consider accumulating positions in gold, particularly if prices dip below $2,450, as this may provide an attractive entry point.
- **Long-term**: Maintain a core allocation to gold in portfolios, anticipating a rise to $2,500 per ounce by year-end, driven by ongoing inflation concerns and geopolitical risks.

Investors should remain vigilant regarding economic indicators and central bank communications as these will significantly influence gold’s trajectory in the coming months. 

---

This comprehensive analysis provides a strong foundation for informed investment decisions in the gold market amidst evolving economic conditions.
