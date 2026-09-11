def create_holding(ticker, shares, cost_basis): 
    return { 
    "ticker": ticker,
    "shares": shares,
    "cost_basis": cost_basis
} 
portfolio=[]
holding1 = create_holding(ticker="AAPL", shares=10, cost_basis=150.00)
holding2 = create_holding(ticker="MSFT", shares=20, cost_basis=250.00)
holding3 = create_holding(ticker="GOOG", shares=30, cost_basis=350.00)
portfolio.append(holding1)
portfolio.append(holding2)
portfolio.append(holding3)
print(portfolio)
