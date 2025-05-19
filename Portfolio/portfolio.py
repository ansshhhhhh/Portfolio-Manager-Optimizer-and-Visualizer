import yfinance as yf
import numpy as np
from tabulate import tabulate
from scipy.optimize import minimize
from Portfolio.utils import *

class Portfolio():
    def __init__(self, tickers : list[str], weights = None):
        """
        Initialize the portfolio
        tickers : list[str]
        weights : list[float]
        """
        self.tickers = tickers
        self.num_assets = len(tickers)
        self.close = None
        self.adj_Close = None
        self.data = None
        self.daily_returns = None
        self.portfolio_daily_return = None
        self.total_return = None
        self.optimized = False
        
        if weights:
            self.weights = np.array(weights)
        else:
            self.weights = np.array([1/self.num_assets] * self.num_assets)

    def add_ticker(self, ticker : str):
        """
        Add a ticker to the portfolio
        ticker : str
        """
        self.tickers.append(ticker)
        self.num_assets += 1
        self.weights = np.concatenate((self.weights * (self.num_assets - 1) / self.num_assets, np.array([1/self.num_assets])))

    def remove_ticker(self, ticker : str):
        """
        Remove a ticker from the portfolio
        ticker : str
        """
        idx  = self.tickers.index(ticker)
        weight = self.weights[idx]
        self.num_assets -= 1
        dis = weight / self.num_assets
        self.weights = np.concatenate((self.weights[:idx] + dis, self.weights[idx+1:] + dis))
        self.tickers.remove(ticker)
        
    def update_weights(self, weights : list[float]):
        """
        Update the weights of the portfolio
        weights : list[float]
        """
        self.weights = np.array(weights)
        self.optimized = False
        

    def get_data(self, period = '5m'):
        """
        Get the data of the portfolio
        period : str
        """
        self.close = yf.download(self.tickers, period = period, auto_adjust=False)['Close']
        self.adj_close = yf.download(self.tickers, period = period, auto_adjust=False)['Adj Close']
        
    def clean_data(self):
        """
        Clean the data of the portfolio
        """
        if not (self.close and self.adj_close):
            self.get_data()
            
        self.close.interpolate(limit = 5, inplace = True)
        self.adj_close.interpolate(limit = 5, inplace = True)
        
        self.close.ffill(inplace = True)
        self.adj_close.ffill(inplace = True)
        
        self.data = self.adj_close
        
        print('Data cleaned successfully.')
        
    def calculate_return(self):
        """
        Calculate the daily returns of the portfolio
        """
        self.daily_returns = self.data.pct_change().dropna()
        daily_return = (self.weights * self.daily_returns)
        self.portfolio_daily_return = daily_return.sum(axis = 1)
        self.total_return = daily_return.sum()
        print('Return Calculated.')
        
    def performance(self): 
        """
        Calculate the performance metrics of the portfolio
        """
        table = [
            ['Performance Metrics', 'Value'],
            ['Cumulative Return', cummulative_return(self.portfolio_daily_return)],
            ['Annualized Return', annualized_return(self.portfolio_daily_return)],
            ['Annualized Volatility', volatility(self.portfolio_daily_return)],
            ['Sharpe Ratio', sharpe_ratio(self.portfolio_daily_return)],
            ['Max Drawdown', max_drawdown(self.portfolio_daily_return)]
        ]
        
        return tabulate(table,  headers='firstrow', tablefmt='github')

    def corr(self, rolling = False, window = None):
        """
        Calculate the correlation matrix of the portfolio
        rolling : bool
        window : int
        """
        if rolling:
            if not window:
                print('Provide window size for rolling correlation.')
                return 
            return self.daily_returns.rolling(window).corr().dropna()
        else:
            return self.daily_returns.corr()
        
    def optimize(self):
        """
        Optimize the portfolio
        """
        constraint = ({'type': 'eq', 'fun': lambda w: np.sum(w) - 1})
        range_ = tuple((0.0, 1.0) for _ in range(self.num_assets))
        w0 = self.weights.copy()
        
        def negativeSharpe(weights):
            return -sharpe_ratio((weights * self.daily_returns).sum(axis = 1))
        
        result = minimize(negativeSharpe, w0, method='SLSQP', bounds=range_, constraints=constraint)
        self.weights = np.array(result.x)
        self.optimized = True
        
        print('Weights updated succesfully')