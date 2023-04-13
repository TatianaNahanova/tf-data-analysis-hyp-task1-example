import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest


chat_id = 230790372 # Ваш chat ID, не меняйте название переменной


def solution(x_success: int,
             x_cnt: int,
             y_success: int,
             y_cnt: int) -> bool:  # x -контроль, y -тест

    alpha = 0.07

    count = np.array([x_success, y_success])
    nobs = np.array([x_cnt, y_cnt])
    _, pvalue = proportions_ztest(count, nobs, alternative='smaller')

    if pvalue <= alpha:
        is_rejected = True
    else:
        is_rejected = False

    return is_rejected
