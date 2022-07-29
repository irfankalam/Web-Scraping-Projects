import pandas as pd
import numpy as np


# Reading the csv file
df_new = pd.read_csv('output_90.csv')

# saving xlsx file
GFG = pd.ExcelWriter('output_90.xlsx')
df_new.to_excel(GFG, index = False)

GFG.save()
# GFG.close()
