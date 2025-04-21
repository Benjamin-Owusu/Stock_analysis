import numpy as np
import pandas as pd

def growth_rate(x):
    return 100*(x - x.shift(1))/ (x.shift(1))



def log_returns(x):
    return 100*(np.log(x / x.shift(1)))


