# COD and RTO Analytics

Compare prepaid versus cash-on-delivery fulfillment, returns, and estimated logistics losses.

A practical, independent Python/Streamlit demo project using **synthetic sample data**. No customer information, passwords, or Shopify credentials are included.

## Features

- Upload your own CSV or use the included example file.
- Explore the analysis with interactive controls.
- Download the results where available.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Dataset

Sample: `sample_fulfillment.csv`. Review its columns before uploading your own data.

## Privacy and limitations

Sample data is fictional. Treat outputs as planning estimates, not audited figures. Do not commit customer phone numbers, addresses, credentials, or private order exports to a public repository.

## Author notes

Developed as a portfolio-ready starter app. Customize assumptions, tests, and integrations before production use.
