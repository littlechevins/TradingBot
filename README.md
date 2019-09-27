# About

A study on trading bots using small time frames and fast in and out trades.
 
We use a 20 and 5 day EMA strategy where buy's are executed when the 20 day crosses over the 5 day. A sell order is executed when the 20 day crosses under. Currently there are no long/short orders.


# Technical

 Built using python, it utilises the **pandas** framework to keep track of the 20 and 5 day EMA

**EMA:** Exponential moving average, a type of moving average with greater weight placed towards the most recent data points.

## How to

1. Run using 'python ./bot'
2. Back testing can be performed with the './backtest' engine. 

Note: data files need to downloaded separately. Python script to do so located in /historical
