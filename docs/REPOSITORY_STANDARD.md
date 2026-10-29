# Repository standard

## Layout

This repository keeps its working source paths. A shared portfolio structure does not require moving a React application, Python package, BI workbook or Verilog project into identical runtime directories.

| Area | Convention |
| --- | --- |
| Landing page | `README.md`: purpose, visuals, demo, features, stack, architecture, setup, tradeoffs and roadmap |
| Detailed reference | `PROJECT_GUIDE.md`: retained project-specific explanation and historical release notes |
| Documentation | `docs/`: design, inventory, reproduction and evidence |
| Work intake | `.github/ISSUE_TEMPLATE/`: bug and feature forms |
| Review | `.github/PULL_REQUEST_TEMPLATE.md`: linked issue, behavior and validation |
| Automation | `.github/workflows/portfolio-docs.yml`: README section and local-link checks |
| Source and tests | Existing project-specific paths listed below; no empty source/test placeholders |

## Workflow

1. Open an issue describing the user problem and measurable acceptance criteria.
2. Add it to a GitHub Project with Todo, In progress, Review and Done states when a board is configured.
3. Use a focused branch and meaningful commits, such as `docs: correct local setup paths` or `fix(api): reject malformed input`.
4. Run the project's documented checks and `python scripts/check_portfolio_docs.py`.
5. Open a pull request with actual validation results and `Closes #<issue-number>`.
6. Merge after review; record release evidence and update the issue/board.

Board creation, profile pins, repository social previews and milestone settings require account-level configuration. This file does not claim those settings have been applied.

## Validation scope

The documentation check validates the landing-page headings and local link targets only. It does not execute models, certify test coverage, inspect Git history for secrets, verify external websites, or prove production readiness. Existing application workflows remain the source of runtime CI evidence.

Keep credentials in local environment variables. A gitignore rule does not remove secrets already tracked or committed. Use only permitted sample data in public demos.

## Inventory at standardization

The following are the pre-existing public project files. New standardization files are described above. Historical guides may mention external bundles that are not part of this list.

- [`README.md`](<../README.md>)
- [`build.py`](<../build.py>)
- [`data`](<../data>)
- [`data/customers.csv`](<../data/customers.csv>)
- [`data/order_details.csv`](<../data/order_details.csv>)
- [`data/orders.csv`](<../data/orders.csv>)
- [`data/products.csv`](<../data/products.csv>)
- [`docs`](<../docs>)
- [`docs/DATA_DICTIONARY.md`](<../docs/DATA_DICTIONARY.md>)
- [`notebooks`](<../notebooks>)
- [`notebooks/eda_analysis.ipynb`](<../notebooks/eda_analysis.ipynb>)
- [`outputs`](<../outputs>)
- [`outputs/dashboard_summary.html`](<../outputs/dashboard_summary.html>)
- [`outputs/rfm_customer_segments.csv`](<../outputs/rfm_customer_segments.csv>)
- [`powerbi`](<../powerbi>)
- [`powerbi/DAX_Measures.dax`](<../powerbi/DAX_Measures.dax>)
- [`recalibrate.py`](<../recalibrate.py>)
- [`requirements.txt`](<../requirements.txt>)
- [`run_project.py`](<../run_project.py>)
- [`sql`](<../sql>)
- [`sql/01_ddl_schema.sql`](<../sql/01_ddl_schema.sql>)
- [`sql/02_advanced_analytics.sql`](<../sql/02_advanced_analytics.sql>)
- [`src`](<../src>)
- [`src/__init__.py`](<../src/__init__.py>)
- [`src/etl.py`](<../src/etl.py>)
- [`tests`](<../tests>)
- [`tests/test_reconciliation.py`](<../tests/test_reconciliation.py>)
- [`tools`](<../tools>)
- [`tools/run_pipeline.py`](<../tools/run_pipeline.py>)
