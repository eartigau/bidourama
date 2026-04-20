# Growthorama

Small static web app for exploring an investment account that grows with market returns, applies management fees, then switches to a fixed real-dollar withdrawal rule once withdrawals begin.

## What it does

- Runs one deterministic projection in Python directly in the browser with Pyodide.
- Applies the average market return and yearly management fees to the portfolio.
- Shows every stage both with fees and without fees.
- Compares yearly withdrawals with fees against the no-fee reference.
- Shows the cumulative value lost to fees over time.

## Inputs

- Portfolio today
- Current age
- Age at start of withdrawals
- Maximum age
- Market average return
- Withdrawal rate once withdrawals start
- Management fee
- Inflation

## How to run

Serve the folder with any simple static web server and open `index.html` in a browser. For example:

```sh
python3 -m http.server 8000
```

Then visit `http://localhost:8000`.

## Notes

- All displayed values are deflated back into today's dollars.
- The withdrawal rule is based on the real value of the portfolio at the start of withdrawals.
- If the withdrawal-start age is equal to the maximum age, the model performs no withdrawals.
- Management fees are applied every year after growth.
- This is a planning toy, not financial advice.