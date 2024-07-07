import os

import toolkit_config as cfg

import yf_example2

def qan_prc_to_csv(year):
    start_period = f"{year}-01-01"
    end_period = f"{year}-12-31"
    ticker = 'QAN.AX'
    file_name = f"qan_prc_{year}.csv"
    file_path = cfg.DATA_DIR + '/' + file_name
    yf_example2.yf_prc_to_csv(ticker, start_period, end_period, file_path)
if __name__ == "__main__":
    qan_prc_to_csv(2020)
