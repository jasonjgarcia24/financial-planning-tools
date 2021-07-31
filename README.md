# <a id="Top-of-Page"> Welcome to the Financial Planning Tool!</a>
#### A tool for current valuation and predictive analysis of portfolio allocations.

***
## <a id="Contents">Cotents</a>
[Project Description](#Project-Description)<br>
[Technologies](#Technologies)<br>
[Installation Guide](#Installation-Guide)<br>
[Usage](#Usage)<br>
[Contributors](#Contributors)<br>
[License](#License)<br>
[Bottom of Page](#Bottom-of-Page)<br>

***
## <a id="Project-Description">Project Description</a>
This project provides up-to-date current portfolio analysis and future estimated projections.

#### A summary of what's under the hood:    
This project is composed of two main financial analysis tools:
1. **Emergencies:** A financial planner for emergencies. The members will be able to use this tool to visualize their current savings. The members can then determine if they have enough reserves for an emergency fund.<br><br>
2. **Retirment:** A financial planner for retirement. This tool will forecast the performance of their retirement portfolio in 30 and 10 years. To do this, the tool will make an Alpaca API call via the Alpaca SDK to get historical price data for use in Monte Carlo simulations.<br>

Using Jupyter notebook, this tool gathers current crypto and stock and bond for a user's portfolio. The modeled assets are:
 - Bitstamp and Coinbase (for crypto)
 - SPDR S&P 500 ETF Trust and iShares Core US Aggregate Bond ETF (for stock and bonds).<br>

The tool also models an average monthly household income of 12,000 USD.<br>

All historical information for crypto assets is collected from the <a href="https://alternative.me/crypto/api/" target="_blank">Free Crypto API</a>, and for the stock and bond assets we use the <a href="https://alpaca.markets/" target="_blank">Alpaca SDK</a>.<br>
#### Project layout:
The layout of essentials for this project is show below.
<p><a href="tree.txt"><img src="img/project_tree.png" title="price-dislocation project tree"></a></p>

**Note:** <code>.env</code> is only a refernece to show how and where it should be in the project structure. Please use <code>SAMPLE.env</code> as a reference template for your own <code>.env</code> file.

***
## <a id="Technologies">Technologies</a>
<a href="https://docs.python.org/release/3.8.0/" title="https://docs.python.org/release/3.8.0/"><img src="https://img.shields.io/badge/python-3.8%2B-red">
<a href="https://pandas.pydata.org/docs/" title="https://pandas.pydata.org/docs/"><img src="https://img.shields.io/badge/pandas-1.3.0-green"></a>
<a href="https://jupyter-notebook.readthedocs.io/en/stable/" title="https://jupyter-notebook.readthedocs.io/en/stable/"><img src="https://img.shields.io/badge/jupyter--notebook-6.4.0-green"></a><a href="https://docs.python-requests.org/en/master/" title="https://docs.python-requests.org/en/master/"><img src="https://img.shields.io/badge/requests-2.24.0-green"></a>
<a href="https://github.com/theskumar/python-dotenv" title="https://github.com/theskumar/python-dotenv"><img src="https://img.shields.io/badge/python--dotenv-0.18.0-orange"></a>
<a href="https://pypi.org/project/alpaca-trade-api/" title="https://pypi.org/project/alpaca-trade-api/"><img src="https://img.shields.io/badge/alpaca--trade--api-1.2.3-orange"></a>
<a href="https://dateutil.readthedocs.io/en/stable/" title="https://dateutil.readthedocs.io/en/stable/"><img src="https://img.shields.io/badge/dateutil-2.8.2-green"></a>
<a href="https://matplotlib.org/" title="https://matplotlib.org/"><img src="https://img.shields.io/badge/matplotlib-3.3.4-blue"></a>
<br>
<a href="requirements.txt" title="requirements.txt">Requirements List</a>

***
## <a id="Installation-Guide">Installation Guide</a>
### Project Installation
To install <a href="https://github.com/jasonjgarcia24/financial-planning-tools" title="https://github.com/jasonjgarcia24/financial-planning-tools">financial-planning-tools</a>, type <code>git clone https://github.com/jasonjgarcia24/financial-planning-tools.git</code> into bash in your prefered local directory.<br><br>
Alternatively, you can navigate to the same address (<code>https://github.com/jasonjgarcia24/financial-planning-tools.git</code>) and download the full <code>main</code> branch's contents as a zip file to your prefered local directory.<br>

### Setting Environment Variables
A <code>.env</code> file is required for use with the <a href="https://alpaca.markets/" target="_blank">Alpaca SDK</a>. The Alpaca SDK will check the environment for a number of variables that can be used rather than hard-coding these into your scripts.

| Environment                        | Description           |
| ---------------------------------- | --------------------- |
| ALPACA_API_KEY=<key_id>            | Your API Key          |
| ALPACA_API_SECRET_KEY=<secret_key> | Your API Secret Key   |

***
## <a id="Usage">Usage</a>
### Inputs
Observe financial-planning-tools with <code>financial_planning_tools.ipynb</code>. No input variables are required if the default assets are used.<br>

### Outputs
This tool provides five main different expected types of textual outputs:
1. An asset's current closing price:<br>
<img src="./img/closing_price_print.png" title="Current closing price"><br>

2. An asset's current closing value:<br>
<img src="./img/closing_value_print.png" title="Current closing value"><br>

3. A portfolio's current closing value:<br>
<img src="./img/closing_portfolio_balance_print.png" title="Current portfolio closing balance"><br>

4. A portfolio's proejcted valuation summary with confidence indices:<br>
<img src="./img/projection_summary_statistics.png" title="Projected portfolio summary statistics"><br>

5. A portfolio's projected valuation with confidence indices:
<img src="./img/ci_portfolio_print.png" title="Projected portfolio valuation with confidence indices"><br>

The tools also provides four different expected visualizations:
1. A pie chart summarizing the portfolio composition:<br>
<img src="./img/portfolio_composition_plot_pie.png" title="Portfolio composition-simple"><br>

2. A pie chart outlining the complete portfolio composition:<br>
<img src="./img/portfolio_composition_plot_donut.png" title="Portfolio composition-complete"><br>

3. A projection line chart from a Monte Carlo simulation:<br>
<img src="./img/monte_carlo_plot_line.png" title="Monte Carlo line plot"><br>

4. A projection distribution chart from a Monte Carlo simulation:<br>
<img src="./img/monte_carlo_plot_freq.png" title="Monte Carlo distribution plot">

***
## <a id="Contributors">Contributors</a>
Currently just me :)<br>

***
## <a id="License">License</a>
Each file included in this repository is licensed under the <a href="https://github.com/jasonjgarcia24/financial-planning-tools/blob/main/LICENSE" title="github.com/jasonjgarcia24/financial-planning-tools/blob/main/LICENSE">MIT License.</a>

***
[Top of Page](#Top-of-Page)<br>
[Contents](#Contents)<br>
[Project Description](#Project-Description)<br>
[Technologies](#Technologies)<br>
[Installation Guide](#Installation-Guide)<br>
[Usage](#Usage)<br>
[Contributors](#Contributors)<br>
[License](#License)<br>
<a id="Bottom-of-Page"></a>
