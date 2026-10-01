# E-Commerce Sales & Customer Analytics

A reproducible portfolio case study covering data quality, SQL, Python EDA, KPI definitions, customer RFM segmentation, retention cohorts, dashboards and business recommendations.

**Synthetic data.** Generated with seed `20260930` for Jan 2024-Dec 2025. Currency: INR. This is not an analysis of a real company.

![Monthly revenue](outputs/charts/monthly_trend.png)

## Results

| KPI | Result |
|---|---:|
| Net revenue | INR 211,448,183.45 |
| Gross profit | INR 63,272,309.05 |
| Gross margin | 29.92% |
| Completed orders with a valid line | 31,581 |
| Purchasing customers | 5,376 |
| Average order value | INR 6,695.42 |
| Repeat customer rate | 80.04% |
| Returned / shipped orders | 7.41% |

## Start immediately

1. Extract the ZIP completely. Open this folder in VS Code.
2. Open `outputs/Ecommerce_Dashboard.html` in Chrome or Edge. It works offline, includes four views and supports year, region and category filters. No Python is needed for this view.
3. Read `outputs/Ecommerce_Final_Report.pdf` and open `outputs/Ecommerce_Analytics.xlsx`.
4. For Power BI, follow `powerbi/README.md`. The project source is supplied; a native Desktop refresh and visual check remain required.

## Reproduce in Python

```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python src/pipeline.py
python src/build_deliverables.py
python -m unittest discover -s tests
streamlit run app.py
```

The supplied outputs already exist. Pipeline execution regenerates the same raw data with the fixed seed and overwrites its analytics outputs. `build_deliverables.py` rebuilds HTML/PDF/docs/notebook. Excel is a supplied snapshot with linked ratio formulas; refresh Excel by replacing its input tables from the new CSV outputs. The workbook builder used for the supplied snapshot is not a public Python dependency.

## Project contents

| Location | Contents |
|---|---|
| `data/raw/` | Original customers, products, orders and dirty order lines |
| `data/processed/` | Clean tables, flattened fact sales, RFM and date dimension |
| `src/pipeline.py` | Synthetic generator, cleaning, EDA, segmentation, SQL execution and checks |
| `sql/` | SQLite views plus 14 analytical queries |
| `notebooks/analysis.ipynb` | Runnable SQL and Python analysis notebook |
| `app.py` | Interactive Streamlit dashboard with four tabs |
| `powerbi/` | Editable native project source, semantic model, DAX and setup guide |
| `outputs/` | Offline dashboard, Excel, PDF, SQLite database, query results and seven charts |
| `docs/` | Definitions, data dictionary, findings, interview notes and GitHub guide |
| `tests/` | Four tests checking accounting semantics, cohorts, rates and recency |
| `.github/workflows/` | Automated pipeline and validation on push/PR |

## Data quality and accounting

Raw lines: 72,388; duplicate line IDs removed: 100; quarantined invalid lines: 60; retained lines: 72,228. One missing category becomes Unknown. Price/discount/quantity are captured at transaction time, not read from the current product price.

Net line value = quantity × transaction unit price − discount amount. Only Completed lines recognize revenue and product cost. Returned/cancelled lines recognize zero. Gross profit = recognized revenue − recognized product cost. Returned products are assumed recoverable with full refunds; handling fees and damaged stock are unavailable.

Revenue is not operating profit. Distinct monthly customers and orders cannot generally be summed across categories or periods to obtain a global distinct total. AOV uses the same completed-order population as its revenue. Return rate uses all shipped orders, including returns, from original order headers.

RFM segments are fixed full-history business rules as of 1 Jan 2026. The dashboard's repeat rate is recomputed within its filters. Cohort charts in Streamlit are explicitly full-history references. High discounts correlate with lower margin in the simulated data; they do not prove causation.

## Validation

SQL/Python revenue and gross profit reconcile within INR 0.01; completed order counts, monthly totals and segment revenue reconcile. Four business tests pass. GitHub CI reproduces the pipeline. Power BI Desktop and Excel's native desktop engine have not been exercised in this environment.

## GitHub

Repository: https://github.com/harshakavali81-collab/E-Commerse-Sales-and-Customers-Analytics

All source, synthetic datasets, report outputs and a CI workflow are included. See `docs/GITHUB_SETUP.md` for local Git commands.

## License

MIT for code and generated synthetic data. See LICENSE. Microsoft documentation and JSON schema references retain their original terms.
