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
#print(portfolio)

def calculate_total_value(portfolio):
    total=0
    for holding in portfolio:
        total+=holding["shares"]*holding["cost_basis"]
    return total
total_value = calculate_total_value(portfolio)
print(total_value)

class Holding:
   def __init__(self,ticker,shares,cost_basis):
       self.ticker=ticker
       self.shares=shares
       self.cost_basis=cost_basis

   def calculate_value(self):
       return self.shares * self.cost_basis
       
holding_1= Holding("AAPL" , 10, 150.00)
print(holding_1.ticker)
print(holding_1.shares)
print(holding_1.calculate_value())




