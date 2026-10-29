# E-Commerce Sales & Customer Analytics

A reproducible portfolio case study covering data quality, SQL, Python EDA, KPI definitions, customer RFM segmentation, retention cohorts, dashboards and business recommendations.

[Setup](#local-installation--setup-guide) · [Architecture](#architecture--system-design-diagram) · [Detailed guide](PROJECT_GUIDE.md) · [Repository standard](docs/REPOSITORY_STANDARD.md)

## Visuals

A captured application screenshot or demo recording is not included yet. See the architecture section and checked-in documentation below.

## Live Link / Demo

Download and open [dashboard_summary.html](outputs/dashboard_summary.html) for the supplied summary artifact. Run the Python entry point below for calculations; no Streamlit application is present in this checkout.

## Key Features

- Pandas joins over customers, products, orders and line items.
- Completed-order revenue, profit, margin and average-order-value calculations.
- Quantile-based RFM customer segmentation and CSV export.
- SQL schema and analytics queries, DAX measures and a summary HTML artifact.

## Tech Stack

![Python](https://img.shields.io/badge/Python-334155?style=flat-square) ![Pandas](https://img.shields.io/badge/Pandas-334155?style=flat-square) ![NumPy](https://img.shields.io/badge/NumPy-334155?style=flat-square) ![SQL](https://img.shields.io/badge/SQL-334155?style=flat-square)

Dependency versions and optional packages are defined in the repository manifests.

## Architecture / System Design Diagram

Source layout and component inventory (asset not present in this checkout). A runtime architecture diagram remains a follow-up task.

## Local Installation & Setup Guide

```bash
git clone https://github.com/harshakavali81-collab/E-Commerse-Sales-and-Customers-Analytics.git
cd E-Commerse-Sales-and-Customers-Analytics
```

Requires Python with venv support. Run from the repository root:

```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python run_project.py
python -m pytest -q
```

The runner reads the checked-in CSVs and overwrites `outputs/rfm_customer_segments.csv`. The current test checks a row-count invariant; broader financial reconciliation tests remain future work. Older guide commands referring to `src/pipeline.py`, `app.py`, or `src/build_deliverables.py` do not match this checkout.

## Challenges & Solutions

Raw lines: 72,388; duplicate line IDs removed: 100; quarantined invalid lines: 60; retained lines: 72,228. One missing category becomes Unknown. Price/discount/quantity are captured at transaction time, not read from the current product price.

Net line value = quantity × transaction unit price − discount amount. Only Completed lines recognize revenue and product cost. Returned/cancelled lines recognize zero. Gross profit = recognized revenue − recognized product cost. Returned products are assumed recoverable with full refunds; handling fees and damaged stock are unavailable.

Revenue is not operating profit. Distinct monthly customers and orders cannot generally be summed across categories or periods to obtain a global distinct total. AOV uses the same completed-order population as its revenue. Return rate uses all shipped orders, including returns, from original order headers.

RFM segments are fixed full-history business rules as of 1 Jan 2026. The dashboard's repeat rate is recomputed within its filters. Cohort charts in Streamlit are explicitly full-history references. High discounts correlate with lower margin in the simulated data; they do not prove causation.

## Future Improvements

- Capture a reproducible end-to-end demo with runtime versions and sample inputs.
- Expand regression checks for invalid inputs and documented edge cases.
- Record measured results, data provenance and deployment limitations alongside each release.

## Scope and supporting evidence

A reproducible portfolio case study covering data quality, SQL, Python EDA, KPI definitions, customer RFM segmentation, retention cohorts, dashboards and business recommendations.

**Synthetic data.** Generated with seed `20260930` for Jan 2024-Dec 2025. Currency: INR. This is not an analysis of a real company.

Monthly revenue (asset not present in this checkout)

## Repository Structure

| Location | Purpose |
| --- | --- |
| `src/` | Source modules |
| `tests/` | Tests |
| `docs/` | Documentation |
| `data/` | Data and samples |
| `sql/` | SQL schema and analysis |
| `powerbi/` | Power BI build assets |
| `.github/` | Issue forms, PR template and automated checks |

[Complete file inventory and workflow](docs/REPOSITORY_STANDARD.md). Runtime entry points retain their existing paths.

## Workflow & Tracking

Use the [bug and feature forms](https://github.com/harshakavali81-collab/E-Commerse-Sales-and-Customers-Analytics/issues/new/choose) to define work with acceptance criteria. Keep tasks in Todo → In progress → Review → Done, and link a pull request with `Closes #<number>`. See [the maintenance workflow](docs/REPOSITORY_STANDARD.md#workflow).

## License

Original project software is available under the [MIT License](LICENSE). See [licensing scope](docs/LICENSING.md) for third-party and data exclusions.

