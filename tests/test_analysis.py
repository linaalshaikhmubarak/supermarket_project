import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
from analysis import average_sales,total_sales_by_branch

df_real = pd.read_csv('data/supermarket_sales.csv')

def test_average_sales_real_data():
    avg=average_sales(df_real)
    assert avg>0


def test_total_sales_by_branch_real_data():
    total_cairo=total_sales_by_branch(df_real,'Cairo')
    assert total_cairo>0


def test_total_sales_non_existing_branch_real_data():
 total_paris=total_sales_by_branch(df_real,'Paris')
 assert total_paris==0

