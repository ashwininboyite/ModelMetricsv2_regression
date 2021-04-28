# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 12:26:59 2021

@author: aboyite
"""

import json
import pandas as pd
from sklearn.metrics import accuracy_score

#modelop.init
def begin():
    pass

#modelop.score
def action(datum):
    yield datum

#modelop.score
def compute_metrics(data):
    """
    A function to evaluate a classification model
    
    param: y: true (actual) labels
    param: y_preds: predicted labels (as scored by model)
    
    return: mutiple classification performance metrics
    """
    print(data)
    data = pd.DataFrame(data)
    data.columns = ['prediction','actual']
    
    y = pd.to_numeric(data['prediction'])
    y_preds = pd.to_numeric(data['actual'])
    
    metrics = {  
    "accuracy":accuracy_score(y, y_preds)
    }
    print(metrics)
    
    yield metrics 
