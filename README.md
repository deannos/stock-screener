# 📈 Indian Stock Screener – Macro + Fundamental Analysis

An institutional-grade **fundamental stock screener** for Indian equities that combines real-time financial data with macroeconomic insights and investor profiling. Built using **Python + Streamlit**, this tool filters high-quality companies aligned with the current economic stage and investor preferences.

---

## 🧭 Table of Contentš

- [Project Overview](#-project-overview)
- [Core Logic](#-core-logic)
- [Financial Metrics Used](#-financial-metrics-used)
- [Project Structure](#-project-structure)
- [Setup Instructions](#-setup-instructions)
- [Deployment Options](#-deployment-options)
- [ Use Cases](#-use-cases)
- [ Future Enhancements](#-future-enhancements)
- [ Contact](#-contact)

---

## 🔍 Project Overview

This project aims to provide a **personalized and data-driven stock screening experience** by combining:

- **Investor Profile**: Risk appetite + investment horizon
- **Macroeconomic Phases**: Sector rotation based on Recession, Recovery, or Expansion
- **Fundamentals**: Capital efficiency and cash generation filters using real-time data

✅ **Goal**: Identify fundamentally strong Indian stocks aligned with market trends and investor strategy.

---

## 📐 Core Logic

### 1. 🧑‍💼 Investor Customization

- **Inputs**: Investment Horizon (`Short / Mid / Long`) + Risk Profile (`Low / Moderate / High`)
- Determines tolerance and sector bias.

### 2. 📉 Macroeconomic Phase

- Options: `Recession`, `Recovery`, `Expansion`
- Each phase maps to historically out/under-performing sectors.

### 3. 🏢 Sector Mapping

Example:
| Macro Stage | Selected Sectors |
|-------------|------------------|
| Expansion | Financials, IT, Consumer Goods |
| Recession | Pharma, FMCG, Utilities |
| Recovery | Industrials, Auto, Infra |

### 4. 🏦 Stock Pooling

- Pulls Indian stock symbols (e.g., `INFY.NS`, `HDFCBANK.NS`) from selected sectors.

### 5. 📊 Real-Time Data Collection

Via `yfinance`:

    - Return on Equity (ROE, proxy for ROIC)
    - Free Cash Flow (FCF)
    - Market Capitalization

### 6. ✅ Screening Conditions

- **ROIC > CoE** → Value creation
- **FCF Yield > 3%** → Strong cash generation

## 📊 Financial Metrics Used

| Metric                   | Explanation                                               |
| ------------------------ | --------------------------------------------------------- |
| **ROIC (via ROE)**       | Return on Invested Capital. Proxy using ROE from yfinance |
| **Cost of Equity (CoE)** | `Risk-Free Rate + Beta × Market Risk Premium`             |
| **Free Cash Flow Yield** | FCF / Market Cap. Shows profitability vs valuation        |
| **Beta**                 | Risk compared to the overall market                       |

---

## 🗂️ Project Structure

```
stock-screener-algo/
│
├── app/                            # Frontend & UI logic
│   └── app.py                      # Streamlit app entry point
│
├── core/                           # Core screening engine
│   ├── screener.py                 # Main screening logic (ROIC, FCF Yield, CAPM)
│   ├── utils.py                    # Financial formulas: CoE, FCF Yield, ROIC proxy
│   └── config.py                   # Constants, sector mappings, macro-stage definitions
│
├── data/                           # Data access layer
│   └── data.py                     # Real-time financial data using yfinance
│
├── assets/                         # Static assets
│   └── screenshots/                # (Optional) UI snapshots
│
├── requirements.txt                # Python dependencies
├── README.md                       # Project overview and instructions
└── .gitignore                      # Files to ignore in version control
```

---

## ⚙️ Setup Instructions

### ✅ Prerequisites

- Python 3.8+
- Internet connection (for yfinance API)

### 🔧 Installation

```bash
git  clone  https://github.com/yourusername/stock-screener-algo.git
cd  stock-screener-algo
pip  install  -r  requirements.txt
```

▶️ Run the App

```bash
streamlit run app.py
```

- Then open your browser to http://localhost:8501.

## Deployment Options

**1. Deploy via Docker**

Run your app in an isolated container using Docker

- Clone the repository

```bash
git clone https://github.com/yourusername/stock-screener-algo.git
cd stock-screener-algo
```

- Build the Docker image

```bash
docker build -t stock-screener .
```

- Run the Docker container

```bash
docker run -p 8501:8501 stock-screener
```

- Visit your app Open your browser and go to: http://localhost:8501

**2. Deploy on Streamlit Cloud**

- Push this project to your GitHub repo
- Go to streamlit.io/cloud
- Click “New App”
- Connect your GitHub repo
- Set app.py as the entry point
- Click “Deploy”

✅ Done! Your app will be live and publicly accessible with a shareable URL.

## Use Cases

- Individual Investors screening Indian stocks based on macro + fundamentals
- Portfolio Managers creating watchlists based on risk-adjusted metrics
- Education tool to learn macro-to-micro investing
- Base for backtesting or quant models

## Future Enhancements

- Add earnings/momentum filters
- Historical ROIC trends (3–5 yr avg for long-term investing)
- NLP for earnings sentiment analysis
- Alert system (Telegram, Email)
- Deploy on Streamlit Cloud or Docker
