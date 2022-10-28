# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn import datasets
import mlflow

def main():

    mlflow.autolog()

    params = {
        "model":"lr"
        }

    mlflow.log_params(params)

    diabetes = datasets.load_diabetes()
    X, y = diabetes.data, diabetes.target

    if params["model"] == "lr":
        model = LinearRegression(fit_intercept=False)
    elif params["model"] == "gb":
        model = GradientBoostingRegressor()
    else:
        raise ValueError('The model parameter should be either lr or gb')

    model.fit(X, y)

if __name__ == "__main__":
    main()

# %%
