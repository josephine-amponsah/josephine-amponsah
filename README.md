# Hi, I'm Josephine Amponsah Baah 👋

**📊 Data scientist in risk: credit, fraud and market risk**
🎓 MSc Data Science, UT Austin · 📈 FRM candidate (GARP) · ☁️ Azure Data Scientist Associate · 📍 Accra, Ghana

I build models that decide who gets credit, catch fraud before it costs money, and measure how much a portfolio can lose. I have more than five years of experience in fintech and e-commerce, most recently at a digital lender operating in four countries, where my models ran in production.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/josephine-amponsah-baah-73379a151/)
[![Medium](https://img.shields.io/badge/Medium-000000?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@josephine-amponsah)
[![Email](https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:josephine.amponsah98@gmail.com)

---

## 🔬 Featured projects

### 📈 [Volatility risk premium: forecasting, trading and risk](https://github.com/josephine-amponsah/volatility-risk-premium)
Forecasts next-month SPY volatility with HAR-RV, GARCH and LSTM models in a walk-forward study (2008–2026), then backtests selling one-month variance. A GJR-GARCH filter lifts the Sharpe ratio from **1.13 to 2.62** after costs and cuts the maximum drawdown by **69%**. The project tests the result for luck with a deflated Sharpe ratio and 21 alternative roll dates, backtests one-day VaR with Kupiec and Christoffersen tests, and fits an arbitrage-checked SVI smile to the SPY option chain.

![statsmodels](https://img.shields.io/badge/statsmodels-4051B5?style=flat-square&logo=python&logoColor=white)
![arch](https://img.shields.io/badge/arch-GARCH-6A5ACD?style=flat-square)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?style=flat-square&logo=scipy&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/CI-GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)

### 🏦 [Credit risk lifecycle: from scoring to portfolio monitoring](https://github.com/josephine-amponsah/credit-scoring-nlp-dl)
Two connected projects:
- **Scorecard:** an LSTM credit scorecard served by FastAPI. It returns a calibrated 300–850 score, with SHAP reason codes expressed in score points.
- **Portfolio monitoring:** a dashboard for 2.2 million Lending Club loans. The PD model reaches an out-of-time AUC of **0.74**, with calibration within about 1 percentage point. It computes expected loss as PD × LGD × EAD, credit VaR from a one-factor Vasicek model, survival curves, and a vintage backtest. **[🔗 Live dashboard](https://dashboard-credit-risk.onrender.com)**

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Dash](https://img.shields.io/badge/Dash-3F4F75?style=flat-square&logo=plotly&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)

### 🔎 Search and recommender systems
[Bayesian Personalised Ranking recommender](https://github.com/josephine-amponsah/bpr-recommender) · [Review-aware (ABSA) recommender](https://github.com/josephine-amponsah/absa-based-recommender)
<!-- TODO: description to be added after the recsys / AI search update -->

---

## 💼 Experience in numbers

| Where | What I built | Result |
|---|---|---|
| 🏦 **Fido** · digital lender (Ghana, Uganda, Zambia, South Africa) | First-loan fraud model | **−28%** false positives |
| | Identity-replication classifier | saved nearly **5%** of revenue |
| | A/B-tested KYC cohorts | removed **3.5 pp** of default-risk exposure |
| | Collections prioritisation recommender, ranking delinquent accounts for collectors | **−8%** loan write-offs |
| | Savings retention analysis and experiments | churn down from **56% to 35%** in 6 months |
| | GenAI analytics agent | data requests answered in **≤ 30 minutes**, down from hours or days |
| 🛒 **WeTheBrands** · e-commerce (Germany) | Hierarchical demand forecasting | **−21%** stock write-offs |
| | Marketing mix model | **+7%** conversion |
| 💳 **Broadspectrum** · digital payments | Dispute analysis | disputes down from hundreds a month to **under 50** |
| | Automated financial reporting | **−70%** reporting time |

At Fido I also built the dbt layer that defines risk metrics, reviewed every model release in CI/CD, deployed risk models on AWS with drift monitoring, and automated the central bank audited reports.

---

## 🛠 Toolkit

**🧠 Modelling:** credit scoring · PD/LGD/EAD · fraud detection · survival analysis · causal inference and A/B testing · time-series and volatility models (HAR, GARCH) · recommender systems · deep learning (LSTM, transformers)

**📉 Risk:** expected loss · credit VaR (Vasicek) · market VaR/ES and backtesting · model validation and calibration · option pricing and Greeks

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=postgresql&logoColor=white)
![R](https://img.shields.io/badge/R-276DC3?style=for-the-badge&logo=r&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Statsmodels](https://img.shields.io/badge/Statsmodels-4051B5?style=for-the-badge&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)
![PySpark](https://img.shields.io/badge/PySpark-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white)

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![DBT](https://img.shields.io/badge/DBT-FF694B?style=for-the-badge&logo=dbt&logoColor=white)
![BigQuery](https://img.shields.io/badge/BigQuery-4285F4?style=for-the-badge&logo=googlebigquery&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonwebservices&logoColor=white)
![Azure](https://img.shields.io/badge/Azure-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)

---

## 🎤 Talks and writing

- **DevX 2025:** statistical and ML methods for predicting fraud risk
- **PyCon Ghana 2025:** geospatial segmentation for risk assessment
- ✍️ **[Medium](https://medium.com/@josephine-amponsah):** practical ML, mathematics and finance for data practitioners

## 🎓 Education and certifications

- **MSc Data Science**, University of Texas at Austin (2024–2026): machine learning, deep learning, NLP, advanced predictive modelling, probability and statistics
- **BSc Chemical Engineering**, Kwame Nkrumah University of Science and Technology
- 🏆 **FRM** (GARP), in progress · **Azure Data Scientist Associate** (Microsoft)

---

🤝 *Open to risk, quantitative and data science roles in fintech, banking, trading and energy.*

![Profile Views](https://komarev.com/ghpvc/?username=josephine-amponsah&color=blue&style=flat)
