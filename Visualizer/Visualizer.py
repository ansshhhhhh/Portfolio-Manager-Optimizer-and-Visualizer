import seaborn as sns
import matplotlib.pyplot as plt
from Portfolio.portfolio import Portfolio

class PortfolioVisualization:
    def __init__(self, portfolio : Portfolio):
        self.portfolio = portfolio
        self.portfolio_returns = portfolio.portfolio_daily_return
        self.asset_returns     = portfolio.daily_returns
        self.asset_prices      = portfolio.data
        
    def plot_cumulative_return(self):
        cum = (1 + self.portfolio_returns).cumprod()
        plt.figure(figsize=(10, 5))
        cum.plot()
        plt.title("Portfolio Cumulative Return")
        plt.ylabel("Growth")
        plt.xlabel("Date")
        plt.tight_layout()
        plt.show()
    
    def plot_correlation_heatmap(self):
        plt.figure(figsize=(8, 6))
        sns.heatmap(self.portfolio.corr(), annot=True, fmt=".2f", cmap="coolwarm", vmin=-1, vmax=1)
        plt.title("Asset Return Correlation Matrix")
        plt.tight_layout()
        plt.show()
    
    def plot_rolling_volatility(self, window=60):
        port_vol = self.portfolio_returns.rolling(window).std() * (252**0.5)
        asset_vol = self.asset_returns.rolling(window).std() * (252**0.5)

        plt.figure(figsize=(10, 5))
        port_vol.plot(label="Portfolio", linestyle='-')
        asset_vol.plot(alpha=0.7, linewidth=0.8)
        plt.title(f"{window}-Day Rolling Annualized Volatility")
        plt.ylabel("Volatility")
        plt.xlabel("Date")
        plt.legend(loc="upper left")
        plt.tight_layout()
        plt.show()

    def plot_drawdown_curve(self):
        cum = (1 + self.portfolio_returns).cumprod()
        peak = cum.cummax()
        dd = cum / peak - 1

        plt.figure(figsize=(10, 4))
        dd.plot()
        plt.title("Portfolio Drawdown Curve")
        plt.ylabel("Drawdown")
        plt.xlabel("Date")
        plt.tight_layout()
        plt.show()

    def plot_asset_performance(self):
        norm = self.asset_prices / self.asset_prices.iloc[0]
        plt.figure(figsize=(10, 5))
        norm.plot()
        plt.title("Individual Asset Performance (Normalized)")
        plt.ylabel("Normalized Price")
        plt.xlabel("Date")
        plt.legend(loc="upper left")
        plt.tight_layout()
        plt.show()
        

    def visualize_portfolio_performance(self):
        self.plot_cumulative_return()
        self.plot_drawdown_curve()