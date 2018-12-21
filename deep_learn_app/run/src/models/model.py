#!/usr/bin/env python3

from src.models import regression_train
from src.models import regression_predict
from src.models import regression_labels

def train():
    regression_train.train()
def predict(x):
    return regression_predict.predict(x)
def labels():
    return regression_labels.labels()
