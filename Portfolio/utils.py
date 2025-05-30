import numpy as np

def cummulative_return(returns):
    """
    Calculate the cummulative return of a portfolio
    """
    return float((1 + returns).cumprod().iloc[-1] - 1)

def annualized_return(returns):
    """
    Calculate the annualized return of a portfolio
    """
    return float(returns.mean() * 252)

def annualized_volatility(returns):
    """
    Calculate the annualized volatility of a portfolio
    """
    return float(returns.std() * np.sqrt(252))

def sharpe_ratio(returns, risk_free_rate = 0.06):
    """
    Calculate the sharpe ratio of a portfolio
    """
    return float((annualized_return(returns) - risk_free_rate) / annualized_volatility(returns))

def max_drawdown(returns):
    """
    Calculate the max drawdown of a portfolio
    """
    return float(np.max(returns.cummax() - returns))

def volatility(returns):
    """
    Calculate the volatility of a portfolio
    """
    return float(returns.std())

