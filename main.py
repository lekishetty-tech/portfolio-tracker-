import json

class Holding:
   def __init__(self,ticker,shares,cost_basis):
       self.ticker=ticker
       self.shares=shares
       self.cost_basis=cost_basis

   def calculate_value(self):
       return self.shares * self.cost_basis

   def to_dict(self):
       return {
          "ticker": self.ticker,
          "shares": self.shares,
          "cost_basis": self.cost_basis
    }

def calculate_total_value(portfolio):
    total=0
    for holding in portfolio:
       total+= holding.calculate_value()
    return total
  
portfolio=[]       
holding1= Holding("AAPL",10,150.00)
holding2= Holding("MSFT",20,250.00)
holding3= Holding("GOOG",30,350.00)
portfolio.append(holding1)
portfolio.append(holding2)
portfolio.append(holding3)
#print(holding1.ticker)
#print(holding1.shares)
#print(holding1.calculate_value())
total_value=calculate_total_value(portfolio)
#print(total_value)
#print(holding1.to_dict())
holdings_as_dicts = [holding.to_dict() for holding in portfolio]
with open("portfolio.json","w") as f:
   json.dump(holdings_as_dicts, f)
try:
    with open("portfolio.json", "r") as f:
        loaded_portfolio = json.load(f)
    loaded_holdings = [Holding(d["ticker"], d["shares"], d["cost_basis"]) for d in loaded_portfolio]
except FileNotFoundError:
    print("no saved portfolio yet, start fresh.")
    loaded_holdings = []
except json.JSONDecodeError:
    print("portfolio.json is corrupted, starting fresh")
    loaded_holdings = []

print(calculate_total_value(loaded_holdings))
        






