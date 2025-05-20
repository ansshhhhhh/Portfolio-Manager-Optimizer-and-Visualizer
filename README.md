# Portfolio Manager Optimizer and Visualizer

A Python-based tool for portfolio management, optimization, and visualization that helps investors analyze and optimize their investment portfolios.

## Features

### Portfolio Management
- Create and manage portfolios with multiple assets
- Add or remove assets dynamically
- Download historical price data using Yahoo Finance
- Calculate daily returns and portfolio performance metrics
- Clean and preprocess financial data

### Portfolio Optimization
- Optimize portfolio weights using Modern Portfolio Theory
- Maximize Sharpe ratio for optimal risk-adjusted returns
- Support for custom weight constraints
- Automatic rebalancing capabilities

### Performance Analysis
- Calculate key performance metrics:
  - Cumulative returns
  - Annualized returns
  - Volatility
  - Sharpe ratio
  - Maximum drawdown
- Generate correlation matrices
- Rolling correlation analysis

### Visualization
- Interactive portfolio performance visualizations:
  - Cumulative return plots
  - Correlation heatmaps
  - Rolling volatility charts
  - Drawdown curves
  - Individual asset performance comparison
- Customizable visualization parameters

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Portfolio-Manager-Optimizer-and-Visualizer.git
cd Portfolio-Manager-Optimizer-and-Visualizer
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Portfolio Creation and Analysis
```python
from Portfolio.portfolio import Portfolio
from Visualizer.Visualizer import PortfolioVisualization

# Create a portfolio with initial assets
portfolio = Portfolio(['AAPL', 'GOOG', 'MSFT'])

# Download and clean data
portfolio.get_data(period='5y')
portfolio.clean_data()

# Calculate returns
portfolio.calculate_return()

# View performance metrics
print(portfolio.performance())

# Create visualizations
visualizer = PortfolioVisualization(portfolio)
visualizer.visualize_portfolio_performance()
```

### Portfolio Optimization
```python
# Optimize portfolio weights
portfolio.optimize()

# View updated weights
print(portfolio.weights)
```

## Project Structure
```
Portfolio-Manager-Optimizer-and-Visualizer/
├── Portfolio/
│   ├── portfolio.py    # Core portfolio management functionality
│   └── utils.py        # Utility functions
├── Visualizer/
│   └── Visualizer.py   # Visualization capabilities
├── main.ipynb          # Example usage and testing
└── README.md
```

## Dependencies
- yfinance: Yahoo Finance data download
- numpy: Numerical computations
- pandas: Data manipulation
- scipy: Optimization algorithms
- matplotlib: Basic plotting
- seaborn: Advanced visualizations
- tabulate: Pretty printing of tables

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the [Apache License](LICENSE) - see the LICENSE file for details.