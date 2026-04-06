# Growthorama

Small static web app for exploring an investment account that grows with market returns, then switches to a fixed real-dollar withdrawal rule at retirement.

## What it does

- Runs 100 Monte Carlo market paths in Python directly in the browser with Pyodide.
- Shows the mean yearly withdrawal in today's dollars with a mean plus/minus one standard deviation band.
- Overlays histograms for the account value at retirement and the value left to heirs at death.

## Inputs

- Portfolio today
- Current age
- Start of withdrawal
- Death age
- Market average return
- Yearly RMS volatility
- Withdrawal rate at retirement
- Inflation

## How to run

Serve the folder with any simple static web server and open `index.html` in a browser. For example:

```sh
python3 -m http.server 8000
```

Then visit `http://localhost:8000`.

## Notes

- All displayed values are deflated back into today's dollars.
- The withdrawal rule is based on the real value of the portfolio at retirement.
- This is a planning toy, not financial advice.