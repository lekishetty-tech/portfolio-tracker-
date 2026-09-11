def create_holding(ticker, shares, cost_basis): 
    return { 
    "ticker": ticker,
    "shares": shares,
    "cost_basis": cost_basis
} 
holding1 = create_holding(ticker="AAPL", shares=10, cost_basis=150.00)
print(holding1 )