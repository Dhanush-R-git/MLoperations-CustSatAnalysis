# MLoperations-CustSatAnalysis

## Predicting how a customer will feel about a product before they even ordered it

**Problem statement**: For a given customer's historical data, we are tasked to predict the review score for the next order or purchase. We will be using the [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce). This dataset has information on 100,000 orders from 2016 to 2018 made at multiple marketplaces in Brazil. Its features allow viewing charges from various dimensions: from order status, price, payment, freight performance to customer location, product attributes and finally, reviews written by customers. The objective here is to predict the customer satisfaction score for a given order based on features like order status, price, payment, etc. In order to achieve this in a real-world scenario, we will be using [ZenML](https://zenml.io/) to build a production-ready pipeline to predict the customer satisfaction score for the next order or purchase.

# How to run?

## :snake: Python Requirements

Clone the repository

```bash
https://github.com/Dhanush-R-git/MLoperations-CustSatAnalysis
```
### Create a conda environment after opening the repository

```bash
conda create -n ml.env.0.0.0 python=3.11.9 -y
```

```bash
conda activate ml.env.0.0.0
```

### install the requirements
```bash
pip install -r requirements.txt
```

### run app.py
```bash
python stramlit_app.py
```

Now,
```bash
open up you local host and port
```

Starting with ZenML 0.20.0, ZenML comes bundled with a React-based dashboard. This dashboard allows you
to observe your stacks, stack components and pipeline DAGs in a dashboard interface. To access this, it is need to [launch the ZenML Server and Dashboard locally](https://docs.zenml.io/user-guide/starter-guide#explore-the-dashboard) 
but first you must install the optional dependencies for the ZenML server:

```bash
pip install zenml["server"]
zenml up 
or
zenml init
```
To match the server version 
```bash
zenml downgrade
```

To `run_deployment.py` script, it need to install some integrations using ZenML:

```bash
zenml integration install mlflow -y
```


