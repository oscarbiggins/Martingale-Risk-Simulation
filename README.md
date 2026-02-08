# Martingale-Risk-Simulation
**Author:** Oscar
## Project Overview
This is a python-based project modeling a Monte Carlo Simulation designed to model the Martingale betting strategy. As an Applied Mathematics and Statistics graduate I completed this visualisation in order to show the convergence of wealth towards zero for players with a finite wealth, despite the underlying stochastic process initially seeming to have a fair nature.

## The Mathematics
The Martingale strategy is a process $X_n$ such that the conditional expectation of the subsequent value, given the current value, is equal to the current value. In mathematical terms:
$$E[X_{n+1} | X_n = X_n$$

## Features
\itemise{
\item{**Object-Oriented Programming:**}
\item{**Liquidity Logic**}
\item{**Visualisation**}
}
## How to Run
1. Clone the repository.
2. Install dependencies: `pip install matplotlib`.
3. Run `python martingale_sim.py`.
